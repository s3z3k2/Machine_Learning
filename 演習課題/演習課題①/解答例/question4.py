# 演習問題④
# 3の倍数、5の倍数、7の倍数のベン図を考慮し、どこに分類されるかを判定するクラスを作成せよ。

# →　build.py上でクラスを呼び出して、関数を実行可能にする。
# →　__init__ で 1 以上100以下の整数をランダムで発生
# →　その数字がどこに位置するかを判定する関数をクラスの中に作成（def judge:）
# →　クラスを読み込んだ上で、build.pyでjudgeを動かして、結果をprint

import numpy as np

class POSITION:

	def __init__(self):
		self.Num = 1 + np.random.choice(range(100))
		print("選択した番号は" + str(self.Num) + "です")

	def judge(self):
		if self.Num % 105 == 0:
			print("この数字は、3の倍数かつ5の倍数かつ7の倍数です")
		elif self.Num % 35 == 0:
			print("この数字は、3の倍数ではありませんが、5の倍数かつ7の倍数です")
		elif self.Num % 21 == 0:
			print("この数字は、5の倍数ではありませんが、3の倍数かつ7の倍数です")
		elif self.Num % 15 == 0:
			print("この数字は、7の倍数ではありませんが、3の倍数かつ5の倍数です")
		elif self.Num % 3 == 0:
			print("この数字は、5と7の倍数ではありませんが、3の倍数です")
		elif self.Num % 5 == 0:
			print("この数字は、3と7の倍数ではありませんが、5の倍数です")
		elif self.Num % 7 == 0:
			print("この数字は、3と5の倍数ではありませんが、7の倍数です")
		else:
			print("この数字は、3の倍数でも5の倍数でも7の倍数でもありません")

