import numpy
import math
import matplotlib.pyplot as plt

e = 2.71828

def forward_euler(steps):
    num_steps = steps
    x = numpy.zeros(num_steps+2)
    y = numpy.zeros(num_steps+2)
    y[0] = 1

    h = 1/num_steps

    for step in range(num_steps+1):
        x[step + 1] = (step + 1) * h
        y[step + 1] = y[step] * (1 + h)

    print("steps: ", steps, " x: ", x[-2], " y: ", y[-2], "error: ", e-y[-2])

    return x,y

#Heun implementeren is me niet gelukt.
def forward_heun(steps):
    num_steps = steps
    x = numpy.zeros(num_steps+2)
    y = numpy.zeros(num_steps+2)
    y[0] = 1

    h = 1/num_steps

    for step in range(num_steps+1):
        x[step + 1] = (step + 1) * h
        y_intermediate = y[step] + h * y[step]
        y[step + 1] = y[step] + (h/2.0) * (y[step] + y_intermediate)

    print("steps: ", steps, " x: ", x[-2], " y: ", y[-2], "error: ", e - y[-2])

    return x,y

step_sizes = [5, 10, 20]
for size in step_sizes:
    print("EULER:")
    forward_euler(size)
    print("HEUN:")
    forward_heun(size)
    print()

def plot_me():
    print("EULER:")
    x1, y1 = forward_euler(100)
    print("HEUN:")
    x2, y2 = forward_heun(100)
    plt.plot(x1, y1)
    plt.plot(x2, y2)
    plt.show()

plot_me()