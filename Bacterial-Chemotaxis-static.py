# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 13:14:08 2016

@author: zamanisa
"""
from __future__ import division
import math
import matplotlib.pyplot as plt
import numpy as np

tm = 1000
v = 0.025
ran = np.random.rand()
w, h = 2, tm
xofta = [[0 for x in range(w)] for y in range(h)]
xoft = np.matrix(xofta)
#xoft[0,:]=[currx,curry]
t = np.zeros(tm+1)
hl = plt.plot([], [])
fx=0
fy=0
plt.title('Bacterial Chemotaxis')
plt.xlabel('x($\mu m$)')
plt.ylabel('y($\mu m$)')
nb=500
finalx=[]
finaly=[]
for j in range(0,nb):
    currangle = ran*2*np.pi
    tumblerate = 2
    currt = 0
    currx = 0
    curry = 0
    cx = np.zeros(tm+1)
    cy = np.zeros(tm+1)
    ind = 0
    for i in range(0,tm):
        dt = -(1/tumblerate)*np.log(np.random.rand())
        dx = v*np.cos(currangle)*dt
        dy = v*np.sin(currangle)*dt
        cx[i+1]=currx
        cy[i+1]=curry
        currt = currt + dt
        currx = currx + dx
        curry = curry + dy
        t[ind]=currt
        ind = ind+1
        currangle = np.random.uniform(-1,1)*2*np.pi
        #plt.plot([cx[i],cx[i+1]],[cy[i],cy[i+1]])
    finalx.append(cx[-1])
    finaly.append(cy[-1])
    plt.plot(cx,cy)
    plt.show()
    fx=cx[-1]+fx
    fy=cy[-1]+fy
print(fx/nb,fy/nb)


