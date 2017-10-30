import numpy as np
import matplotlib.pylab as plt

class Activation_function:
	
	def __init__(self):
		self.x = np.arange(-5.0,5.0,0.1)

	def step_function(self):
		y = np.where(self.x > 0, 1, 0)
		plt.plot(self.x, y)
		plt.ylim(-0.1, 1.1)
		plt.title("Step Function")
		plt.show()

	def sigmoid_function(self):
		y = 1 / (1 + np.exp(-self.x))
		plt.plot(self.x, y)
		plt.ylim(-0.1, 1.1)
		plt.title("Sigmoid Function")
		plt.show()

	def relu_function(self):
		y = np.where(self.x < 0, 0, self.x)
		plt.plot(self.x, y)
		plt.ylim(-0.1, 6)
		plt.title("ReLU Function")
		plt.show()


