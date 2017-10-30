import Layer

apple = 200
apple_num = 2
orange = 300
orange_num = 3
tax = 1.1

red_layer = Layer.Multi_Layer()
blue_layer = Layer.Multi_Layer()
green_layer = Layer.Multi_Layer()
purple_layer = Layer.Add_Layer()

orange_price = red_layer.forward(orange , orange_num)
apple_price = blue_layer.forward(apple , apple_num)
all_price = purple_layer.forward(orange_price , apple_price)
price = green_layer.forward(all_price , tax)

dprice = 1
dall_price , dtax = green_layer.backward(dprice)
dorange_price , dapple_price = purple_layer.backward(dall_price)
dapple , dapple_num = blue_layer.backward(dapple_price)
dorange , dorange_num = red_layer.backward(dorange_price)

print(price)
print(dapple_num , dapple , dorange , dorange_num , dtax)



