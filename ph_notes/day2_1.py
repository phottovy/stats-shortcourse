import matplotlib.pyplot as plt
import numpy as np

def get_simple_regression_samples(n,b0=-0.3,b1=0.5,error=0.2):
    trueX =  np.random.uniform(-1,1,n)
    trueT = b0 + (b1*trueX)
    return np.array([trueX]).T, trueT + np.random.normal(0,error,n)

seed = 42
n = 20
b0_true = -0.3
b1_true = 0.5
x,y = get_simple_regression_samples(n,b0=b0_true,b1=b1_true,seed=seed)

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)
ax.plot(x[:,0],y,'ko')
ax.plot(x[:,0], b0_true + x[:,0]*b1_true,color='black',label='model mean')
ax.legend()
plt.show()
