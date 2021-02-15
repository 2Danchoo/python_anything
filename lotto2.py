import random

def lotto() :
    lotto = random.sample(range(1,46),6)
    lotto.sort()
    return lotto

print(lotto())
