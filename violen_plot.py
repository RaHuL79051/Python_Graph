import seaborn as sns
import matplotlib.pyplot as plt

text = sns.load_dataset('tips')

colors = ['Red', 'Green', 'Blue', 'Orange', 'Yellow']
sns.set_theme(style="whitegrid")
sns.violinplot( x='day', y='tip', hue="time", data=text, color='Yellow', cut=0)
plt.show()