# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 01:16:20 2020

@author: Abhay Kshirsagar
"""
import numpy as np
import matplotlib.pyplot as plt
def base_seir_model(init_vals, params, t):
    S_0, E_0, I_0, R_0 = init_vals
    S, E, I, R = [S_0], [E_0], [I_0], [R_0]
    alpha, beta, gamma = params
    dt = t[1] - t[0]
    for _ in t[1:]:
        next_S = S[-1] - (beta*S[-1]*I[-1])*dt
        next_E = E[-1] + (beta*S[-1]*I[-1] - alpha*E[-1])*dt
        next_I = I[-1] + (alpha*E[-1] - gamma*I[-1])*dt
        next_R = R[-1] + (gamma*I[-1])*dt
        S.append(next_S)
        E.append(next_E)
        I.append(next_I)
        R.append(next_R)
    return np.stack([S, E, I, R]).T , S , E, I, R

# Define parameters
t_max = 100
dt = .1
t = np.linspace(0, t_max, int(t_max/dt) + 1)
N = 10000
init_vals = 1 - 1/N, 1/N, 0, 0
alpha = 0.4
beta = 1.5
gamma = 0.6
rho = 0.7
params = alpha, beta, gamma
# Run simulation
results,S,E,I,R = base_seir_model(init_vals, params, t)

plt.ylabel("Infected people (in thousands)")
plt.xlabel("Days Passed")
#plt.plot([i for i in range(1,1002)],results,label=['Suseptible','Exposed','Infected','Recovered'])
#lt.plot(t,S,label = "Suseptible")
#plt.plot(t,E,label ="Exposed")
plt.plot(t,I,label = "Without Social Distancing")
plt.legend(loc = "upper right")
#plt.plot(t,R,label = "Recovered")

#plt.show()
def seir_model_with_soc_dist(init_vals, params, t):
    S_0, E_0, I_0, R_0 = init_vals
    S, E, I, R = [S_0], [E_0], [I_0], [R_0]
    alpha, beta, gamma, rho = params
    dt = t[1] - t[0]
    for _ in t[1:]:
        next_S = S[-1] - (rho*beta*S[-1]*I[-1])*dt
        next_E = E[-1] + (rho*beta*S[-1]*I[-1] - alpha*E[-1])*dt
        next_I = I[-1] + (alpha*E[-1] - gamma*I[-1])*dt
        next_R = R[-1] + (gamma*I[-1])*dt
        S.append(next_S)
        E.append(next_E)
        I.append(next_I)
        R.append(next_R)
    return np.stack([S, E, I, R]).T, S , E, I, R
params = alpha, beta, gamma, rho
results, S , E, I, R = seir_model_with_soc_dist(init_vals, params, t)
plt.ylabel("People in thousands")
plt.xlabel("Days Passed")
#plt.plot(t,results,label='Suseptible')
#plt.plot(t,E)
plt.plot(t,I,label = "With Social Distancing rho = 0.7")
plt.legend(loc = "upper right")
plt.savefig("SEIR.png",dpi=200)
plt.show()


