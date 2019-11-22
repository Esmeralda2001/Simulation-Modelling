import numpy as np
import matplotlib.pyplot as plt

h = 1
population = 9.7e7
infection_chance = 0.03
average_contacts = 78
transmission_coeff = (infection_chance * average_contacts)/population #5e-9
infectious_time = 5

end_time = 60
num_steps = int(end_time/h)
times = h * np.array(range(num_steps+1))

print(0.2/(5e-9))
print(0.2/(transmission_coeff))

def seir_model(latency):
    latency_time = latency

    s = np.zeros(num_steps+1)
    e = np.zeros(num_steps + 1)
    i = np.zeros(num_steps + 1)
    r = np.zeros(num_steps + 1)

    s[0] = 9.7e7-1e6-1e5
    e[0] = 0
    i[0] = 1e5
    r[0] = 1e6

    for step in range(num_steps):
        s2e = h * transmission_coeff * s[step] * i[step]
        e2i = h / latency_time * e[step]
        i2r = h / infectious_time * i[step]

        s[step+1] = s[step] - s2e
        e[step+1] = e[step] + s2e - e2i
        i[step+1] = i[step] + e2i - i2r
        r[step+1] = r[step] + i2r

    return s, e, i, r

S, E, I, R = seir_model(1)
S1, E1, I1, R1 = seir_model(2)

print(S[-1]+E[-1]+I[-1]+R[-1])

def plot_me():
    plt.subplot(211)
    plt.plot(times, S, label='Susceptible')
    plt.plot(times, E, label='Exposed')
    plt.plot(times, I, label='Infectious')
    plt.plot(times, R, label='Recovered')
    plt.legend()

    plt.subplot(212)
    plt.plot(times, S1, label='Susceptible')
    plt.plot(times, E1, label='Exposed')
    plt.plot(times, I1, label='Infectious')
    plt.plot(times, R1, label='Recovered')
    plt.legend()

    plt.show()

plot_me()







