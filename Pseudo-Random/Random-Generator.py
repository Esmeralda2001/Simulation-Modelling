import scipy as sp
import scipy.stats as st
import random
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

def average(arr):
    avg = 0
    for i in arr:
        avg += i
    avg /= (len(arr)-1)
    return(avg)

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


averages = []
for i in range(1, 100):
    gener_nums = random_generator(i, 1000)
    averages.append(average(gener_nums))
print("Smallest found average: ", min(averages), " Biggest found average: ", max(averages))


for i in range(1, 100):
    generated_nums = random_generator(i, 1000)
    binCounts = bin_count(variation(generated_nums))
    print(st.chisquare(binCounts))

print(st.chisquare([100, 100, 10, 100, 100]))
