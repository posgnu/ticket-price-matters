import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

plt.style.use("seaborn")
import math
import csv

file = open("../../data/eth2.csv")
csvreader = csv.reader(file)

header = next(csvreader)
x = [int(header[0])]
for row in csvreader:
    x.append(int(row[0]))


def get_beta(T):
    waste = [e % T for e in x]

    return sum(waste) / I


fig, ax = plt.subplots()
n, bins, patches = ax.hist(x, 150, density=False)
mode_idx = np.argmax(n)

mode_val = bins[mode_idx]

ticket_price = mode_val * (2 / 3)

R = sum(x)
I = len(x)

AN = (
    math.floor(R / ticket_price) - math.floor(I * get_beta(ticket_price) / ticket_price)
) / I

MN = max(np.array(x) // ticket_price)


print(f"AN: {AN}")
print(f"MN: {MN}")
