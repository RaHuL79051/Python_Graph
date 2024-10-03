import seaborn as sns
import matplotlib.pyplot as plt
text = sns.load_dataset('tips')
sns.swarmplot(data=text, x='size')
plt.show()