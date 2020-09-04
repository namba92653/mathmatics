import numpy as np
from scipy.integrate import odeint
#odeintは常微分方程式を解く
import matplotlib.pyplot as plt

def func(y,x,a):
    dydx=a*x
    return dydx

#初期値
a=1
y0=1
x=np.arange(0,3,0.01)

#微分方程式
y = odeint(func, y0, x, args=(a,))

#画像表示
plt.plot(x,y,label="dydx")
plt.show()
