
import csv
import matplotlib.pyplot as plt
import statistics
import math

file = open("eth2.csv")
csvreader = csv.reader(file)

header = next(csvreader)
x = [int(header[0])]
for row in csvreader:
    x.append(int(row[0]))

# Normalization
x = [math.log(e, 32) for e in x]

num_bins = 150
mu = sum(x)/len(x)  # mean of distribution
sigma = statistics.stdev(x)  # standard deviation of distribution

fig, ax = plt.subplots()

# the histogram of the data
n, bins, patches = ax.hist(x, num_bins, density=True)

# add a 'best fit' line
ax.set_xlabel('Ratio of voting power (resource)')
ax.set_ylabel('The number of identity')

# Tweak spacing to prevent clipping of ylabel
fig.tight_layout()
fig.savefig("eth2_resource_distribution.png")
plt.show()

