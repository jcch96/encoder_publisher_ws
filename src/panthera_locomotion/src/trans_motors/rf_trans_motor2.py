#!/usr/bin/env python

import rospy
import math
import orienbus
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32
import serial.tools.list_ports
from trans_class import TransMotor

if __name__ == "__main__":
	try:
		rospy.init_node('rf_trans_motor')
		rf_motor = TransMotor('rf', 1, -1) # init translational motors TransMotor(name, address, sign). sign is for each motor either +1 or -1
		#rate = rospy.Rate(1)
		while not rospy.is_shutdown():
			# subscribes to both /panthera_cmd & /reconfig
			if rf_motor.wheel_speed == 0:
				# if /reconfig publishes 0 speed, read from /panthera_cmd
				rf_motor.adjust_speed(rf_motor.linear_x, rf_motor.angular_z)
			else:
				# if /panthera_cmd publishes 0 speed, read from /reconfig
				rf_motor.motor.writeSpeed(rf_motor.wheel_speed)
			rf_motor.pub_wheel_vel()
	except rospy.ROSInterruptException:
		pass

