import sys, os 
import numpy as np

class TwoLayerNet:

	def __init__(self, input_size, hidden_size, output_size, weight_init_std = 0.01):
		# 重みの初期化
		self.params = {}
		self.params['W1'] = weight_init_std * np.random.randn(input_size , hidden_size)
		self.params['b1'] = np.zeros(hidden_size)
		self.params['W2'] = weight_init_std * np.random.randn(hidden_size , output_size)
		self.params['b2'] = np.zeros(output_size)

	def sigmoid(self, x):
		return 1 / (1 + np.exp(-x))

	def softmax(self, x):
		c = np.max(x)
		return np.exp(x-c) / np.sum(np.exp(x-c))

	def predict(self, x):
		W1 = self.params['W1']
		W2 = self.params['W2']
		b1 = self.params['b1']
		b2 = self.params['b2']

		a1 = np.dot(x,W1) + b1
		z1 = self.sigmoid(a1)
		a2 = np.dot(z1,W2) + b2
		y  = self.softmax(a2)

		return y

	def cross_entropy_error(self, y, t):
		delta = 1e-7

		if y.ndim == 1:
			t = t.reshape(1,t.size)
			y = y.reshape(1,y.size)

		batch_size = y.shape[0]

		return -np.sum(t * np.log(y + delta)) / batch_size

	def loss(self, x, t):
		y = self.predict(x)

		return self.cross_entropy_error(y,t)

	def accuracy(self, x, t):
		y = self.predict(x)
		y = np.argmax(y, axis=1)
		t = np.argmax(t, axis=1)

		accuracy = np.sum(y == t) / float(x.shape[0])
		return accuracy

	def numerical_gradient(self,f, X):
		if X.ndim == 1:
			return self._numerical_gradient_no_batch(f, X)
		else:
			grad = np.zeros_like(X)

		for idx, x in enumerate(X):
			grad[idx] = self._numerical_gradient_no_batch(f, x)

		return grad

	def _numerical_gradient_no_batch(self,f, x):
		h = 1e-4 # 0.0001
		grad = np.zeros_like(x)

		for idx in range(x.size):
			tmp_val = x[idx]
			x[idx] = float(tmp_val) + h
			fxh1 = f(x) # f(x+h)

			x[idx] = tmp_val - h 
			fxh2 = f(x) # f(x-h)
			grad[idx] = (fxh1 - fxh2) / (2*h)

			x[idx] = tmp_val # 値を元に戻す

		return grad

	def caluculate_gradient(self, x, t):
		loss_W = lambda W: self.loss(x, t)

		grads = {}
		grads['W1'] = self.numerical_gradient(loss_W, self.params['W1'])
		grads['b1'] = self.numerical_gradient(loss_W, self.params['b1'])
		grads['W2'] = self.numerical_gradient(loss_W, self.params['W2'])
		grads['b2'] = self.numerical_gradient(loss_W, self.params['b2'])

		return grads
