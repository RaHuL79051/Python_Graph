######################################################################################################################################################################
#################################################                           Layered Plot                        ######################################################
######################################################################################################################################################################

# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.array([2017, 2018, 2019, 2020, 2021])
#
# y1 = np.array([3, 2, 5, 7, 6])
# y2 = np.array([2, 3, 4, 3, 2])
# y3 = np.array([1, 4, 2, 5, 4])
#
# plt.fill_between(x, y1, color="skyblue", label='Category A')
# plt.fill_between(x, y1 + y2, y1, color="orange, label='Category B')
# plt.fill_between(x, y1 + y2 + y3, y1 + y2, color="green", label='Category C')
#
# plt.xlabel("Year")
# plt.ylabel("Values")
# plt.title("Stacked Area Chart")
# plt.legend()
#
# plt.show()


######################################################################################################################################################################
#################################################                           Single Plot                         ######################################################
######################################################################################################################################################################


# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.array([2017, 2018, 2019, 2020, 2021])
#
# y = np.array([3, 2, 5, 7, 6])
#
# plt.fill_between(x, y, color="skyblue")
#
# plt.xlabel("Year")
# plt.ylabel("Values")
# plt.title("Simple Area Chart")
#
# plt.show()


######################################################################################################################################################################
#################################################                           Simple Plot                         ######################################################
######################################################################################################################################################################


# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.arange(1, 11)
# y = np.array([1, 3, 2, 5, 7, 4, 8, 6, 9, 10])
#
# plt.fill_between(x, y, color='skyblue')
# plt.plot(x, y, color='Slateblue', linewidth=2)
#
# plt.title('Area Chart Example')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
#
# plt.show()
