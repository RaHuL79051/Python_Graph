# import matplotlib.pyplot as plt
# import numpy as np
#
# arr = np.array([1, 2, 4, 6, 7, 8])
# arr2 = np.array(['A', 'B', 'C', 'D', 'E', 'F'])
#
# plt.pie(arr, labels=arr2)
# plt.title('My Pie')
# plt.legend(title="My Legend", frameon = False)
# plt.show()
#
#

import matplotlib.pyplot as plt
categories = ['Study', 'Sleep', 'Games', 'Other Stuff']
values = [25, 35, 20, 20]

plt.pie(values, labels=categories, startangle=90, colors=['skyblue', 'lightgreen', 'coral', 'gold'])

plt.title('Rahul Saxena Graph')
plt.show()
