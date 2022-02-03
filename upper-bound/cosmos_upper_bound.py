import csv
import matplotlib.pyplot as plt
plt.style.use('seaborn')
import numpy as np

file = open("cosmos.csv")
csvreader = csv.reader(file)

x = next(csvreader)
x = [int(e) for e in x]

R = sum(x)
I = len(x)
theta = 1/4

def get_beta(T):
    waste = [e % T for e in x]
    
    return sum(waste) / I


T = np.linspace(10000, 1000000, 100)
h = []
for t in T:
    beta = get_beta(t)
    h.append(((R - I * beta) * theta) / t * t / R)


fig, ax = plt.subplots()  # Create a figure containing a single axes.
T = T / R
ax.plot(T, h, label="The minimum size")  # Plot some data on the axes.
ax.hlines(y=theta, xmin=min(T), xmax=max(T), linewidth=1, color='r', label="Resiliency bound")
ax.hlines(y=1/5, xmin=min(T), xmax=max(T), linewidth=1, color='b', label="Rich adversary")

ax.set_xlabel("T / R")  # Add an x-label to the axes.
ax.set_ylabel("h * T / R")  # Add a y-label to the axes.
ax.set_title("The minimum size of adversary")  # Add a title to the axes.

plt.show()
fig.savefig("upper_bound_cosmos.png")