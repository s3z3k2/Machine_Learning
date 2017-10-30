# 課題４の解答例
# フィボナッチ数列を作成し、2**30以下の値までをファイル出力せよ。
def Fibonacci(a,b):
	return a + b

Fibonacci_sequence = [1,1]
last_Num = 0

while last_Num < 2**30:
	Num = len(Fibonacci_sequence)
	last_Num = Fibonacci(Fibonacci_sequence[Num-1], Fibonacci_sequence[Num-2])
	Fibonacci_sequence.append(last_Num)

print(Fibonacci_sequence)