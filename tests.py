import numpy as np
import matplotlib.pyplot as plt
x = []
x0 = 0

h = 0.0001

y = []

N = 10000

for i in range(N):
    x.append(x0)
    y.append(round(np.sin(50*x0),3))
    x0 += h

maxy = max(y)
miny = min(y)
'''for i in range(len(y)):
    if y[i] == maxy:
        for j in range(len(y)):
            if y[j] == miny:
                for n in range(j-i):
                    if abs(y[i+1])==abs(y[j-1]):
                        print("k")'''
t = 0
maxl = 0
maxa = []
tao = 100                
for i in range(len(y)-100):
    for t in range(tao):
        if y[t] > y[t+1] and y[i]>maxl:
            maxa.append(y[i])
    t += 1
    tao += 1
print(maxa)            
plt.plot(x, y, 'y--')
plt.show()