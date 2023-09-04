import numpy as np
import matplotlib.pyplot as plt

n = 1000

def etc(delta, n = n):
    mu1 = 0
    mu2 = -1*delta
    regret = 0
    m_star = (4/(delta**2))*(np.log(n*delta*delta/4))
    m = max(1,m_star)
    m = int(m)
    np.random.seed(10)
    arm1_exploration = np.random.normal(mu1,1,(m,))
    arm2_exploration = np.random.normal(mu2,1,(m,))

    regret += m*delta
    
    emp_mean_arm1 = np.sum(arm1_exploration)/m
    emp_mean_arm2 = np.sum(arm2_exploration)/m

    for i in range(2*m,n):
        if (emp_mean_arm1 > emp_mean_arm2):
            regret += 0
        else:
            regret += delta

    return regret
    
deltas = np.linspace(1e-8,1,100)
experimental_regrets = []
theoretical_regrets = []

for delta in deltas:
    x = delta + (4/delta)*np.max([ 0 , 1 + np.log(n * delta* delta/4)])
    theoretical_regrets.append(np.min([n*delta,x]))
    experimental_regret = 0
    for i in range(100):
        experimental_regret += etc(delta)/100
    experimental_regrets.append(experimental_regret)
    

plt.plot(deltas, experimental_regrets)
plt.plot(deltas, theoretical_regrets)
plt.legend(['Experimental Regret', 'Theoretical Regret'])
plt.show()


