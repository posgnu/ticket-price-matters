import csv
import matplotlib.pyplot as plt

plt.style.use("seaborn")
import statistics

file = open("./data/cosmos.csv")
csvreader = csv.reader(file)

x = next(csvreader)
x = [int(e) for e in x]
x = [e / sum(x) for e in x]


num_bins = 150

fig, ax = plt.subplots()

# the histogram of the data
n, bins, patches = ax.hist(x, num_bins, density=False)

# add a 'best fit' line
ax.set_xlabel("Ratio of voting power (resource)", fontsize=24)
ax.set_ylabel("The number of participants", fontsize=24)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)

# Tweak spacing to prevent clipping of ylabel
fig.tight_layout()
fig.savefig("./results/cosmos_resource_distribution.png")
# plt.show()
