import numpy as np
import matplotlib.pylab as plt
import perceptron
import activation_function
import newral_network

# ゲートの実行
gate = perceptron.Perceptron(0,0)

# AND  = gate.AND()
# print(AND)

# OR   = gate.OR()
# print(OR)

# NAND = gate.NAND()
# print(NAND)

# XOR  = gate.XOR()
# print(XOR)

# # 活性化関数の描写
# active = activation_function.Activation_function()
# active.step_function()
# active.sigmoid_function()
# active.relu_function()

# 3層 Newral Network の実行
x = np.array([1.0,0.5])
network = newral_network.Newral_network(x)
y = network.forward()
print(y)



