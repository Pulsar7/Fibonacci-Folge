#
#Pulsar
#https://mein-wissen.glitch.me
#https://github.com/Pulsar7
#Python-3.8.2
#
import os
import matplotlib.pyplot as plt
import numpy as np

def draw(y_elements):
    x_elements = []
    for n in range(0,len(y_elements)):
        x_elements.append(f"f{n+1}")
    (fig, ax) = plt.subplots()
    plt.plot(x_elements,y_elements,"bo-")
    (start, end) = ax.get_ylim()
    ax.set_yticks(np.arange(0, end, 1))
    (start, end) = ax.get_xlim()
    ax.set_xticks(np.arange(0, end, 1))
    plt.grid()
    plt.show()

def show():
    fibonacci = []
    for i in range(0,7):
        if (i < 2):
            fn = 1
        else:
            fa = (fibonacci[i-1])
            fb = (fibonacci[i-2])
            fn = (fa + fb)
        fibonacci.append(int(fn))
        print(fn)
    draw(fibonacci)

if (__name__ == '__main__'):
    os.system("clear") #Linux
    show()
