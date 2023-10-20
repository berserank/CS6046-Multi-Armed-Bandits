import numpy as np
import matplotlib.pyplot as plt

n = 1000

def etc(delta, m, n = n):
    mu1 = 0
    mu2 = -1*delta
    regret = 0
    m = int(m)
    np.random.seed(10)
    arm1_exploration = np.random.normal(mu1,1,(m//2,))
    arm2_exploration = np.random.normal(mu2,1,(m//2,))

    regret += m*delta/2
    emp_mean_arm1 = 2*np.sum(arm1_exploration)/m
    emp_mean_arm2 = 2*np.sum(arm2_exploration)/m

    for i in range(m,n):
        if (emp_mean_arm1 > emp_mean_arm2):
            regret += 0
        else:
            regret += delta
    return regret

def etc_optimal(delta, n = n):
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

def ucb_bound(arm_empirical_mean, t, t1):
    return arm_empirical_mean + np.sqrt(2*np.log(t)/t1)
    
def ucb(delta, n = n):
    mu1 = 0
    mu2 = -1*delta
    regret = 0
    np.random.seed(100)
    arm1_initialisation = np.random.normal(mu1,1,(1,))[0]
    arm2_initialisation = np.random.normal(mu2,1,(1,))[0]
    regret += delta
    t1 = 1
    t2 = 1
    arm1_empirical_mean = arm1_initialisation
    arm2_empirical_mean = arm2_initialisation
    for i in range(3,n):
        arm1_ucb = ucb_bound(arm1_empirical_mean,i,t1)
        arm2_ucb = ucb_bound(arm2_empirical_mean,i,t2)
        if (arm1_ucb > arm2_ucb):
            np.random.seed(100)
            arm1_empirical_mean = (arm1_empirical_mean * t1 + np.random.normal(mu1,1,(1,))[0])/(t1+1)
            t1 += 1
        elif (arm2_ucb > arm1_ucb):
            np.random.seed(100)
            arm2_empirical_mean = (arm2_empirical_mean * t2 + np.random.normal(mu2,1,(1,))[0])/(t2+1)
            t2 += 1
            regret += delta
    return regret
        

deltas = np.linspace(1e-8,1,100)
experimental_regrets_etc_100 = []
experimental_regrets_etc_200 = []
experimental_regrets_etc_300 = []
experimental_regrets_etc_500 = []
experimental_regrets_etc_optimal = []
experimental_regrets_ucb = []

for delta in deltas:
    experimental_regret_100 = 0
    experimental_regret_200 = 0
    experimental_regret_300 = 0
    experimental_regret_500 = 0
    experimental_regret_optimal = 0
    experimental_regret_ucb = 0

    for i in range(100):
        experimental_regret_100 += etc(delta,100)/100
        experimental_regret_200 += etc(delta,200)/100
        experimental_regret_300 += etc(delta,300)/100
        experimental_regret_500 += etc(delta,500)/100
        experimental_regret_optimal += etc_optimal(delta)/100
        experimental_regret_ucb += ucb(delta)/100
    experimental_regrets_etc_100.append(experimental_regret_100)
    experimental_regrets_etc_200.append(experimental_regret_200)
    experimental_regrets_etc_300.append(experimental_regret_300)
    experimental_regrets_etc_500.append(experimental_regret_500)
    experimental_regrets_etc_optimal.append(experimental_regret_optimal)
    experimental_regrets_ucb.append(experimental_regret_ucb)


    

plt.plot(deltas, experimental_regrets_etc_100)
plt.plot(deltas, experimental_regrets_etc_200)
plt.plot(deltas, experimental_regrets_etc_300)
plt.plot(deltas, experimental_regrets_etc_500)
plt.plot(deltas, experimental_regrets_etc_optimal)
plt.plot(deltas, experimental_regrets_ucb)
plt.legend(['ETC(m = 100)', 'ETC(m = 200)', 'ETC(m = 300)', 'ETC(m = 500)','ETC(optimal)','UCB'])
plt.show()


# n = [100,200,300,400,500,600,700,800,900,1000]
# delta = 0.5
# for elem in n:
#     experimental_regret_optimal = 0
#     experimental_regret_ucb = 0
#     for i in range(100):
#         experimental_regret_optimal += etc_optimal(delta)/100
#         experimental_regret_ucb += ucb(delta)/100
#     experimental_regrets_etc_optimal.append(experimental_regret_optimal)
#     experimental_regrets_ucb.append(experimental_regret_ucb)

# plt.plot(n, experimental_regrets_etc_optimal)
# plt.plot(n, experimental_regrets_ucb)
# plt.legend(['ETC(optimal)','UCB'])
# plt.show()
    

