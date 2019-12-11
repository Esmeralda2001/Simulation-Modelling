import math
import scipy.stats as st
import matplotlib.pyplot as plt
import numpy as np

def variation(arr):
    inter = np.arange(0, 1.1, step=.1)
    bins = []

    for i in range(len(inter)-1):
        new_bin = []
        for num in arr:
            if inter[i] < num and num <= inter[i+1]:
                new_bin.append(num)
        bins.append(new_bin)

    return np.array(bins)

def bin_count(bins):
    bin_counter = []
    for bini in bins:
        bin_counter.append(len(bini))
    return bin_counter


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

u1 = random_generator(5, 2000)
u2 = random_generator(15, 2000)

for i in range(len(u1)):
    values.append(math.sqrt(-2 * math.log(u1[i])) * math.sin(2*math.pi*u2[i]))
    values.append(math.sqrt(-2 * math.log(u1[i])) * math.cos(2 * math.pi * u2[i]))

bins = bin_count(variation(values))

plt.hist(values, bins=100)
plt.show()

print(st.shapiro(values))