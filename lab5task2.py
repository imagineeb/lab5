import statistics
import numpy as np
import matplotlib.pyplot as plt

x = np.repeat([0, 1, 2, 3, 4, 5, 6], [10, 10, 20, 30, 15, 10, 5])
res_std = statistics.stdev(x)

N = len(x)
sigma = 3   # Cтандартное отклонение наблюдаемых значений
k = 0.5     # Tеоретическое значение параметра k
b = 2       # Tеоретическое значение параметра b

f = np.array([k*z+b for z in range(N)])
y = f + np.random.normal(0, sigma, N)
plt.scatter(x, y, s=2, c='red')
plt.grid(True)
plt.show()

mx = x.sum()/N
my = y.sum()/N
a2 = np.dot(x.T, x)/N
a11 = np.dot(x.T, y)/N
 
kk = (a11 - mx*my)/(a2 - mx**2)
bb = my - kk*mx

ff = np.array([kk*z+bb for z in range(N)])

plt.plot(f)
plt.plot(ff, c='red')

print(x.mean(), res_std)
