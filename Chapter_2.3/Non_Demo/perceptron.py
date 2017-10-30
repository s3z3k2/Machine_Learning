import numpy as np

class Perceptron:
	
	# 初期化
	def __init__(self,x1,x2):
		self.x = np.array([x1,x2])

	# ANDゲート
	def AND(self):
		w = np.array([0.5,0.5])
		b = -0.7

		tmp = np.sum(self.x * w) + b

		if tmp <= 0:
			return 0
		else:
			return 1

	# ORゲート
	def OR(self):
		w = np.array([0.5,0.5])
		b = -0.1

		tmp = np.sum(self.x * w) + b

		if tmp <= 0:
			return 0
		else:
			return 1

	# NANDゲート
	def NAND(self):
		w = np.array([-0.5,-0.5])
		b = 0.7

		tmp = np.sum(self.x * w) + b
		if tmp <= 0:
			return 0
		else:
			return 1

	# XORゲート
	def XOR(self):
		s = np.array([self.NAND(),self.OR()])
		w = np.array([0.5,0.5])
		b = -0.7

		tmp = np.sum(s * w) + b

		if tmp <= 0:
			return 0
		else:
			return 1
