# 課題４の解答例
	# 1,2,…,9の数をこの順序で、”+"、"-"、または何もせず結果が100となるあらゆる
	# 組合せを出力するプログラムを記述せよ。
	# 例えば、1 + 2 + 34 – 5 + 67 – 8 + 9 = 100となる

# 解答例①（ゴリ押し）
formula = []
result = []

def append_operator(a,b):
	if a == 0:
		b.append("+")
	elif a == 1:
		b.append("-")
	else:
		pass

	return b

for i1 in range(3):
	formula.append("1")
	append_operator(i1,formula)

	for i2 in range(3):
		formula.append("2")
		append_operator(i2,formula)
		
		for i3 in range(3):
			formula.append("3")
			append_operator(i3,formula)

			for i4 in range(3):
				formula.append("4")
				append_operator(i4,formula)

				for i5 in range(3):
					formula.append("5")
					append_operator(i5,formula)

					for i6 in range(3):
						formula.append("6")
						append_operator(i6,formula)

						for i7 in range(3):
							formula.append("7")
							append_operator(i7,formula)

							for i8 in range(3):
								formula.append("8")
								append_operator(i8,formula)
								formula.append("9")

								result_formula = ''.join(formula)

								if eval(result_formula) == 100:
									result.append(str(result_formula) + " = 100 ")

								del formula[formula.index("8"):]

								if i8 == 2:
									del formula[formula.index("7"):]
									if i7 == 2:
										del formula[formula.index("6"):]
										if i6 == 2:
											del formula[formula.index("5"):]
											if i5 == 2:
												del formula[formula.index("4"):]
												if i4 == 2:
													del formula[formula.index("3"):]
													if i3 == 2:
														del formula[formula.index("2"):]
														if i2 == 2:
															del formula[formula.index("1"):]
print("解答例①による出力結果")
for i in range(len(result)):
	print(result[i])

# 解答例②（少しスマート）
import itertools
import numpy as np

# 演算子の重複順列の作成
operator_list = ["+", "-", ""]
operator_choice = []
for i in itertools.product(operator_list, repeat=8):
	operator_choice.append(i)

operator_choice = np.array(operator_choice)

formula = []
result_formula = []

for i in range(operator_choice.shape[0]):
	for k in range(1,10):
		if k == 9:
			formula.append("9")
		else:
			formula.append(str(k))
			formula.append(operator_choice[i][k-1])

	formula = ''.join(formula)
	result = eval(formula)
	if result == 100:
		result_formula.append(str(formula) + " = 100 ")

	formula = []

print("解答例②による出力結果")
for i in range(len(result_formula)):
	print(result_formula[i])
