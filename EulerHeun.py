import numpy
import matplotlib.pyplot

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
def forward_heun():
    num_steps = 10
    x = numpy.zeros(num_steps+2)
    y = numpy.zeros(num_steps+2)
    y[0] = 1

    h = 1/num_steps

    for step in range(num_steps+1):
        x[step + 1] = (step + 1) * h
        y[step + 1] = y[step] + (h * ((0+x[step]) + (h+y[step]))/2)
        print(x[step], y[step])

    return x,y

forward_euler(5)
forward_euler(10)
forward_euler(20)

x,y = forward_euler(100)

def plot_me():
    matplotlib.pyplot.plot(x, y)
    matplotlib.pyplot.show()

plot_me()