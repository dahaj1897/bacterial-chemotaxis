#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 23:09:51 2017

@author: seyed
"""
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def data_gen(cnt=0):
    dx, dy =0, 0
    while cnt < 500:
        cnt += 1
        tumblerate = 1
        currangle = np.random.uniform(-1,1)*np.pi
        dt = -(1/tumblerate)*np.log(np.random.rand())
        dt2 = .1
        dx = .25*np.cos(currangle)*dt + dx
        dy = .25*np.sin(currangle)*dt + dy
        yield dx, dy


def init():
    ax.set_ylim(-1.1, 1.1)
    ax.set_xlim(-1, 1)
    del xdata[:]
    del ydata[:]
    line.set_data(xdata, ydata)
    return line,

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=0.75)
ax.grid()
xdata, ydata = [0], [0]
print(xdata)
plt.title('Bacterial Chemotaxis')
plt.xlabel('x($\mu m$)')
plt.ylabel('y($\mu m$)')
def run(data):
    # update the data
        dx, dy = data
        xdata.append(dx)
        ydata.append(dy)
        xmin, xmax = ax.get_xlim()
        ymin, ymax = ax.get_ylim()
        if dy >= ymax:
            ax.set_ylim(ymin, 1.5*ymax)
            ax.figure.canvas.draw()
        if dy < ymin:
            ax.set_ylim(1.5*ymin, ymax)
            ax.figure.canvas.draw()
        if dx >= xmax:
            ax.set_xlim(xmin, 1.5*xmax)
            ax.figure.canvas.draw()
        if dx < xmin:
            ax.set_xlim(1.5*xmin, xmax)
            ax.figure.canvas.draw()
        line.set_data(xdata, ydata)
        if len(xdata)==500:
            plt.plot([xdata[0],xdata[-1]],[xdata[0],ydata[-1]],'ro')
            print(dx,dy,xdata[-1],ydata[-1])
        return line

ani = animation.FuncAnimation(fig, run, data_gen, blit=False, interval=1,
                              repeat=False, init_func=init)

plt.show()