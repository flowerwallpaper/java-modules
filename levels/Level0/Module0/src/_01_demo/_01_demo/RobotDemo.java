package _01_demo;

/*
 *    Copyright (c) The League of Amazing Programmers 2013-2020
 *    Level 0
 */

import org.jointheleague.graphical.robot.Robot;
import java.awt.Color;
import java.sql.Driver;

// This recipe draws a square using the Robot

public class RobotDemo {

	public static void demo0() {

		// This code makes a new Robot
		Robot rob = new Robot();

		// PEN. Put the robot's pen down so it can draw, Use this command:
		rob.penDown();

		// SPEED. Make the robot move quickly. Use this command:
		rob.setSpeed(100);

		for(int i = 0; i < 40; i++){
			rob.move(200);
			rob.turn(70);
		}
	}

	public static void demo1() {
		Robot rob = new Robot();
		String url = "http://icons.iconarchive.com/icons/martin-berube/character/96/Robot-icon.png";
		rob.changeRobot(url);
		rob.setSpeed(10);
		rob.penDown();
	}

	 public static void demo2() {
		Robot rob = new Robot(125, 125);
		rob.setSpeed(10);
		rob.miniaturize();
		rob.penDown();
		rob.setPenColor(Color.RED);
		rob.sleep(1000);
		int[] moves = new int[]{260, 150, 260, 150};
  
		for(int i = 0; i < moves.length; ++i) {
		   rob.turn(90);
		   rob.move(moves[i]);
		}
  
		rob.turn(90);
		rob.penUp();
		rob.move(185);
		rob.turn(-90);
		rob.setSpeed(2);
		rob.move(-75);
	 }



	public static void main(String[] args) {
		demo2();
	}
}
