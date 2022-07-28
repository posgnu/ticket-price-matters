import csv
import matplotlib.pyplot as plt

plt.style.use("seaborn")
import statistics
import math
import numpy as np

file = open("./data/eth2.csv")
csvreader = csv.reader(file)

header = next(csvreader)
x = [int(header[0])]
for row in csvreader:
    x.append(int(row[0]))

# Normalization
x = [math.log(e, 32) for e in x]
x = [e / sum(x) for e in x]
num_bins = 150

fig, ax = plt.subplots()

# the histogram of the data
n, bins, patches = ax.hist(x, num_bins, density=False)


# add a 'best fit' line
ax.set_xlabel("Ratio of voting power (log(resource))", fontsize=24)
ax.set_ylabel("The number of participants", fontsize=24)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)

# exp = lambda x: 10 ** (x)
# log = lambda x: np.log(x)
# ax.set_yscale("function", functions=(exp, log))

# Tweak spacing to prevent clipping of ylabel

fig.tight_layout()
fig.savefig("./results/eth2_resource_distribution.png")
# plt.show()
