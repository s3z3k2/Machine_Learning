import numpy as np

x1 = 1
x2 = 1

w1 = 0.5
w2 = 0.5
b = -0.2


a = (x1 * w1) + (x2 * w2) + b

if a > 0:
	y = 1
else:
	y = 0

print(y)