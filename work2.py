import matplotlib.pyplot as plt
from pylab import plot
import numpy as np
x=[[3,3],[4,3],[1,1],[2,4]]
y=[1,1,-1,-1]
w=[0,0]
b=0
alpha=1
sign=0
def sgn(x):
    if x>0:
        return 1
    else:
        return -1
while sign==0:
    sign=1
    for i in range(0,len(x)):
        while (sgn(np.dot(w,x[i])+b)!=y[i]):
            w[0]=w[0]+alpha*y[i]*x[i][0]
            w[1]=w[1]+alpha*y[i]*x[i][1]
            b=b+alpha*y[i]
            sign=0
print(w)
print(b)
ascent=-w[0]/w[1]
intercept=-b/w[1]
x=np.linspace(0,5,50)
y=ascent*x+intercept
plt.axis([0,5,0,5])
plt.scatter(1,1,color='red',marker='x')
plt.scatter(2,4,color='red',marker='x')
plt.scatter(3,3,color='blue',marker='o')
plt.scatter(4,3,color='blue',marker='o')
plt.plot(x,y)
plt.show()