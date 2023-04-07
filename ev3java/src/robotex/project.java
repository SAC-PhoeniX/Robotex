package robotex;


import lejos.hardware.port.SensorPort;
import lejos.hardware.sensor.EV3UltrasonicSensor;
import lejos.hardware.sensor.NXTUltrasonicSensor;

import lejos.hardware.motor.Motor;
import lejos.utility.Delay;

public class project {
	
	static float diameter = 3.1f;
	static float pi = 3.14f;
	static float vehicleWidth = 14f;

	static EV3UltrasonicSensor sonar1;
	static NXTUltrasonicSensor sonar2;
	static EV3UltrasonicSensor sonar3;
	
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

		Motor.A.rotate(-(int) convertToDegree(turnDistance), true); //-(int) convertToDegree(vehicleWidth)
		Motor.B.rotate((int) convertToDegree(turnDistance), true);

		while (Motor.A.isMoving() || Motor.B.isMoving()) {
			Delay.msDelay(10);
		}
		
	}
	
	public static void turnLeft90(int speed) {

		float turnDistance = vehicleWidth*pi/4;
		
		Motor.A.setSpeed(speed);
		Motor.B.setSpeed(speed);

		Motor.A.rotate((int) convertToDegree(turnDistance), true); //-(int) convertToDegree(vehicleWidth)
		Motor.B.rotate(-(int) convertToDegree(turnDistance), true);

		while (Motor.A.isMoving() || Motor.B.isMoving()) {
			Delay.msDelay(10);
		}
		
	}
		
	public static void turnRight45(int speed) {

		float turnDistance = vehicleWidth*pi/2;
		Motor.A.setSpeed(speed);
		Motor.B.setSpeed(speed);

		Motor.A.rotate(-(int) convertToDegree(turnDistance), true); //-(int) convertToDegree(vehicleWidth)
		Motor.B.rotate((int) convertToDegree(turnDistance), true);

		while (Motor.A.isMoving() || Motor.B.isMoving()) {
			Delay.msDelay(10);
		}
		
	}
	
	public static void turnLeft45(int speed) {

		float turnDistance = vehicleWidth*pi/2;
		
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
		float[] distances = new float [10];
		return distances;
	}

	public static void main(String[] args) {
		
		

		// Getting sensor info might seem slow but it is almost instant the first time takes time because its setting up the sensors

		
		
		sonar1 = new EV3UltrasonicSensor(SensorPort.S1);
		sonar2 = new NXTUltrasonicSensor(SensorPort.S2);
		sonar3 = new EV3UltrasonicSensor(SensorPort.S3);
		
		float[] distances = getAllDistances(sonar1,sonar2,sonar3);
		for (float i : distances) {
			System.out.println(i);
		}
		
		//goForward(10, 1080);
		//Motor.B.rotate(90);
		//turnRight(1080);
		//turnLeft(1080);
		//System.out.println(convertToDegree(10));
		

	}

}
