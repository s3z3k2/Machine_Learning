# 日本語のエンコード（理解する必要はなし）
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 手順１の作成範囲--------------------------------------------------
import numpy as np

class TwoLayerNet:

	# 手順２の作成範囲--------------------------------------------------
	def __init__(self,input_size,hidden_size,output_size,weight_init_std=0.01):
		self.params = {}
		self.params['W1'] = weight_init_std * np.random.randn(input_size,hidden_size)
		self.params['b1'] = np.zeros(hidden_size)
		self.params['W2'] = weight_init_std * np.random.randn(hidden_size,output_size)
		self.params['b2'] = np.zeros(output_size)

	# 手順３の作成範囲--------------------------------------------------
	def get_data(self):
		from mnist import load_mnist
		(x_train, t_train),(x_test, t_test) = \
			load_mnist(normalize=True, one_hot_label=True)

		return x_train, t_train

	# 手順４の作成範囲--------------------------------------------------
	def sigmoid(self,x):
		return 1 / (1 + np.exp(-x))

	# 手順５の作成範囲--------------------------------------------------
	def softmax(self,x):
		c = np.max(x)
		return np.exp(x-c) / np.sum(np.exp(x-c))

	# 手順６の作成範囲--------------------------------------------------
	def predict(self,x):
		A = np.dot(x,self.params['W1']) + self.params['b1']
		Z = self.sigmoid(A)
		B = np.dot(Z,self.params['W2']) + self.params['b2']
		Y = self.softmax(B)

		return Y

	# 手順７の作成範囲--------------------------------------------------
	def cross_entropy_error(self, y, t):
		delta = 1e-7

		if y.ndim == 1:
			t = t.reshape(1,t.size)
			y = y.reshape(1,y.size)

		batch_size = y.shape[0]

		return -np.sum(t * np.log(y + delta)) / batch_size

	# 手順８の作成範囲--------------------------------------------------
	def loss(self, x, t):
		y = self.predict(x)

		return self.cross_entropy_error(y,t)

	# 手順９の作成範囲--------------------------------------------------
	def numerical_calculate(self,f, x):
		h = 1e-4
		grad = np.zeros_like(x)

		it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])
		while not it.finished:
			idx = it.multi_index
			tmp_val = x[idx]
			x[idx] = float(tmp_val) + h
			f_plus = f(x)

			x[idx] = float(tmp_val) - h
			f_minus = f(x)

			grad[idx] = (f_plus - f_minus) / (2*h)

			x[idx] = tmp_val
			it.iternext()

		return grad

	# 手順10の作成範囲--------------------------------------------------
	def numerical_gradient(self,x,t):
		loss_W = lambda W: self.loss(x,t)

		grads = {}
		grads['W1'] = self.numerical_calculate(loss_W,self.params['W1'])
		grads['b1'] = self.numerical_calculate(loss_W,self.params['b1'])
		grads['W2'] = self.numerical_calculate(loss_W,self.params['W2'])
		grads['b2'] = self.numerical_calculate(loss_W,self.params['b2'])

		return grads

