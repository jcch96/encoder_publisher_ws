#!/usr/bin/env python
import rospy
import paho.mqtt.client as mqtt
from geometry_msgs.msg import Twist
from ds4_driver.msg import Status

class MqttNode():
	def __init__(self):
		rospy.init_node("mqtt_client")

		self.step = 0.01
		self.vx = 0.12
		self.wz = 0.08618

		self.linear_x = 0
		self.angular_z = 0

		self.rot_right = 0
		self.rot_left = 0

		self.vision_value = 0

		self.holo_left = 0
		self.holo_right = 0

		self.rec_r = 0
		self.rec_l = 0

		self.d_vx = 0
		self.d_wz = 0
		self.decrease = 0

		self.brush_value = 0
		self.act_value = 0
		self.vac_value = 0
		self.broker_address = "10.19.51.66"
		self.client = mqtt.Client("P1")
		self.client.connect(self.broker_address)
		rospy.Subscriber("/cmd_vel", Twist, self.cmd_sub)
		rospy.Subscriber("/status", Status, self.ds4_sub)
		self.pub = rospy.Publisher("/panthera_cmd", Twist, queue_size=1)
		self.tw = Twist()

	def cmd_sub(self, data):
		self.linear_x = data.linear.x
		self.angular_z = data.angular.z
		self.tw = data

	def ds4_sub(self, data):
		self.rot_right = data.button_dpad_right
		self.rot_left = data.button_dpad_left

		## VISION ##
		self.vision_value = data.button_dpad_up
		############
		self.holo_right = data.button_r1
		self.holo_left = data.button_l1

		self.rec_r = data.button_r2
		self.rec_l = data.button_l2

		self.d_vx = data.button_triangle# and (not data.button_share)
		self.d_wz = data.button_cross# and (not data.button_share)
		self.decrease = -data.button_share

		### Brushes roboclaw stuff
		self.brush_value = data.button_options
		self.act_value = data.button_square
		self.vac_value = data.button_circle
		###

	def run(self):
		self.change_vx()
		self.change_wz()
		msg = "{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}".format(self.linear_x, self.angular_z, self.rot_right, self.rot_left, self.vision_value,
																	self.holo_right, self.holo_left, self.rec_r, self.rec_l, self.d_vx, self.d_wz,
																	self.decrease, self.brush_value, self.act_value, self.vac_value)
		self.client.publish("cmd_vel", msg)
		#print(msg)
		self.print_instructions()

		#self.pub.publish(data)

	def change_vx(self):
		if self.d_vx == 0:
			pass
		else:
			while self.d_vx == 1:
				pass
			self.vx += (1*(not self.decrease) + self.decrease) * self.step

	def change_wz(self):
		if self.d_wz == 0:
			pass
		else:
			while self.d_wz == 1:
				pass
			self.wz += (1*(not self.decrease) + self.decrease) * self.step

	def print_instructions(self):
		print('\n')
		print("    MOVEMENT    ")
		print("    --------    ")
		print("[Left joystick]: Forward/Backwards")
		print("[Right joystick]: Left/Right")
		print("[left]: Rotate Left")
		print("[Right]: Rotate Right" + '\n')

		print("    HOLONOMIC/RECONFIGURATION MOVEMENT    ")
		print("    ----------------------------------    ")
		print("[r1] + [up]: Holonomic Right")
		print("[l1] + [up]: Holonomic Left")
		print("[r2] + [up]/[down]: Right Contract/Expand")
		print("[l2] + [down]/[up]: Left Contract/Expand" + '\n')
		print("[up] VISION mode: " + str(self.vision_value) + '\n')

		print("    ADJUST SPEED    ")
		print("    ------------    ")
		print("[Triangle/Cross]: + VX/WZ")
		print("[share] + [triangle/cross]: - VX/WZ" + '\n')

		print("    Current Velocity: ")
		print("    -----------------")
		print("VX: " + str(self.linear_x*self.vx))
		print("WZ: " + str(self.angular_z*self.wz))

		print("    Cleaning:")
		print("    ---------")
		print("[options]: Brushes -> " + str(self.brush_value))
		print("[square]: Actuators -> " + str(self.act_value))
		print("[circle]: Vacuum -> " + str(self.vac_value))

if __name__=="__main__":
	start = MqttNode()
	#start.print_instructions()
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		start.run()
		rate.sleep()