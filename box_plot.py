import seaborn as sns
import matplotlib.pyplot as plt
text = sns.load_dataset('iris')

sns.boxplot(data=text, x = 'petal_width')
plt.show()