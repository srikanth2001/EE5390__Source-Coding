import numpy as np

x = (np.load('./mss.npy')).flatten()
p = [[0.2718549983, 0.7281450017], [0.6653328103, 0.3346671897]] # P(Y|X) matrix

y = np.zeros(len(x))
x_i = np.zeros(len(x))
for i in range(len(x)):
    y[i] = np.random.binomial(1, p[1][x[i]])
    if p[0][int(y[i])] >= p[1][int(y[i])]:
        x_i[i] = 0
    else:
        x_i[i] = 1

print("BER:", np.sum(x != x_i) / len(x))