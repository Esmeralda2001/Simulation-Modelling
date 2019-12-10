import numpy
import matplotlib.pyplot

def spring_friction(h, g, x, v, step, stretch, friction):
    return (v[step] + g * h) - friction * v[step] - stretch * x[step]

def spring(h, g, x, v, step, stretch):
    return (v[step] - (g * h)) + stretch * x[step]

def falling_friction(h, g, v, step, friction):
    return (v[step] - (g * h)) + friction

def falling(h, g, v, step):
    return (v[step] - (g * h))

def forward_euler():
    h=0.1
    g=9.81
    friction = 0.1
    stretch = 4

    num_steps = 50
    t = numpy.zeros(num_steps+1)
    x = numpy.zeros(num_steps+1)
    v = numpy.zeros(num_steps+1)


    for step in range(num_steps):
        # schrijf hier code voor Euler-integratie
        t[step+1] = (step + 1) * h
        x[step + 1] = x[step] + v[step]*h
        v[step+1] = spring_friction(h, g, x, v, step, stretch, friction)
        #v[step+1] = spring(h, g, x, v, step, stretch)
        #v[step + 1] = falling_friction(h, g, v, step, friction)
        #v[step + 1] = falling(h, g, v, step)

    return t,x,v

def forward_euler_springfriction():
    h=0.1
    g=9.81
    friction = 0.1
    stretch = 4

    num_steps = 50
    t = numpy.zeros(num_steps+1)
    x = numpy.zeros(num_steps+1)
    v = numpy.zeros(num_steps+1)


    for step in range(num_steps):
        # schrijf hier code voor Euler-integratie
        t[step+1] = (step + 1) * h
        x[step + 1] = x[step] + v[step]*h
        v[step+1] = spring_friction(h, g, x, v, step, stretch, friction)

    return t,x,v



t,x,v = forward_euler()

def plot_me(t, x, v):
    axes_height = matplotlib.pyplot.subplot(211)
    matplotlib.pyplot.plot(t, x)
    axes_velocity = matplotlib.pyplot.subplot(212)
    matplotlib.pyplot.plot(t, v)
    axes_height.set_ylabel('Height in m')
    axes_velocity.set_ylabel('Velocity in m/s')
    axes_velocity.set_xlabel('Time in s')

plot_me(t, x, v)
matplotlib.pyplot.show()