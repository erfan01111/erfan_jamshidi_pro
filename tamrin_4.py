
import numpy as np
import matplotlib.pyplot as plt

n = int(input("num:"))
mean = int(input("ave:"))
std = int(input("sta:"))

def plot_normal_dist(n, mean, std):

    data = np.random.normal(mean, std, n)
    plt.hist(data, bins=100, color='green', edgecolor='black')

    plt.title('Normal distribution chart')
    plt.xlabel('amount')
    plt.ylabel('number')

    plt.show()

plot_normal_dist(1000, 0, 1)