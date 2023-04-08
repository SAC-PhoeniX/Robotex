package robotex;


import lejos.hardware.port.SensorPort;
import lejos.hardware.sensor.EV3UltrasonicSensor;
import lejos.hardware.sensor.NXTUltrasonicSensor;
import lejos.hardware.Button;
import lejos.hardware.lcd.LCD;
import lejos.hardware.motor.Motor;
import lejos.utility.Delay;

public class project {
	
	static float diameter = 3.1f;
	static float pi = 3.14f;
	static float vehicleWidth = 15.8f;
	static int tooCloseDist = 10;
	static int defaultSpeed = 1080;

	static EV3UltrasonicSensor sonar1;
	static NXTUltrasonicSensor sonar2;
	static EV3UltrasonicSensor sonar3;
	
	static float[] oldDistances = new float[3];
	
	public static float convertToDegree(float centimeter) {
		float oneTurnDistance = diameter*pi;
		float distance = centimeter/oneTurnDistance;
		
		return distance*360;
		
	}
	
	public float convertToCentimeter(float meter) {
		return 100*meter;
	}
	
	public static void goForward(float centimeter, int speed) {
		
		
		Motor.A.setSpeed(speed);
		Motor.B.setSpeed(speed);
		
		Motor.A.rotate((int) convertToDegree(centimeter), true);
		Motor.B.rotate((int) convertToDegree(centimeter), true);
		
		while (Motor.A.isMoving() || Motor.B.isMoving()) {
			Delay.msDelay(10);
		}
		
	}
	
	public static void goBackward(float centimeter, int speed) {
		
		
		Motor.A.setSpeed(speed);
		Motor.B.setSpeed(speed);
		
		Motor.A.rotate(-(int) convertToDegree(centimeter), true);
		Motor.B.rotate(-(int) convertToDegree(centimeter), true);
		
		while (Motor.A.isMoving() || Motor.B.isMoving()) {
			Delay.msDelay(10);
		}
		
	}
	
	public static void turnRight90(int speed) {

		float turnDistance = vehicleWidth*pi/4;
		Motor.A.setSpeed(speed);
		Motor.B.setSpeed(speed);

		Motor.A.rotate((int) convertToDegree(turnDistance), true); //-(int) convertToDegree(vehicleWidth)
		Motor.B.rotate(-(int) convertToDegree(turnDistance), true);

		while (Motor.A.isMoving() || Motor.B.isMoving()) {
			Delay.msDelay(10);
		}
		
	}
	
	public static void turnLeft90(int speed) {

		float turnDistance = vehicleWidth*pi/4;
		
		Motor.A.setSpeed(speed);
		Motor.B.setSpeed(speed);

		Motor.A.rotate(-(int) convertToDegree(turnDistance), true); //-(int) convertToDegree(vehicleWidth)
		Motor.B.rotate((int) convertToDegree(turnDistance), true);

		while (Motor.A.isMoving() || Motor.B.isMoving()) {
			Delay.msDelay(10);
		}
		
	}
		
	public static void turnRight45(int speed) {

		float turnDistance = vehicleWidth*pi/8;
		Motor.A.setSpeed(speed);
		Motor.B.setSpeed(speed);

		Motor.A.rotate(-(int) convertToDegree(turnDistance), true); //-(int) convertToDegree(vehicleWidth)
		Motor.B.rotate((int) convertToDegree(turnDistance), true);

		while (Motor.A.isMoving() || Motor.B.isMoving()) {
			Delay.msDelay(10);
		}
		
	}
	
	public static void turnLeft45(int speed) {

		float turnDistance = vehicleWidth*pi/8;
		
		Motor.A.setSpeed(speed);
		Motor.B.setSpeed(speed);

		Motor.A.rotate((int) convertToDegree(turnDistance), true); //-(int) convertToDegree(vehicleWidth)
		Motor.B.rotate(-(int) convertToDegree(turnDistance), true);

		while (Motor.A.isMoving() || Motor.B.isMoving()) {
			Delay.msDelay(10);
		}
		
	}
	
	public static float[] getAllDistances(EV3UltrasonicSensor sonar1,NXTUltrasonicSensor sonar2,EV3UltrasonicSensor sonar3) {
		float [] distances = new float[3];
		sonar1.getDistanceMode().fetchSample(distances, 0);
		sonar2.getDistanceMode().fetchSample(distances, 1);
		sonar3.getDistanceMode().fetchSample(distances, 2);
		
		return distances;
	}
	
	public static float[] get360Distances(NXTUltrasonicSensor sonar) {
		// do a 360 turn and get the distances from the middle sensor while doing it
		// NOT FINISHED
		float[] distances = new float [36];
		float turnDistance = vehicleWidth*pi/36;
		// sonar2.getDistanceMode().fetchSample(distances, null);
		Motor.A.rotate((int) turnDistance);
		// 1080 degree/second
		while (Motor.A.isMoving() || Motor.B.isMoving()) {
			
		}
		return distances;
	}

	public static void mainLoop(EV3UltrasonicSensor sonar1, NXTUltrasonicSensor sonar2,EV3UltrasonicSensor sonar3) {
		while (Button.DOWN.isUp()) {
			
			float[] distances = getAllDistances(sonar1, sonar2, sonar3);
			float ls = distances[0]*100, fs = distances[1]*100, rs = distances[2]*100;
			
			
			if (oldDistances[0] != 0 || oldDistances[1] != 0 || oldDistances[2] != 0 ) {
				
			
				if (Float.isInfinite(ls)) {
					if(oldDistances[0]*100 > 40) {
						ls = 150;
					}else {
						ls = 5;
					}
					
				}
				
				if (Float.isInfinite(fs)) {
					if(oldDistances[1]*100 > 40) {
						fs = 150;
					}else {
						fs = 5;
					}
				}
				
				if (Float.isInfinite(rs)) {
					if(oldDistances[2]*100 > 40) {
						rs = 150;
					}else {
						rs = 5;
					}
				}
			}
			
			LCD.clear();

			System.out.println("Left s:"+String.valueOf(ls));
			System.out.println("Mid s:"+String.valueOf(fs));
			System.out.println("Right s:"+String.valueOf(rs));

			
			if (fs > tooCloseDist) {
				
				goForward(fs-tooCloseDist + 1, defaultSpeed);
				System.out.println("Goint Forward: "+ String.valueOf(fs-tooCloseDist));
				
				distances = getAllDistances(sonar1, sonar2, sonar3);
				rs = distances[0]*100; fs = distances[1]*100; ls = distances[2]*100;
				
				if (fs <= tooCloseDist) {
					if (rs > ls && rs > tooCloseDist) {
						System.out.println("turning right");
						turnRight90(defaultSpeed);
						
					} else if (ls > rs && ls > tooCloseDist) {
						System.out.println("turning left");
						turnLeft90(defaultSpeed);
					} 
					
				}else {
					Delay.msDelay(2000);
					continue;
				}
				
			} else if (rs > ls && rs > tooCloseDist) {
				turnRight90(defaultSpeed);
				System.out.println("turning right");

				
			} else if (ls > rs && ls > tooCloseDist) {
				turnLeft90(defaultSpeed);
				System.out.println("turning left");
			}
			Delay.msDelay(2000);
			copyFloatList(distances, oldDistances);
		}
	}
	
	static float[] copyFloatList(float[] list1, float[] list2) {
		for (int i=0; i < list1.length; i++ ) {
			list2[i] = list1[i]*100;
		}
		return list2;
	}


	public static void main(String[] args) {
		
		

		// Getting sensor info might seem slow but it is almost instant the first time takes time because its setting up the sensors

		
		/*
		sonar1 = new EV3UltrasonicSensor(SensorPort.S1);
		sonar2 = new NXTUltrasonicSensor(SensorPort.S2);
		sonar3 = new EV3UltrasonicSensor(SensorPort.S3);
		
		float[] distances = getAllDistances(sonar1,sonar2,sonar3);
		for (float i : distances) {
			System.out.println(i);
		}*/
		
		
		sonar1 = new EV3UltrasonicSensor(SensorPort.S1);
		sonar2 = new NXTUltrasonicSensor(SensorPort.S2);
		sonar3 = new EV3UltrasonicSensor(SensorPort.S3);
		
		LCD.drawString("Press To Start", 0, 0);
		Button.waitForAnyPress();
		mainLoop(sonar1, sonar2, sonar3);
		
		//goForward(20, defaultSpeed);
		//System.out.println("Hey");
		
		
		//turnRight(1080);
		//turnLeft(1080);
		//System.out.println(convertToDegree(10));
		

	}

}
