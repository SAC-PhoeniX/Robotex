int const ena = 9;
int const enb = 10;

void setup() {
  pinMode(4, OUTPUT);   // LED init
  pinMode(5, OUTPUT);   // LED init
  pinMode(6, OUTPUT);   // LED init
  pinMode(7, OUTPUT);   // LED init
  pinMode(9, OUTPUT);   // LED init
  pinMode(10, OUTPUT);  // LED init
  // put your setup code here, to run once:
}

void loop() {
  // put your main code here, to run  repeatedly:
  digitalWrite(4, HIGH);
  digitalWrite(5, LOW);
  digitalWrite(6, HIGH);
  digitalWrite(7, LOW);
  for (int i = 0; i < 255; i++) {
    analogWrite(9, i);
    analogWrite(10, i);
    delay(100);
  }
}
