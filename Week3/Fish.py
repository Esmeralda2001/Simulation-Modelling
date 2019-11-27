import matplotlib.pyplot as plt
import numpy as np

fish_plots = []
harvest_rates = [2e4, 5e4, 1e5, 2e5] # tons/year

def logistic_growth():
    max_growth_rate = 0.5 # per year
    carrying_capacity = 2e6

    end_time = 10 # years
    h = 0.1 # years
    num_steps = int(end_time/h)
    times = h * np.array(range(num_steps+1))

    fish = np.zeros([num_steps+1]) # tons
    fish[0] = 2e5

    for harvest_rate in harvest_rates:
        is_extinct = False
        for step in range(num_steps):
            if is_extinct:
                fish[step+1] = 0
            else:
                fish[step+1] = (fish[step] + (h * max_growth_rate) * (1-(fish[step]/carrying_capacity)) * fish[step]) - (harvest_rate * h)
                if fish[step+1] <= 0:
                    is_extinct = True
                    fish[step+1] = 0
        fish_plots.append(plt.plot(times, fish))

    return fish


def harvest():
    maximum_growth_rate = 0.5  # 1 / year
    carrying_capacity = 2e6  # tons
    maximum_harvest_rate = .7 * 2.5e5  # tons / year

    end_time = 10.  # years
    h = 0.1  # years
    num_steps = int(end_time / h)

    fish = np.zeros(num_steps + 1) # tons
    fish[0] = 2e5

    results = []

    for ramp_start in np.arange(2., 10.01, 0.5):
        for ramp_end in np.arange(ramp_start, 10.01, 0.5):
            total_harvest = 0
            is_extinct = False
            for step in range(num_steps):
                time = step * h
                harvest_factor = 0.0
                if time > ramp_end:
                    harvest_factor = 1.0
                elif time > ramp_start:
                    harvest_factor = (time - ramp_start) / (ramp_end - ramp_start)

                harvest_rate = harvest_factor * maximum_harvest_rate

                if is_extinct:
                    fish[step+1] = 0.
                    current_harvest = 0
                else:
                    current_harvest = h * harvest_rate
                    fish[step+1] = fish[step] + h * (maximum_growth_rate * (1. - fish[step] / carrying_capacity) * fish[step] - harvest_rate)
                if fish[step+1] <= 0.:
                    is_extinct = True
                total_harvest += current_harvest
            results.append([ramp_start, ramp_end, total_harvest])
    return fish, results

fish, results = harvest()

for result in results:
    plt.scatter(x=result[0], y=result[1],s=result[2] / 10000, color='b')
    plt.xlabel("Start tijd")
    plt.ylabel("Eind tijd")
plt.title(label='MSY = .7')
plt.show()


# CODE FOR LOGISTIC GROWTH
#plot1, = fish_plots[0]
#plot2, = fish_plots[1]
#plot3, = fish_plots[2]
#plot4, = fish_plots[3]

#plt.legend([harvestplot],harvest_rates)
#axes = plt.gca()
#axes.set_xlabel('Time in years')
#axes.set_ylabel('Amount of fish')

#plt.show()

