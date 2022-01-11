import matplotlib
import numpy as np
from matplotlib import pyplot as plt
from random import *
import scipy
from scipy.stats import bernoulli

for i in range(0,50):
    print(bernoulli.ppf(0.04,p,packet))
    p2.insert(i,Bernoulli(p,packet))
    d2.insert(i,10-p2[i])

    plt.plot(p2[i],d2[i])

    p = p + 0.04
    d = 1 - p

x = 0

print("The average number of busy outputs vs p: ")

j = 0.04
while j < 0.96:
    x += 1
    print(round(j,2), "-", round(j+0.04,2), ":")

    for x in range(0,p2[x],1):
        print("*")

    x = 0

    print("The average number of dropped packets versus p: ")

    i = 0.04
    while i < 0.96:
        x += 1
        counter = 1;

        print("\n",round(i,2),"-",round(i+0.04,2), ":")
        for k in range(0,d2[x]):
            counter +=1
        #plt.plot(i,counter)
        i += 0.04
    j += 0.04

random = randint(0,1)
a, b = 0.2, 0.8
rv = bernoulli(a,b)

