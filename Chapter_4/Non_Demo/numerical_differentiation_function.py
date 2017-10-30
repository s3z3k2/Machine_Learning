import numpy as np
import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D

class Diff:
	def __init__(self):
		return

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


	def numerical_gradient(self,f, X):
		if X.ndim == 1:
			return self._numerical_gradient_no_batch(f, X)
		else:
			grad = np.zeros_like(X)

		for idx, x in enumerate(X):
			grad[idx] = self._numerical_gradient_no_batch(f, x)

		return grad

	def function_1(self,x):
		return np.sum(x**2 + 2*x)

	def plot_tangent_line(self):
		x0 = np.arange(-2, 2.5, 0.25)
		x1 = np.arange(-2, 2.5, 0.25)
		X, Y = np.meshgrid(x0, x1)

		X = X.flatten()
		Y = Y.flatten()

		grad = self.numerical_gradient(self.function_1, np.array([X, Y]))

		plt.figure()
		plt.quiver(X, Y, -grad[0], -grad[1],  angles="xy",color="#666666")#,headwidth=10,scale=40,color="#444444")
		plt.xlim([-2, 2])
		plt.ylim([-2, 2])
		plt.xlabel('x0')
		plt.ylabel('x1')
		plt.grid()
		plt.legend()
		plt.draw()
		plt.show()


	def gradient_descent(self,f, init_x, lr=0.01, step_num=100):
		x = init_x

		for i in range(step_num):
			grad = self.numerical_gradient(f,x)
			x -= lr * grad

		return x