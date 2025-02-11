# -*- coding: utf-8 -*-
"""FoDS-A1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ufadahU5YvED83afQ6OTvMQAVgZWWvfW
"""

from scipy.special import gamma
from scipy.stats import bernoulli, beta
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

data = np.array(bernoulli.rvs(size=169,p=0.8))
fig = plt.figure()
x = np.linspace(0,1,200)

print(data)
print(np.count_nonzero(data)/len(data))

fig = plt.figure()
ax = plt.axes(ylim=(0,30))
line, = ax.plot([],[])
def init():
  line.set_data([],[])
  return line,
##make a prior distribution
a = 0.4
b = 0.6
m = 0
n = 0
mu = a/(a+b)
def animate_func(i):
  global a, b, mu, x,n,m
  sample = data[random.randint(0,len(data)-1)]
  n = n+1
  m = m+sample
  a = a+sample
  b = b+(1-sample)
  mu = a/(a+b)
  y = beta.pdf(x,a,b)
  print(max(y))
  line.set_data(x,y)
  return line,
  #print(mu,a,b)

anim = animation.FuncAnimation(fig, animate_func, init_func=init,
                               frames=300, interval=20, blit=True)
anim.save('a.gif',writer='imagemagick')
plt.show()

print(mu)

