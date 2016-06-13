#!/usr/bin/python3


from __future__ import division
import random
import matplotlib.pyplot as plt
plt.style.use('ggplot') # makes graphs pretty

# initialisation 
MAX_TIME = 1000
t = 0               # initial time
N = 100.0           # population size
A = 50              # initial proportion of believers A
B = N-A             # initial proportion of believers B

"""
!!!!!!!!!!!
Q: should we keep 'attractiveness' normalised? I don't think it matters too much 
cause we take a relative value anyways so it's more a question of 'do we want to make it pretty, pretty' 
it may be an overkill - it's gonna add an unnecessary line of code. 

!!!!!!!!!!!
"""
Ta = 1.0            # initial attractiveness of option A
Tb = 1.1            # initial attractiveness of option B
alpha = 0.1         # strength of the transmission process
believersA = [A]    # the first value is equal to the initialisation value (defined above)
believersB = [B]

    
def transmission(believers, Tx,Ty):
    """ transmission is the rate of 'conversion' of believers from one option (religion) to another.
        It depends on the current proportion between believers in the populaiton (no_adopters).
        And it's attractiveness to believers (defined in the 'attractiveness' function).
    """
    no_adopters = (believers / N) 
    attraction = (Tx - Ty) / (Ty + Tx)
    return no_adopters * attraction

def attractiveness(Ta, Tb):
    """ attractiveness is a dynamically changing feature of each cultural soption. 
    The function is composed of the current value for each option (Ta_now, Tb_now)
    and a small stochastic change defined by the function K
    """
    Ka = 0          # steady state traits
    Kb = 0
    
    Ta = Ta + Ka
    Tb = Tb + Kb
    return Ta, Tb
    

while t < MAX_TIME: 
    """ Main loop. Repeat until stop condition is met.
    1. define the current attractiveness of each option 
    2. define proportion of population swithching from B to A and vice versa
    3. calculate current numbers of practicioners of each option
    4. output the numbers to two lists for plotting    
    
    """
   
    print('next step:',t)

    # define the current attractiveness of each option
    Ta_now, Tb_now = attractiveness(Ta, Tb)  
    
    # calculate the change between believers A and B in the current time step       
    changeBA = alpha * transmission(A, Ta_now, Tb_now) * B       
    changeAB = alpha * transmission(B, Tb_now, Ta_now) * A    

    # update the population    
    A = A + changeBA 
    B = B + changeAB

    
    # save the values to a list for plotting    
    believersA.append(A)
    believersB.append(B)
        
    # time = time + 1        
    t+=1 
    
# plot the results    
plt.plot(believersA)
plt.plot(believersB) 
plt.show()
