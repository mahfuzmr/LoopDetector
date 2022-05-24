import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

total_motiff = [566, 1039453, 19537, 41489, 2121]
#total_hit_1 = [0.98, 0.77, 0.47, 0.92, 0.47]
total_hit_10_complEX = [0.94, 0.84, 0.95, 0.99, 0.99]
data_type = ['AIDA', 'FB15k', 'WN18', 'UMLS', 'Nations']

data = np.c_[total_motiff, total_hit_10_complEX, data_type]
data_df = pd.DataFrame(data, columns=['total_motiff', 'hit@10', 'benchmark data'])
data_df['hit@10'] = data_df['hit@10'].astype(float)
data_df['total_motiff'] = data_df['total_motiff'].astype(float)
#fig, axes = plt.subplots(1, 2)

fig = plt.figure()
ax1 = fig.add_subplot(212)

g1 = sns.barplot(
    data=data_df,
    x="benchmark data", y="hit@10",
    hue='benchmark data', ax=ax1
)
g1.set(ylim=(0.80, 1.0))
ax1.get_legend().remove()
ax1.grid()
#plt.grid()
ax2 = fig.add_subplot(222)
g2 = sns.barplot(
    data=data_df,
    x="benchmark data", y="total_motiff",
    hue='benchmark data',
    ax=ax2
)
ax2.grid()
ax2.get_legend().remove()
ax3 = fig.add_subplot(221)
g3 = sns.barplot(
    data=data_df,
    x="benchmark data", y="total_motiff",
    hue='benchmark data',
    ax=ax3
)
ax3.grid()
g2.set(ylim=(0, 42000))
ax3.get_legend().remove()

handles, labels = ax3.get_legend_handles_labels()
fig.legend(handles, labels, loc='upper left')
#plt.grid()
plt.show()