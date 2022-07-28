import numpy as np
import matplotlib.pyplot as plt

plt.style.use("seaborn")
import math
import csv

file = open("./data/eth2.csv")
csvreader = csv.reader(file)

header = next(csvreader)
x = [int(header[0])]
for row in csvreader:
    x.append(int(row[0]))


def get_beta(T):
    waste = [e % T for e in x]

    return sum(waste) / I


R = sum(x)
T = np.linspace(1, R * 0.00001, 100)
# Normalization
# T = np.log(T)
I = len(x)

mu = []
for t in T:
    mu.append((math.floor(R / t) - math.floor(I * get_beta(t) / t)) / I)

fig, ax = plt.subplots()
T = T / R
(line1,) = ax.plot(T, mu, label="Average number of nodes")
# ax.plot(np.linspace(min(T), max(T), 100), [2] * 100, label="2")


ax.set_xlabel("Ratio of ticket price (T / R)", fontsize=24)  # Add an x-label to the axes.
ax.set_ylabel("Average number of nodes", fontsize=24)  # Add a y-label to the axes.
# ax.set_title("Average number of nodes distribution")  # Add a title to the axes.
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)

plt.tight_layout()
# plt.show()
fig.savefig("./results/average_nodes_distribution_eth2.png")
