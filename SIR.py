"""
SIR disease model
S' = -beta*S*I
I' = beta*S*I - nu*I
R' = nu*I
"""

import numpy as np
from ODESOLVER import ForwardEuler
from matplotlib import pyplot as plt

class SIR:
    def __init__(self, nu, beta, S0, I0, R0):
        #nu and Beta are paramters in ODE , meaning that the S0 I0 and R0 are the inital values

        if isinstance(nu, (float, int)):
            # Is number?
            self.nu = lambda t: nu
			#for any t u put in you get the same nu out 
        elif callable(nu):
            self.nu = nu

        if isinstance(beta, (float, int)):
            self.beta = lambda t: beta 
			#for any t u put in you get the same beta out
        elif callable(beta):
            self.beta = beta

        self.initial_conditions = [S0, I0, R0]

    def __call__(self, u, t):

        S, I, R = u 

        return np.asarray([
            -self.beta(t)*S*I, # Susceptibles
            self.beta(t)*S*I - self.nu(t)*I, # Infected
            self.nu(t)*I # Recovered
        ])

if __name__ == "__main__":

	#parameters that help model the virus. beta  is the probabilty that a person gets infected, nu is the probabilty of an infected recovering, the third one is the size of the control group (population), the fourth one is the number of infected people being at the start of the simluation (DAY 0) and the last one is teh number of removed (dead) or recovered.
    #The parameters given are random for testing
    SIR = SIR(0.140, 0.285, 1500, 1, 0)
    solver = ForwardEuler(SIR)
    solver.set_initial_conditions(SIR.initial_conditions)

    time_steps = np.linspace(0, 100, 100000001)
    u, t = solver.solve(time_steps)

    plt.plot(t, u[:, 0], label="Susceptible")
    plt.plot(t, u[:, 1], label="Infected")
    plt.plot(t, u[:, 2], label="Recovered")
    plt.legend()
    plt.show()