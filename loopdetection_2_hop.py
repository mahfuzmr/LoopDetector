import numpy as np
import pandas as pd
from itertools import combinations
from tqdm import tqdm

def check_existance(head_1, head_2, observed_triples_subject_object):
    try:
        observed_triples_subject_object[head_1, head_2]
        return True
    except:
        return False

data = pd.read_table('/home/mahfuz/Documents/pythonProject/RelationalShape/data/nations/train.txt',
                     header=None)
numberofentities=list(set(list(data[0].values)+list(data[2].values)))
numberofrelations=data[1].unique()
print(len(numberofentities))
print(len(numberofrelations))
print(len(data))
exit()
data.columns = ['head', 'relation', 'tail']
data_no_relation = data[['head','tail']]
data_no_relation.columns = ['head', 'tail']
unique_heads = data['head'].unique()
unique_tails = data['tail'].unique()

triples_without_relation = np.array(data_no_relation)

observed_triples_subject_object = {}
for triple in triples_without_relation:
    observed_triples_subject_object[triple[0], triple[1]]=1

heads_per_tail_df = data.groupby('tail')['head'].apply(list)

heads_per_tail_df = heads_per_tail_df.rename_axis('tail').reset_index()
heads_per_tail_df.columns = ['tail', 'heads']

already_visited = []
motiff_count = 0
for entry in tqdm(heads_per_tail_df.index):
    if len(heads_per_tail_df.loc[entry, 'heads'])>1:
        list_of_heads = heads_per_tail_df.loc[entry, 'heads']
        current_tail = heads_per_tail_df.loc[entry, 'tail']
        list_of_heads_all_combination = [",".join(map(str, comb))
                                         for comb in combinations(list_of_heads, 2)]
        for element in list_of_heads_all_combination:
            head_1, head_2 = element.split(sep=',')
            #print('head_1: ', head_1, 'head_2: ', head_2)
            #check existing connection
            if (check_existance(head_1, head_2, observed_triples_subject_object) == True) \
                    and ([head_1,head_2,current_tail] not in already_visited):
                already_visited.append([head_1, head_2, current_tail])
                motiff_count+=1
print(motiff_count)