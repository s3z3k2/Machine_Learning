# 演習問題②
# 数字を1つ与えると、以下の操作を実行
# →　奇数なら、その数字に３を掛けて１を足す
# →　偶数なら、その数字を２で割る
# 最終的に１になるまで繰り返し。ただし、その過程の数字を全部出力する。

# →　過程を全部ファイル出力する

Num = 30
history = []

while Num != 1:
	if Num%2 == 0:
		Num = Num / 2
		history.append(str(Num) + "\n")
		print(Num)
	else:
		Num = 3 * Num + 1
		history.append(str(Num) + "\n")
		print(Num)

# ファイル作成
open('History.txt', mode = 'w+')

# ファイルへの書き込み
with open('History.txt', mode = 'a') as f:
	for i in range(len(history)):
		f.write(history[i])
f.close()