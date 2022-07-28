import matplotlib.pyplot as plt

plt.style.use("seaborn")

f = open("./data/bitcoin.csv", "r")

count = dict()
for line in f:
    count[line] = count.get(line, 0) + 1

raw_data = []
for k in count.values():
    raw_data.append(k)
data = [x / sum(raw_data) for x in raw_data]

top5 = sorted(count.items(), key=lambda item: item[1], reverse=True)[:5]
# print(top5)
label = ["AntPool", "F2Pool", "ViaBTC", "Unknown", "Unknown"]
num_bins = 150

fig, ax = plt.subplots()

# the histogram of the data
n, bins, patches = ax.hist(data, num_bins, density=False)

# add a 'best fit' line
ax.set_xlabel("Ratio of hashing power (resource)", fontsize=24)
ax.set_ylabel("The number of participants", fontsize=24)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)

# Tweak spacing to prevent clipping of ylabel
fig.tight_layout()
fig.savefig("./results/bitocin_resource_distribution.png")
# plt.show()
