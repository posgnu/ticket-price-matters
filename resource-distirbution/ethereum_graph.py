import matplotlib.pyplot as plt

plt.style.use("seaborn")

f = open("data/ethereum.csv", "r")

count = dict()
for line in f:
    count[line] = count.get(line, 0) + 1

data = []
for k in count.values():
    data.append(k)


num_bins = 150

fig, ax = plt.subplots()

# the histogram of the data
n, bins, patches = ax.hist(data, num_bins, density=False)

# add a 'best fit' line
ax.set_xlabel("Ratio of hasing power (resource)")
ax.set_ylabel("The number of identity")

# Tweak spacing to prevent clipping of ylabel
fig.tight_layout()
fig.savefig("ethereum_resource_distribution.png")
plt.show()
