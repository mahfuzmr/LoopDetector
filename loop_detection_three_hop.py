import pandas as pd
import numpy as np
from itertools import product
from tqdm import tqdm
def detect_connection(node_subject, node_object, max_hop ,data):
    #TODO detect two hop connection between node_subject
    connection_count = 0

    return connection_count


data = pd.read_table('/data/umls/train.txt',
                     sep = '\t', header = None)

unique_entities = np.unique(list(data[0].unique()) + list(data[2].unique()))
unique_entities_sub = list(data[0].unique())
unique_relations = list(data[1].unique())

unique_s_o_pairs = list(product(data[0].unique(), data[1].unique()))

#Create the indexes
existing_triples = {}
for triple in np.array(data):
    #mark triples which exists in the dataset
    existing_triples[triple[0], triple[1], triple[2]] = 1

data_arr = np.array(data)
#loop_candidates = [data.loc[(data[0]==data_arr[i][2])] for i in range(len(data_arr))]
already_checked_two_hop = []
already_checked_three_hop = []
two_hop_count =0
three_hop_count = 0
df = pd.DataFrame()
for entity in tqdm(unique_entities_sub):
#for triple in data_arr:
    sub = entity
    #print(already_checked_two_hop)
    #if sub not in already_checked_two_hop:
        #print('first time')

    candidate_objects = data.loc[(data[0]==sub)][2].unique()
    for sub_2 in candidate_objects:
        #print(sub)
        candidate_objects_subject_df = data.loc[(data[0]==sub_2) & (data[2]!= sub_2)]
        candidate_objects_subject_df_value = data.loc[(data[0] == sub_2) & (data[2] != sub_2)][2]

        if (len(candidate_objects_subject_df)>0) and (sub in np.array(candidate_objects_subject_df_value) ):
            continue
        #print(candidate_objects_subject_df)
        #exit()
        #unique_entity_sub_2 = np.copy(candidate_objects)
        if (sub_2 not in already_checked_three_hop):
            #candidate_objects_2 = candidate_objects_subject_df.loc[(candidate_objects_subject_df[2][2].unique()
            candidate_objects_2 = candidate_objects_subject_df[2].unique()
            #print(candidate_objects_2)
            #exit()
            #exist = set(already_checked_three_hop) - set(candidate_objects_2)
            truth_table = [candidate_objects_2[i] not in already_checked_three_hop for i in range(len(candidate_objects_2)) ]
            #if (len(candidate_objects_2)>0) and (candidate_objects_2[i] not in already_checked_three_hop):
            if (len(candidate_objects_2) > 0) and (all(truth_table)):
                #if (candidate_objects_2 not in already_checked_three_hop)
                candidate_objects_subject_df_2 = data.loc[(data[0].isin(candidate_objects_2)) & (data[2]==sub)]

                third_node_df = data.loc[(data[0]==candidate_objects_2[0]) & (data[2]==sub)]

            #print(candidate_objects_subject_df_2)
                if len(third_node_df)>0:
                    three_hop_count+=1
                    already_checked_three_hop.append(sub_2)
                    already_checked_three_hop.append(candidate_objects_2[0])
                    df = df.append(pd.DataFrame(np.array([sub,sub_2,candidate_objects_2[0]])).T)
                    #print(np.array([sub,sub_2,candidate_objects_2[0]]))
                    #rint(sub,sub_2,candidate_objects_2[0])
            #print(len(candidate_objects))
            #exit()
            #candidate_objects_as_subject = data.loc[(data[0].isin(np.unique(candidate_objects)))][2]
            #print(candidate_objects_as_subject)
            #exit()
            #print(candidate_objects_subject_df[2])
            #exit()
            #T5 2405101ODO here to implement three hop loop
            #probable_candidate = data.loc[(data[2]==sub)]#& (data[0]!=sub)
        #print('candidate triples', probable_candidate)
        #print('#################################')
        # if len(candidate_objects_subject_df)>0:
        #     #print('sub',, sub)
        #     #print('obj', candidate_objects)
        #     #print('candidate_objects subject', candidate_objects_subject)
        #     two_hop_count+=1
        #     #already_checked.append(sub)
        #     already_checked_two_hop.extend(np.array(candidate_objects_subject_df[0]))
    #exit()
#print(two_hop_count)
print(three_hop_count)
# for s_o in unique_s_s1o_pairs:
#     for triple in np.array(data):
#         try:
#             other_side_exists = existing_triples[triple[0],s_o[1],s_o[0]]
#             node_subject=triple[0]
#             node_object = data.loc[(data[0]==s_o[0]) & (data[1]==s_o[1])][2].unique()
#             print('node_subject', node_subject)
#             if len(node_object)>0:
#                 print('node_object', node_object)
#                 print('node_relation', s_o[1])
#                 probable_objects_for_s = data.loc[(data[0]==node_subject)][2].unique()
#                 print('probable_object_for_node_subject', probable_objects_for_s)
#                 #detect_connection(node_subject, node_object, probable_objects_for_s ,data)
#             print5 2405101('##########################################')
#             #TODO we need to get the distance between node_subject and node_object
#         except:
#             continue
