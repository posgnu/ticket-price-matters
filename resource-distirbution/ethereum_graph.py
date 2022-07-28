import matplotlib.pyplot as plt
import numpy as np

plt.style.use("seaborn")

f = open("./data/ethereum.csv", "r")

count = dict()
for line in f:
    count[line] = count.get(line, 0) + 1

raw_data = []
for k in count.values():
    raw_data.append(k)
data = [x / sum(raw_data) for x in raw_data]


top5 = sorted(count.items(), key=lambda item: item[1], reverse=True)[:5]

num_bins = 150

fig, ax = plt.subplots()


# the histogram of the data
n, bins, patches = ax.hist(data, num_bins, density=False)

# label
label = ["Ethermine", "f2pool2", "Hiveon Pool", "Spark Pool", "Nanopool"]
"""
for ((k, v), label_text) in zip(top5, label):
    x = v / sum(raw_data)
    y = -1
    ax.text(
        x,
        y,
        label_text,
        fontsize=5,
        horizontalalignment="center",
        verticalalignment="center",
    )
"""

# add a 'best fit' line
# mu = np.mean(data)
# sigma = np.std(data)
# y = (1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * (1 / sigma * (bins - mu)) ** 2)
# ax.plot(bins, y, "--")

# add a 'best fit' line
ax.set_xlabel("Ratio of hashing power (resource)", fontsize=24)
ax.set_ylabel("The number of participants", fontsize=24)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)

# exp = lambda x: 10 ** (x)
# log = lambda x: np.log(x)
# ax.set_yscale("function", functions=(exp, log))

# Tweak spacing to prevent clipping of ylabel
fig.tight_layout()
fig.savefig("./results/ethereum_resource_distribution.png")
# plt.show()
