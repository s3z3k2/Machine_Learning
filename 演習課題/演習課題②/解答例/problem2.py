import numpy as np
# 1. y = x**2をlambdaを用いて作成せよ。
# 2. y＝[[●,◯],[●,◯],[●,◯]]を●を基準に並び替えよ。
# 	ただし、●と◯はランダムに発生される100以下の自然数とする。
# 	例：y = [[1,5],[8,2],[3,3]] →　y_sort = [[1,5],[3,3],[8,2]]
# 	また、y, y_sort をともにprint文で表示するものとする。
# 	ヒント：lambdaとmapとを組み合わせる。
# 3. 100以下の自然数のうち、3の倍数を抽出せよ。
# 	ヒント：lambdaとfilterとを組み合わせる。
# 4. 100以下の自然数３要素からなる配列をランダムに作成し、
# 	その各々の要素を２乗した配列を返すプログラムを作成せよ。
# 	例： y = [2,30,4]　→　y_sqrt = [4,900,16]
# 	ヒント：lambdaとmapを組み合わせる。

# 課題2-1の解答例
myfunc1 = lambda x: x**2
x = np.random.randint(1,101)

print(str(x) + "の2乗は" + str(myfunc1(x)) + "です")

# 課題2-2の解答例
# 下記のURL参照
# https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q10122367430
y = [[np.random.randint(1,101) for col in range(2)] for row in range(3)]
print("並び替える前の y は" + str(y) + "です")

y_sort = sorted(y, key = lambda x: x[0])
print("並び替えた後の y は" + str(y_sort) + "です")

# 課題2-3の解答例
Natural_Num = range(1,101)
Natural_Num_filtered = filter(lambda x: x % 3 == 0, Natural_Num)
print(list(Natural_Num_filtered))

# 課題2-4の解答例
rand_y = [np.random.randint(1,101) for col in range(3)]
print("2乗する前の値は" + str(rand_y) + "です")
rand_y_square = map(lambda x: x**2, rand_y)
print("2乗した後の値は" + str(list(rand_y_square)) + "です")