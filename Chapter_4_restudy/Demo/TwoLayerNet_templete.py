# 日本語のエンコード（理解する必要はなし）
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 手順１の作成範囲--------------------------------------------------


	# 手順２の作成範囲--------------------------------------------------
	def
		self.params = {}


	# 手順３の作成範囲--------------------------------------------------
	def



		return 

	# 手順４の作成範囲--------------------------------------------------
	def
		return 

	# 手順５の作成範囲--------------------------------------------------
	def

		return 

	# 手順６の作成範囲--------------------------------------------------
	def 

		return 

	# 手順７の作成範囲--------------------------------------------------
	def
		delta = 1e-7

		if y.ndim == 1:
			t = t.reshape(1,t.size)
			y = y.reshape(1,y.size)

		batch_size = y.shape[0]

		return 

	# 手順８の作成範囲--------------------------------------------------
	def

		return 

	# 手順９の作成範囲--------------------------------------------------
	def
		h = 1e-4
		grad = np.zeros_like(x)

		it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])
		while not it.finished:
			idx = it.multi_index
			tmp_val = x[idx]
			# 前方差分の計算

			# 後方差分の計算

			# 微分係数の計算

			x[idx] = tmp_val
			it.iternext()

		return 

	# 手順10の作成範囲--------------------------------------------------
	def
		# 関数をlambdaで定義

		grads = {}


		return 

