import random

indices = [i for i in range(0,10)]
seed = 44902
random.Random(seed).shuffle(indices)
print(indices)