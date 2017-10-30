# 課題１の解答例
# x<0の範囲では0を取り、x>=0の範囲ではxそのものを返す関数をReLU関数と言う。
# ReLU関数をグラフに出力せよ。

import numpy as np
import matplotlib.pyplot as plt

def ReLU(x):
	x = np.where(x > 0, x, 0)
	return x

x = np.arange(-1,1.01,0.01)
y = ReLU(x)
plt.plot(x,y)
plt.xlim(-1, 1)
plt.ylim(-0.1, 1.5)
plt.show()