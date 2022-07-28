import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

plt.style.use("seaborn")
import math


def get_beta(T):
    waste = [e % T for e in x]

    return sum(waste) / I


f = open("../../data/bitcoin.csv", "r")

count = dict()
for line in f:
    count[line] = count.get(line, 0) + 1

raw_data = []
for k in count.values():
    raw_data.append(k)
x = raw_data

fig, ax = plt.subplots()
n, bins, patches = ax.hist(x, 150, density=False)
mode_idx = np.argmax(n)

mode_val = (bins[mode_idx] + bins[mode_idx + 1]) / float(2)


ticket_price = mode_val * (2 / 3)

R = sum(x)
I = len(x)

AN = (
    math.floor(R / ticket_price) - math.floor(I * get_beta(ticket_price) / ticket_price)
) / I

MN = max(np.array(x) // ticket_price)


print(f"AN: {AN}")
print(f"MN: {MN}")
