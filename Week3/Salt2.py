import numpy as np
import matplotlib.pyplot as plt


def salt_overtime(mins, out_speed=6):
    times = [0]
    values_A = [0]
    values_B = [0]

    total_water_A = 100
    total_water_B = 100

    total_salt_A = 0
    total_salt_B = 0
    salt_concentration_in = .2

    in_speed_A = 6
    in_speed_B = 3

    out_speed_A = 4
    out_speed_B = 2

    B_to_A = 1

    for i in range(mins):
        #flow in
        total_water_A += in_speed_A
        total_salt_A += salt_concentration_in * in_speed_A
        salt_concentration_A = total_salt_A/total_water_A

        #flow out
        total_water_A -= out_speed_A
        total_salt_A -= salt_concentration_A * out_speed_A
        salt_concentration_A = total_salt_A/total_water_A

        times.append(i)
        values_A.append(salt_concentration_A)

        # flow in
        total_water_B += in_speed_B
        total_salt_B += salt_concentration_in * in_speed_B
        salt_concentration_B = total_salt_B / total_water_B

        # flow out
        total_water_B -= out_speed_B
        total_salt_B -= salt_concentration_B * out_speed_B
        salt_concentration_B = total_salt_B / total_water_B

        values_B.append(salt_concentration_B)


    return values_A, values_B, times


def plot_me():
    salt1, salt2, time1 = salt_overtime(1000)
    print(len(salt1), len(salt2), len(time1))
    plt.plot(time1, salt1, label='Tank A')
    plt.plot(time1, salt2, label='Tank B')
    plt.legend()
    plt.show()

plot_me()