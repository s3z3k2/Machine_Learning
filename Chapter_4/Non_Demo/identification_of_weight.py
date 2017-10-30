import numpy as np
import sys,os
import TwoLayerNet

sys.path.append("../Deep-Learning_sample/dataset")
from mnist import load_mnist

# 画像の取得
(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

train_loss_list = []
train_acc_list = []
test_acc_list = []

# ハイパーパラメター
iters_num = 3
train_size = x_train.shape[0]
batch_size = 10
learning_rate = 0.1

iter_per_epoch = max(train_size/batch_size, 1)

# クラスの呼び出し
network = TwoLayerNet.TwoLayerNet(input_size = 784, hidden_size = 5, output_size = 10)

# 繰り返し学習の開始
for i in range(iters_num):
	print(str(i) + "回目")
	# ミニバッチの取得
	batch_mask = np.random.choice(train_size, batch_size)
	x_batch = x_train[batch_mask]
	t_batch = t_train[batch_mask]

	# 勾配の計算
	grads = network.caluculate_gradient(x_batch, t_batch)

	# パラメータの更新
	for key in ('W1', 'b1', 'W2', 'b2'):
		network.params[key] -= learning_rate * grads[key]

	# 学習経過の記録
	loss = network.loss(x_batch, t_batch)
	train_loss_list.append(loss)

	# 1エポックごとに認識精度を計算
	if i % iter_per_epoch == 0:
		train_acc = network.accuracy(x_train, t_train)
		test_acc = network.accuracy(x_test, t_test)
		train_acc_list.append(train_acc)
		test_acc_list.append(test_acc)
		print("train acc, test acc | " + str(train_acc) + "," + str(test_acc))
