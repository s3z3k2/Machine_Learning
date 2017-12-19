import numpy as np

class function:
	def __init__(self):
		pass

	def softmax(self,x):
		if x.ndim == 2:
			x = x.T
			x = x - np.max(x, axis=0)
			y = np.exp(x) / np.sum(np.exp(x), axis=0)
			return y.T

		x = x - np.max(x) # オーバーフロー対策
		return np.exp(x) / np.sum(np.exp(x))

	def cross_entropy_error(self, y, t):
		delta = 1e-7

		if y.ndim == 1:
			t = t.reshape(1,t.size)
			y = y.reshape(1,y.size)

		batch_size = y.shape[0]

		return -np.sum(t * np.log(y + delta)) / batch_size

	def sigmoid(self, x):
		return 1 / (1 + np.exp(-x))

	def ReLU(self, x):
		return np.maximum(0,x)
