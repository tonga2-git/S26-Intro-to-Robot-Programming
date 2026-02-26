class Robot:
	def __init__(self, ID_Number,location, status = True):
		self.ID_Number = ID_Number
		self.location = location
		self.status = status


	def moveBot(self, new_location):
		if self.status:
			self.location = new_location
			print(f"{self.ID_Number} is now located at {self.location}.")
		else:
			print(f"{self.ID_Number} is off. Please turn on to change location.")


	def changeStatus(self):
		self.status = not self.status
		print(f"Status of {self.ID_Number}s state.")

	def __str__(self):
		return f"Robot {self.ID_Number} is at {self.location} and its status is {self.status}. "

#verification that it works as expected
robot1 = Robot(101, "A3")
print(robot1)
robot1.moveBot("B3")
print(robot1)
robot1.changeStatus()
print(robot1)
robot1.moveBot("C3")
print(robot1)
robot1.changeStatus()
print(robot1)
robot1.moveBot("C3")
print(robot1)
