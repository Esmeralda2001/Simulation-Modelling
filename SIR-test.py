import numpy as np
import matplotlib.pyplot

h = 1
population = 9.7e8
infection_chance = 0.03
average_contacts = 78
transmission_coeff = (infection_chance * average_contacts)/population #5e-9
latency_time = 1
infectious_time = 5

end_time = 60
num_steps = int(end_time/h)
times = h * np.array(range(num_steps+1))

def seir_model():

    s = np.zeros(num_steps+1)
    e = np.zeros(num_steps + 1)
    i = np.zeros(num_steps + 1)
    r = np.zeros(num_steps + 1)

    s[0] = 9.7e8-1e7-1e6
    e[0] = 0
    i[0] = 1e6
    r[0] = 1e7

    for step in range(num_steps):
        s2e = h * transmission_coeff * s[step] * i[step]
        e2i = h / latency_time * e[step]
        i2r = h / infectious_time * i[step]

        s[step+1] = s[step] - s2e
        e[step+1] = e[step] + s2e - e2i
        i[step+1] = i[step] + e2i - i2r
        r[step+1] = r[step] + i2r

    return s, e, i, r

S, E, I, R = seir_model()

print(S[-1]+E[-1]+I[-1]+R[-1])

def plot_me():
    axes_sus = matplotlib.pyplot.subplot(311)
    matplotlib.pyplot.plot(times, S)
    axes_infected = matplotlib.pyplot.subplot(312)
    matplotlib.pyplot.plot(times, I)
    axes_recovered = matplotlib.pyplot.subplot(313)
    matplotlib.pyplot.plot(times, R)
    axes_recovered.set_ylabel('Recovered people')
    axes_sus.set_ylabel('Susceptible people')
    axes_infected.set_ylabel('Infected people')
    axes_infected.set_xlabel('Time in days')
    matplotlib.pyplot.show()

plot_me()