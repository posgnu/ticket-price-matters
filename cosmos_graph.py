import csv
import matplotlib.pyplot as plt
import statistics

file = open("cosmos.csv")
csvreader = csv.reader(file)

x = next(csvreader)
x = [int(e) for e in x]


num_bins = 150
mu = sum(x)/len(x)  # mean of distribution
sigma = statistics.stdev(x)  # standard deviation of distribution

fig, ax = plt.subplots()

# the histogram of the data
n, bins, patches = ax.hist(x, num_bins, density=False)

# add a 'best fit' line
ax.set_xlabel('Ratio of voting power (resource)')
ax.set_ylabel('The number of identity')

# Tweak spacing to prevent clipping of ylabel
fig.tight_layout()
fig.savefig("cosmos_resource_distribution.png")
plt.show()

