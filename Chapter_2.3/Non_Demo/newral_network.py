import numpy as np

# 3層Newral Network の実装
class Newral_network:

	def __init__(self,x):
		self.network = {}
		self.network['W1'] = np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]])
		self.network['b1'] = np.array([0.1,0.2,0.3])
		self.network['W2'] = np.array([[0.1,0.4],[0.2,0.5],[0.3,0.6]])
		self.network['b2'] = np.array([0.1,0.2])
		self.network['W3'] = np.array([[0.1,0.3],[0.2,0.4]])
		self.network['b3'] = np.array([0.1,0.2])

		self.x = x

	def sigmoid_function(self,x):
		return  1 / (1 + np.exp(-x))

	def identity_function(self,x):
		return x

	def softmax_function(self,x):
		c = np.max(x)
		return np.exp(x-c) / np.sum(np.exp(x-c))

	def forward(self):
		# 1層の処理
		a1 = np.dot(self.x, self.network['W1']) + self.network['b1']
		z1 = self.sigmoid_function(a1)
		# 2層の処理
		a2 = np.dot(z1, self.network['W2']) + self.network['b2']
		z2 = self.sigmoid_function(a2)
		# 3層の処理
		a3 = np.dot(z2, self.network['W3']) + self.network['b3']

		# y = self.identity_function(a3)
		y = self.softmax_function(a3)

		return y

