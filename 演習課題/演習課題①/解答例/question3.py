# 演習問題③
# 2つの引数を与えたら、その数の最大公約数を求める。（ユークリッドの互除法を使って）

def divisor(a,b):
	# 引数の大小関係に応じて変数の割り当て
	if a > b:
		BigNum = a
		SmallNum = b
	else:
		SmallNum = a
		BigNum = b

	# 余りの初期値を設定
	rest = 100

	# 余りが0になるまで徐算の実行
	while rest != 0:
		# 余りの計算
		rest = BigNum % SmallNum
		# 割り切れた場合はSmallNumを返す
		if rest == 0:
			return SmallNum

		# SmallNUmをBigNumに
		BigNum = SmallNum
		# 余りをSmallNumに
		SmallNum = rest

