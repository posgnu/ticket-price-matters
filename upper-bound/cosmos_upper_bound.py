import csv
import matplotlib.pyplot as plt

plt.style.use("seaborn")
import numpy as np

file = open("./data/cosmos.csv")
csvreader = csv.reader(file)

x = next(csvreader)
x = [int(e) for e in x]

R = sum(x)
I = len(x)
theta_a = 1 / 4
theta_b = 1 / 3


def get_beta(T):
    waste = [e % T for e in x]

    return sum(waste) / I


T = np.linspace(1, R * 0.05, 100)
h_a = []
for t in T:
    beta = get_beta(t)
    h_a.append(((R - I * beta) * theta_a) / t * t / R)
h_b = []
for t in T:
    beta = get_beta(t)
    h_b.append(((R - I * beta) * theta_b) / t * t / R)



fig, ax = plt.subplots()  # Create a figure containing a single axes.
T = T / R

ax.plot(
    T, h_a, label="Actual resiliency bound at $\u03B8_{A}$"
)  # Plot some data on the axes.
ax.plot(
    T, h_b, label="Actual resiliency bound at $\u03B8_{B}$"
)  # Plot some data on the axes.
ax.plot(
    np.linspace(min(T), max(T), 100),
    [theta_a] * 100,
    label="Theorectical resiliency bound at $\u03B8_{A}$",
)
ax.plot(
    np.linspace(min(T), max(T), 100),
    [theta_b] * 100,
    label="Theorectical resiliency bound at $\u03B8_{B}$",
)
# ax.plot(np.linspace(min(T), max(T), 100), [1 / 5] * 100, label="Rich adversary")

ax.set_xlabel("Ratio of ticket price (T / R)",fontsize=24)  # Add an x-label to the axes.
ax.set_ylabel(
    "New resiliency bound", fontsize=24
)  # Add a y-label to the axes.
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
# ax.set_title("The minimum size of adversary")  # Add a title to the axes.
ax.legend()

# plt.show()
plt.tight_layout()
fig.savefig("./results/upper_bound_cosmos.png")
