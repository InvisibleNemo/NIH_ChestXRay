"""
project:      NIH Chest XRay dataset
date:         04/06/2018
developed by: Debanjan Paul
filename:     one_hot_labels.py
version:      0.1
description:  Converts csv into one hot encoded labels
dependencies: Pandas
		
"""

# Imports
import pandas as pd

# Read csv file into pandas dataframe
labels_csv = pd.read_csv("sample_labels.csv")

# Extract the set of labels in alphabetical order
label_set = labels_csv['Finding Labels'].tolist()
label_set = "|".join(labels)
label_set = list(set(labels.split("|")))

# Create columns in dataframe to store binary values
for i in label_set:
  labels_csv[i] = 0

# Get binary values
for i in range(labels_csv.shape[0]):
  for j in list(label_set):
    if(j in labels_csv.iloc[i]['Finding Labels']):
      labels_csv.loc[i,(j)] = 1

# Store one hot encoded labels in dataframe
labels_csv['one_hot'] = labels_csv[[
                                    'Atelectasis', 
                                    'Cardiomegaly',  
                                    'Consolidation',  
                                    'Edema',  
                                    'Effusion',  
                                    'Emphysema',  
                                    'Fibrosis',  
                                    'Hernia',  
                                    'Infiltration',  
                                    'Mass',  
                                    'No Finding',  
                                    'Nodule',  
                                    'Pleural_Thickening',  
                                    'Pneumonia',  
                                    'Pneumothorax']].values.tolist()

# Store one hot encoded labels in list
one_hot_labels = labels_csv[[
                             'Atelectasis', 
                             'Cardiomegaly',  
                             'Consolidation',  
                             'Edema',  
                             'Effusion',  
                             'Emphysema',  
                             'Fibrosis',  
                             'Hernia',  
                             'Infiltration',  
                             'Mass',  
                             'No Finding',  
                             'Nodule',  
                             'Pleural_Thickening',  
                             'Pneumonia',  
                             'Pneumothorax']].values.tolist()
