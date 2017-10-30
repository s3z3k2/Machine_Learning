# 日本語のエンコード（理解する必要はなし）
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 手順１１の作成範囲--------------------------------------------------
import numpy as np
import TwoLayerNet
net = TwoLayerNet.TwoLayerNet(input_size=784,hidden_size=5,output_size=10)

# 手順１２の作成範囲----------------------------------------------
sys.path.append("../Deep-Learning_sample/dataset")
x , t = net.get_data()

# 手順１３の作成範囲--------------------------------------------------
iter_num = 3
learning_rate = 0.1
batch_size = 10

# 手順１４の作成範囲--------------------------------------------------
for i in range(iter_num):

	batch_mask = np.random.choice(x.shape[0],batch_size)
	grads = net.numerical_gradient(x[batch_mask],t[batch_mask])

	# 手順１５の作成範囲----------------------------------------------
	for key in ('W1', 'b1', 'W2', 'b2'):
		net.params[key] -= learning_rate * grads[key]

	W2 = list(net.params['W2'][0])
	print(str(i) + "回目の反復です。今回のW2は " + str(W2[0]))

