# 課題４の解答例
# ElCentro.txtを読み込み、グラフとして出力せよ。

import matplotlib.pylab as plt
import numpy as np

acc = np.loadtxt('El Centro.txt')
time = np.loadtxt('time.txt')

plt.plot(time,acc)
plt.show()
