PYTHON_VERSION = None
try:
	# User is running Python3
	import tkinter as tk
	import tkinter.ttk as ttk
	PYTHON_VERSION = 3
except ImportError:
	# User is running Python2
	import Tkinter as tk
	import ttk
	PYTHON_VERSION = 2

import time
from math import floor
from random import uniform
from animals import Monkey, Giraffe, Elephant, species

# How fast the game ticks in ms
ITERATION_TIME = 3000


def get_time(hours):
	days = floor(hours // 24)
	hours = hours % 24
	return 'Day {} ({}:00)'.format(days, hours)


class MainWindow:
	def __init__(self, container):
		self.container = container
		self.zoo = []

		# Generate 5 of each species
		for row in range(5):
		  self.zoo += [Monkey(), Giraffe(), Elephant()]

		# Widget text variables
		self.time = 0
		self.timer_text = tk.StringVar()

		# Load components
		self._load_components()

		# Initial tick to start the ticking recursion
		self.started = True
		self._tick()

	def feed_animals(self):
		""" A method to feed the animals. """

		# Generate 3 random values
		food = [uniform(10, 25) for _ in range(3)]

		# Feed different species different food.
		for animal in self.zoo:
			animal.feed(food[animal.species])

			self._render(animal)


	def _tick(self, forced=False):
		""" Ticks after each ITERATION_TIME (default is three seconds) """

		self.time += 1
		self.timer_text.set(get_time(self.time))

		for animal in self.zoo:
			animal.tick()
			self._render(animal)
			
		# If we don't check if a tick() was forced, it'll re-create recursion
		if not forced:
			self.container.after(ITERATION_TIME, self._tick)

	def _render(self, animal):
		""" Renders an animal's nameplate. """

		# Render different colour background depending on an animal's condition
		if animal.is_dead:
			animal.label.config(bg='red')
			status_string = 'dead' 

		elif animal.health < 70:
			animal.label.config(bg='orange')
			status_string = 'unhealthy'

		elif animal.species == species['Elephant'] and animal.can_walk == False:
			animal.label.config(bg='yellow')
			status_string = 'Can\'t Walk'

		else:
			animal.label.config(bg='lime')
			status_string = 'healthy'

		animal.stringvar.set('{}\n({}%)\n({})'
			.format(animal, animal.get_health(), status_string))

	def _load_components(self):
		""" For organisational purposes, to load all components in one method. """
		
		# Looping a dict in python 2 and 3 are slightly different, so we must account for both.
		species_list = species.items() if PYTHON_VERSION == 3 else species.iteritems()

		# Column headers
		for name, id_ in species_list:
			ttk.Label(self.container, font='helvetica 18 bold', text=name).grid(row=0, column=id_, padx=100)

		# Create all animal labels.
		row_number = 0
		for animal in self.zoo:
			# StringVar is how tkinter updates labels. We must store one for each instance of Animal
			animal.stringvar = tk.StringVar()

			# Create the label widget for the animal and place it in a grid.
			animal.label = tk.Label(self.container, textvariable=animal.stringvar, background='grey')
			animal.label.grid(row=(row_number // 3) + 1, column=animal.species, padx=100, pady=20)
			self._render(animal)

			row_number += 1

		# Our functional buttons
		ttk.Button(self.container, text='Feed', command=self.feed_animals).grid(row=7, column=0, sticky="nsew")
		ttk.Button(self.container, text='+1 hour', command=lambda: self._tick(True)).grid(row=7, column=2, sticky="nsew")

		# Current simulation time
		ttk.Label(self.container, textvariable=self.timer_text).grid(row=7, column=1)

if __name__ == '__main__':
	root = tk.Tk()
	root.resizable(False, False)
	root.title('George Beager - Zoo Simulation')

	gui = MainWindow(root)
	root.mainloop()