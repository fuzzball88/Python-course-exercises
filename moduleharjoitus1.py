import random

for i in range(0,5):
    coin = random.randint(0,1)
    if coin == 0:
            coin = "Tails!"
            print(coin)
    else:
            coin = "Heads!"
            print(coin)
