from random import uniform


# Animal names and IDs
species = {
	'Monkey': 0,
	'Giraffe': 1,
	'Elephant': 2
}


class Animal:
	""" Parent animal object """
	def __init__(self):
		self.health = 100.00
		self.is_dead = False
		self.name = type(self).__name__

	def tick(self):
		""" Method called every hour of simulation time """
		
		# Do not process animal's tick if its dead.
		if self.is_dead:
			return

		# Generate a random float value between 0-20 to two decimal places.
		self.health -= uniform(0, 20)

		# Check the animal's condition. I call a separate method here as they will all differ.
		self.check_condition()

	def feed(self, value):
		""" Method is called when an animal is fed. """

		if self.is_dead:
			return

		self.health += value
		
		if self.health > 100.0:
			self.health = 100.0

	def _check_condition(self):
		""" Intenal method is called to check a certain animal's condition. """
		pass

	def get_health(self):
		""" Returns the animal health as a string to two decimal places. """
		return '{0:.2f}'.format(self.health)

	def __str__(self):
		return self.name


class Monkey(Animal, object):
	def __init__(self):
		self.species = species['Monkey']
		super(Monkey, self).__init__()

	def check_condition(self):
		if self.health < 30.0:
			self.is_dead = True


class Giraffe(Animal, object):
	def __init__(self):
		self.species = species['Giraffe']
		super(Giraffe, self).__init__()

	def check_condition(self):
		if self.health < 50.0:
			self.is_dead = True


class Elephant(Animal, object):
	def __init__(self):
		self.species = species['Elephant']
		self.can_walk = True
		super(Elephant, self).__init__()

	def check_condition(self):
		if self.health < 70.0 and self.can_walk == False:
			self.is_dead = True
		elif self.health < 70.0:
			self.can_walk = False
		elif self.health >= 70.0:
			self.can_walk = True