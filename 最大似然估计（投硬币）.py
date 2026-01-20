import numpy as np
import matplotlib.pyplot as plt
import math

N = 10000
p = 0.6
coin_tosses = np.random.binomial(1, p, N)
print(coin_tosses)

n_heads = np.sum(coin_tosses)
n_tails = N - n_heads
print(n_heads, n_tails) 

def log_likelihood_function(p):
    if p <=0 or p >=1:
        return -np.inf
    return n_heads * np.log(p) + n_tails * np.log(1-p)

p_values = np.linspace(0.01,0.99,100)
log_likelihood_values = [log_likelihood_function(p) for p in p_values]
mle = np.argmax(log_likelihood_values)
print(f"MLE: {p_values[mle]}")
plt.plot(p_values,log_likelihood_values)
plt.xlabel("p")
plt.ylabel("log likelihood")
plt.title("Log Likelihood Function")
plt.show()
