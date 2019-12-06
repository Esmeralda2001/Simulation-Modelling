import scipy as sp
import scipy.stats as st
import random
import numpy as np
import math


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

def test_generator():
    for i in range(1, 101):
        generated_nums = random_generator(i, 1000)
        binCounts = bin_count(variation(generated_nums))
        print(st.chisquare(binCounts))

def approach_pi():
    C = 0

    pi_estimate = []
    smallest_num = []
    indexes_smallest = []
    for i in range(1, 100000):
        x = random_generator(i/10, 1)#random_generator(random.uniform(1, 100), 1)
        y = random_generator(i+.1/10, 1)#random_generator(random.uniform(1, 100), 1)

        if math.sqrt(x[0]**2 + y[0]**2) <= 1:
            C += 1
        pi_estimate.append(4 * C / (i + 1))

    for i in range(len(pi_estimate)):
        calc = pi_estimate[i]-math.pi
        if calc <= .000001 and calc >= -.0000001:
            indexes_smallest.append(i)
            smallest_num.append(calc)

    print(smallest_num.index(min(smallest_num)), min(smallest_num))
    print(indexes_smallest[1])
    print(pi_estimate[indexes_smallest[1]])

approach_pi()

averages = []
for i in range(1, 100):
    gener_nums = random_generator(i, 1000)
    averages.append(average(gener_nums))
print("Smallest found average: ", min(averages), " Biggest found average: ", max(averages))
