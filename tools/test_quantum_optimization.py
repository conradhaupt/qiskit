"""Test the cost function for different basis functions."""
import numpy as np
from quantum_optimization import cost_classical

# cost function
alpha = np.zeros(5)
alpha[4] = 1
beta = np.zeros((5, 5))
beta[0, 1] = 0.5
beta[1, 0] = 0.5
beta[0, 2] = 0.5
beta[2, 0] = 0.5
beta[1, 2] = 0.5
beta[2, 1] = 0.5
beta[1, 3] = 0.5
beta[3, 1] = 0.5
beta[2, 3] = 0.5
beta[3, 2] = 0.5

n = 5
data = {'00000': 10}
print(cost_classical(data, n, alpha, beta))
data = {'00001': 10}
print(cost_classical(data, n, alpha, beta))
data = {'00010': 10}
print(cost_classical(data, n, alpha, beta))
data = {'00011': 10}
print(cost_classical(data, n, alpha, beta))
data = {'00100': 10}
print(cost_classical(data, n, alpha, beta))
data = {'00101': 10}
print(cost_classical(data, n, alpha, beta))
data = {'00110': 10}
print(cost_classical(data, n, alpha, beta))
data = {'00111': 10}
print(cost_classical(data, n, alpha, beta))
data = {'01000': 10}
print(cost_classical(data, n, alpha, beta))
data = {'01001': 10}
print(cost_classical(data, n, alpha, beta))
data = {'01010': 10}
print(cost_classical(data, n, alpha, beta))
data = {'01011': 10}
print(cost_classical(data, n, alpha, beta))
data = {'01100': 10}
print(cost_classical(data, n, alpha, beta))
data = {'01101': 10}
print(cost_classical(data, n, alpha, beta))
data = {'01110': 10}
print(cost_classical(data, n, alpha, beta))
data = {'01111': 10}
print(cost_classical(data, n, alpha, beta))
data = {'10000': 10}
print(cost_classical(data, n, alpha, beta))
data = {'10001': 10}
print(cost_classical(data, n, alpha, beta))
data = {'10010': 10}
print(cost_classical(data, n, alpha, beta))
data = {'10011': 10}
print(cost_classical(data, n, alpha, beta))
data = {'10100': 10}
print(cost_classical(data, n, alpha, beta))
data = {'10101': 10}
print(cost_classical(data, n, alpha, beta))
data = {'10110': 10}
print(cost_classical(data, n, alpha, beta))
data = {'10111': 10}
print(cost_classical(data, n, alpha, beta))
data = {'11000': 10}
print(cost_classical(data, n, alpha, beta))
data = {'11001': 10}
print(cost_classical(data, n, alpha, beta))
data = {'11010': 10}
print(cost_classical(data, n, alpha, beta))
data = {'11011': 10}
print(cost_classical(data, n, alpha, beta))
data = {'11100': 10}
print(cost_classical(data, n, alpha, beta))
data = {'11101': 10}
print(cost_classical(data, n, alpha, beta))
data = {'11110': 10}
print(cost_classical(data, n, alpha, beta))
data = {'11111': 10}
print(cost_classical(data, n, alpha, beta))
"""
Output:

6.0
2.0
0.0
0.0
0.0
0.0
-2.0
2.0
2.0
-2.0
0.0
0.0
0.0
0.0
2.0
6.0
4.0
0.0
-2.0
-2.0
-2.0
-2.0
-4.0
0.0
0.0
-4.0
-2.0
-2.0
-2.0
-2.0
0.0
4.0"""
