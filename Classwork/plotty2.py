import matplotlib.pyplot as plt
import numpy as np
import random
fig, ax = plt.subplots()
width = 0.35
JanMon = random.randint(0,100)
print(JanMon)
plt.plot(JanMon,JanMon,[random.randint(0,100)],[random.randint(0,100)], [random.randint(0,100)], [random.randint(0,100)], [random.randint(0,100)], [random.randint(0,100)], [random.randint(0,100)], [random.randint(0,100)], [random.randint(0,100)], [random.randint(0,100)])
plt.ylabel('Sales')
plt.xlabel("Month")
labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
ax.set_xticklabels(labels)
ax.

plt.show()