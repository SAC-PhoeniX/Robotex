const int trigPin1 = 2;
const int echoPin1 = 3;
const int trigPin2 = 11;
const int echoPin2 = 12;
const int minDistance = 12;
const int delaybetweenturns = 210; 

//Sensor 1 right
//Sensor 2 Mid
//Sensor3 left



bool mswitch{};


const int trigPin3 = 18;
const int echoPin3 = 19;
// defines variables
unsigned long duration;
int distance;
int distances[3];

long ctr;
long ctr2;
long ctr3;

char state = 'f';


int calcdif(int leftspeed) {
  // int rightspeed{};
  // int dif[];
  //241,246
  const int increase = -5;
  return leftspeed + increase < 255 ? leftspeed + increase : 255;
}


void getsensordata() {

  // Clears the trigPin
  digitalWrite(trigPin1, LOW);
  delayMicroseconds(2);
  // Sets the trigPin on HIGH state for 10 micro seconds
  digitalWrite(trigPin1, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin1, LOW);
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin1, HIGH, 100000); //The Third Param Allows us to limit the time waited for each sensor, we dont want to mresure a target 2000 meters away 
  // Calculating the distance
  distance = duration * 0.034 / 2;
  // Prints the distance on the Serial Monitor
  //Serial.print("Distance1: ");
  //Serial.println(distance);
  distances[0] = distance;

  // Clears the trigPin
  digitalWrite(trigPin2, LOW);
  delayMicroseconds(2);
  // Sets the trigPin on HIGH state for 10 micro seconds
  digitalWrite(trigPin2, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin2, LOW);
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin2, HIGH,100000);
  // Calculating the distance
  distance = duration * 0.034 / 2;
  // Prints the distance on the Serial Monitor
  //Serial.print("Distance2: ");
  //Serial.println(distance);
  distances[1] = distance;

  // Clears the trigPin
  digitalWrite(trigPin3, LOW);
  delayMicroseconds(2);
  // Sets the trigPin on HIGH state for 10 micro seconds
  digitalWrite(trigPin3, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin3, LOW);
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin3, HIGH,100000);
  // Calculating the distance
  distance = duration * 0.034 / 2;
  // Prints the distance on the Serial Monitor
  //Serial.print("Distance3: ");
  //Serial.println(distance);

  distances[2] = distance;
}

void setmotorvels(uint8_t left, uint8_t right, bool nodif = false) {
  analogWrite(10, left);  // Left Wheel
  if (nodif) {
    analogWrite(9, right);
    //Serial.println("Motor Vels " + String(left) + ", " + String(right) + " : Nodif");
  } else {
    analogWrite(9, calcdif(left));

    //Serial.println("Motor Vels " + String(left) + ", " + String(calcdif(left)) + " : Dif");
  }
  return;
};
void foward() {
  digitalWrite(4, LOW);
  digitalWrite(5, HIGH);
  digitalWrite(6, HIGH);
  digitalWrite(7, LOW);
  setmotorvels(246, 241);
  state = 'f';
  Serial.println("foward");
}

void backward() {
  digitalWrite(4, HIGH);
  digitalWrite(5, LOW);
  digitalWrite(6, LOW);
  digitalWrite(7, HIGH);
  setmotorvels(241, 246);
  state = 'b';
  Serial.println("backward");
}

void turnleft(int dif) {
  setmotorvels(241, 0, true);
  //Serial.println((700 - (dif * 50)>0));
  delay(delaybetweenturns);
  foward();
  Serial.println("left");
}

void turnright(int dif) {
  setmotorvels(0, 246, true);
  Serial.println((700 - (dif * 50)>0));
  delay(delaybetweenturns);
  foward();
  Serial.println("right");
}



void setup() {
  //Sensors
  pinMode(trigPin1, OUTPUT);  // Sets the trigPin as an Output
  pinMode(echoPin1, INPUT);   // Sets the echoPin as an Input
  pinMode(trigPin2, OUTPUT);  // Sets the trigPin as an Output
  pinMode(echoPin2, INPUT);   // Sets the echoPin as an Input
  pinMode(trigPin3, OUTPUT);  // Sets the trigPin as an Output
  pinMode(echoPin3, INPUT);   // Sets the echoPin as an Input

  //Motors
  pinMode(4, OUTPUT);   // Motor init
  pinMode(5, OUTPUT);   // Motor init
  pinMode(6, OUTPUT);   // Motor init
  pinMode(7, OUTPUT);   // Motor init
  pinMode(9, OUTPUT);   // Motor init
  pinMode(10, OUTPUT);  // Motor init
  // put your setup code here, to run once:
  Serial.begin(9600);  // Starts the serial communication

  digitalWrite(4, HIGH);
  digitalWrite(5, LOW);
  digitalWrite(6, LOW);
  digitalWrite(7, HIGH);
}

void loop() {
  ctr = millis();
  getsensordata();

  //distances debugging
  Serial.print("Distances: ");
  for (auto a : distances) {
    Serial.print(a);
    Serial.print(" ");
  }
  Serial.print('\n');

  //handles the turn logic

  if ((distances[0] <= minDistance) && (distances[0]!=0)) {
    if (distances[1] < minDistance ){
        turnleft(distances[2] - distances[0]);
      }
    else {
      turnleft((distances[2] - distances[1]));
    }
  } else if ((distances[2] <= minDistance )&& (distances[2]!=0)) {
    if (distances[2]< minDistance){
        turnright(distances[1] - distances[2]);
      }
    else {
      turnright((distances[1] - distances[2] ));
    }
  } else if (distances[1] < minDistance+3 && distances[1]!=0) {
    //backward
    backward();
    delay(500);
    foward();
    delay(100);

    if(distances[0]<distances[2]){
        turnleft(100);
    }else{
      turnright(100);
    }
 

  }
  else{
      foward();
  }

}
