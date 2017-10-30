# 課題３の解答例
# 自然数のリストを与えられたとき、数を並び替えて可能な最大数を返す関数を記述せよ。 
# 例えば、[50, 2, 1, 9]が与えられた時、95021が答えとなる

import numpy as np
import itertools
# 要素数の指定
Num = 4
# ランダムな自然数要素を持つ配列の作成
List = np.random.choice(range(1,100),Num)

#順列の作成
List_seq = []

for i in itertools.permutations(List):
	List_seq.append(i)

List_seq = np.array(List_seq)

# 各要素の連結
string = []
List_link = []

for i in range(len(List_seq)):

	tmp = List_seq[i]

	for k in range(len(tmp)):
		string.append(str(tmp[k]))

	string = ''.join(string)
	List_link.append(string)
	string = []

# 最大値の出力
print(max(List_link))