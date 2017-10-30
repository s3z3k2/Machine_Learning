# coding=utf-8
import sys, os
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris

# クラスの呼び出し
import iris_network

net = iris_network.TwoLayerNet(input_size=4, hidden_size=50, output_size=3)

# データの読み込み
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['class'] = iris.target

# 学習データと試験データに分割
df = df.take(np.random.permutation(len(df)))
df = df.reset_index(drop=True)
df_test = df[0:50]
df_train = df[50:150]

# DFをarrayに変換
t_train = df_train['class']
t_test = df_test['class']
t_train = pd.get_dummies(t_train, columns=['class'])  # one-hot表現に変換
t_test = pd.get_dummies(t_test, columns=['class'])  # one-hot表現に変換

t_train = np.array(t_train)
t_test = np.array(t_test)
del df_train['class']
del df_test['class']
x_train = np.array(df_train)
x_test = np.array(df_test)

# ハイパーパラメタの設定
iter_num = 10000
train_size = x_train.shape[0]
batch_size = 10
learning_rate = 0.1

# 各種記録用空配列の作成
train_loss_list = []
train_acc_list = []
test_acc_list = []

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
        test_acc_list.append(test_acc)
        # print(str(i) + "回目の更新時の訓練データ予測精度は" + str(train_acc * 100) + "%です")
        print(str(i) + "回目の更新時の試験データ予測精度は" + str(test_acc * 100) + "%です")
