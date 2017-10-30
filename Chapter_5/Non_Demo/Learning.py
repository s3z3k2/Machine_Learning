# coding=utf-8
import sys, os
import numpy as np

# サンプルソースの参照
sys.path.append("../../Deep-Learning_sample/dataset")
from mnist import load_mnist

# クラスの呼び出し
import TwoLayerNet

net = TwoLayerNet.TwoLayerNet(input_size=784, hidden_size=50, output_size=10)

# データの読み込み
(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

# ハイパーパラメタの設定
iter_num = 10000
train_size = x_train.shape[0]
batch_size = 60
learning_rate = 0.1

# 各種記録用空配列の作成
train_loss_list = []
train_acc_list = []
test_acc_llist = []

# エポック数の計算
iter_per_epoch = max(train_size / batch_size, 1)

# 繰り返し処理の実行
for i in range(iter_num):
    # バッチ処理
    batch_mask = np.random.choice(train_size, batch_size)
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]

    # 誤差逆伝播法による勾配取得
    grads = net.gradient(x_batch, t_batch)

    # 重みパラメタの更新
    for key in ('W1', 'b1', 'W2', 'b2'):
        net.params[key] -= learning_rate * grads[key]

    # 損失値の計算
    loss = net.loss(x_batch, t_batch)
    train_loss_list.append(loss)

    # エポック数毎に精度計算
    if i % iter_per_epoch == 0:
        train_acc = net.accuracy(x_train, t_train)
        test_acc = net.accuracy(x_test, t_test)
        train_acc_list.append(train_acc)
        test_acc_llist.append(test_acc)
        # print(str(i) + "回目の更新時の訓練データ予測精度は" + str(train_acc * 100) + "%です")
        print(str(i) + "回目の更新時の試験データ予測精度は" + str(test_acc * 100) + "%です")
