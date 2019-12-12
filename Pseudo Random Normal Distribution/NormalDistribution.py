import math
import scipy.stats as st
import matplotlib.pyplot as plt
import numpy as np


def random_generator(seed, amount):
    a = 314
    c = 459
    m = 100000

    sequence = []
    previous = seed

    for i in range(amount):
        new_num = ((a*previous) + c) % m
        previous = new_num
        sequence.append(new_num/m)

    return sequence


values = []

u1 = random_generator(2, 2000)
u2 = random_generator(1, 2000)

for i in range(len(u1)):
    values.append(math.sqrt(-2 * math.log(u1[i])) * math.sin(2*math.pi*u2[i]))
    values.append(math.sqrt(-2 * math.log(u1[i])) * math.cos(2*math.pi*u2[i]))

plt.hist(values, bins=100) #Bins van 100, omdat je anders minder goed de verdeling ziet
plt.show()

print(st.shapiro(values))