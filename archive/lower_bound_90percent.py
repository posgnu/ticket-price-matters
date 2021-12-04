import numpy as np
import matplotlib.pyplot as plt
import math

I = np.linspace(2400, 15000)
S = [24, 32]
c = 9/10

fig, ax = plt.subplots()

for i, s in enumerate(S):
    T = np.log(1 - 1 / s) / (np.log(1 - c) * I)
    ax.plot(I, T, label=f"S = {s}")
    
ax.set_xlabel("The number of identities (I)")  # Add an x-label to the axes.
ax.set_ylabel("T")  # Add a y-label to the axes.
ax.set_title(f"lower_bound_90percent")  # Add a title to the axes.
    
ax.legend()
plt.show()
fig.savefig("lower_bound_90percent.png")
