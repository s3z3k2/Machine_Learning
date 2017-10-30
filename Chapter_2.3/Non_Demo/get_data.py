import numpy as np
import sys, os
from PIL import Image
import pickle

class MNIST:
	def __init__(self):
		# sampleフォルダをパスに追加
		os.chdir(os.pardir)
		path = os.getcwd() + "/Deep-Learning_sample/dataset"
		os.chdir(path)
		sys.path.append(os.pardir)
		from dataset.mnist import load_mnist

		# 訓練データと試験データの呼び出し
		(self.x_train, self.t_train), (self.x_test, self.t_test) = load_mnist(flatten=True, normalize=False)

	# 画像データのreturn
	def get_data(self):
		return self.x_train, self.t_train, self.x_test, self.t_test

	# MNIST画像データの表示
	def img_show(self,img):
		img = img.reshape(28,28)
		pil_img = Image.fromarray(np.uint8(img))
		pil_img.show()

	# 重みパラメタの取得(本来はこの”重み”も求めるべきものだが、今回は既に与えられているものとする)
	def get_weight(self):
		os.chdir(os.pardir)
		path = os.getcwd() + "/ch03"
		os.chdir(path)

		with open("sample_weight.pkl", 'rb') as f:
			self.weight = pickle.load(f)

	def sigmoid_function(self,x):
		return  1 / (1 + np.exp(-x))

	def softmax_function(self,x):
		c = np.max(x)
		return np.exp(x-c) / np.sum(np.exp(x-c))


	def predict(self,x):
		# 1層の処理
		a1 = np.dot(x, self.weight['W1']) + self.weight['b1']
		z1 = self.sigmoid_function(a1)
		# 2層の処理
		a2 = np.dot(z1, self.weight['W2']) + self.weight['b2']
		z2 = self.sigmoid_function(a2)
		# 3層の処理
		a3 = np.dot(z2, self.weight['W3']) + self.weight['b3']

		y = self.softmax_function(a3)

		return y







