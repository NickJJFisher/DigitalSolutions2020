import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import random

labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
men_means = [random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100)]

x = np.arange(len(labels))  # the label locations
width = 0.15  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width, men_means)


# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Percentage Profits')
ax.set_title('Profits a month')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()




fig.tight_layout()

plt.show()