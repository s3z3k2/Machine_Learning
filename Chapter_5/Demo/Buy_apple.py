import Layer

apple = 200
apple_num = 3
tax = 1.1

orange_layer = Layer.Multi_Layer()
blue_layer   = Layer.Multi_Layer()

apple_price = orange_layer.forward(apple , apple_num)
price = blue_layer.forward(apple_price , tax)

dprice = 1
dapple_price , dtax = blue_layer.backward(dprice)
dapple , dapple_num = orange_layer.backward(dapple_price)

print(dapple , dapple_num , dtax)