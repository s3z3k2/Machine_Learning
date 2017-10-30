# 勾配確認のサンプルコード
import sys, os
sys.path.append('../../Deep-Learning_sample/dataset')
import numpy as np
from mnist import load_mnist
import two_layer_net

# データの読み込み
(x_train , t_train) , (x_test , t_test) = \
    load_mnist(normalize=True, one_hot_label=True)

# TwoLayerNetの呼び出し
net = two_layer_net.TwoLayerNet(input_size=784, hidden_size=50,output_size=10)


# バッチ処理
x_batch = x_train[:3]
t_batch = t_train[:3]

# 誤差逆伝播法による勾配計算
grad_backprop = net.gradient(x_batch , t_batch)

# 数値微分による勾配計算
grad_numerical = net.numerical_gradient(x_batch , t_batch)

# 各重みの絶対誤差の平均を求める
for key in grad_numerical.keys():
    diff = np.average( np.abs(grad_backprop[key] - grad_numerical[key]) )
    print(key + ":" + str(diff))