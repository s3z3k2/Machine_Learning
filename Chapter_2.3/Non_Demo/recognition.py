import numpy as np
import PIL as Image
import sys, os
import get_data
import pickle

data = get_data.MNIST()
# MNIST画像データの取得
x_train, t_train, x_test, t_test = data.get_data()

# 取得した画像を表示
data.img_show(x_train[1])

# # 験データに対して精度の検証
# data.get_weight()
# accuracy_count = 0
# batch_size = 100

# for i in range(0, len(x_test), batch_size):
# # for i in range(len(x_test)):
# 	x_batch = x_test[i:i+batch_size]
# 	y_batch = data.predict(x_batch)
# 	# y = data.predict(x_test[i])
# 	p = np.argmax(y_batch, axis = 1)
# 	# p = np.argmax(y)

# 	# if p == t_test[i]:
# 	# 	accuracy_count += 1
# 	accuracy_count += np.sum(p == t_test[i:i+batch_size])

# print("Accuracy: " + str(float(accuracy_count) / len(x_test)))