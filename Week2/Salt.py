import numpy as np
import matplotlib.pyplot as plt


def salt_overtime(mins, out_speed=6):
    times = [0]
    values = [0]

    total_water = 1000
    total_salt = 0
    salt_concentration_in = .1
    in_speed = 6

    for i in range(mins):
        #flow in
        total_water += in_speed
        total_salt += salt_concentration_in * in_speed
        salt_concentration = total_salt/total_water

        #flow out
        total_water -= out_speed
        total_salt -= salt_concentration * out_speed
        salt_concentration = total_salt/total_water

        times.append(i)
        values.append(salt_concentration)


    return values, times


def plot_me():
    salt1, time1 = salt_overtime(1000)
    salt2, time2 = salt_overtime(1000, 5)
    plt.plot(time1, salt1, label='Outspeed= 6')
    plt.plot(time2, salt2, label='Outspeed= 5')
    plt.legend()
    plt.show()

plot_me()
