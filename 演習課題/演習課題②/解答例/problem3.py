# 課題３の解答例
# 10000以下の素数を全て表示せよ。
prime_Num = []

for i in range(2,10000 + 1):
	judge = 0

	for k in range(2,i):
		if i%k == 0:
			judge = 1
	if judge == 0:
		prime_Num.append(i)

print(prime_Num)