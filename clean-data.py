# Takes a run*_data.star file. Counts contributions of each particle to a 2D class. If the same
# particle enters in 2 different classes (nodes) then a link is established between them.
# Count shows a number of connections netween two classes (nodes). 

import pandas as pd
import numpy as np
import sys


filein = sys.argv[-1]
#filein = 'run_it017_data.star'
fileout = 'clean_data'
data = pd.read_csv(filein, header = 35, sep='\s+|\t+|\n+', engine = 'python', usecols=[2,28], names=['helixID','2Dclass'])


summa = 0
helix = 0
new_helix = pd.DataFrame()
for idx in data['helixID'].index:
    if data.iloc[idx-1,0] <= data.iloc[idx,0]:
        summa = data.iloc[idx,0] + helix - 1
        new_helix = new_helix.append([summa], ignore_index=True)
    else:    
        helix = data.iloc[idx,0] + summa
        new_helix = new_helix.append([helix], ignore_index=True)


data['helixNew']= new_helix
data = data.drop(['helixID'], axis=1)


data = data.drop_duplicates().reset_index(drop=True)
data.head()


n = 1
node1 = pd.DataFrame()
node2 = pd.DataFrame()
network = pd.DataFrame()

for idx in data['helixNew'].index:
    if data.iloc[idx-1,1] == data.iloc[idx,1]:
        node1 = node1.append([data.iloc[idx,0]], ignore_index=True)
        node2 = node2.append([data.iloc[idx-1,0]],ignore_index=True )


node1.head(), node2.head()


network = pd.concat([node1, node2], axis = 1)
network.columns = ['node1','node2']
network = network.groupby(network.columns.tolist()).size().reset_index().rename(columns={0:'count'})


network.to_csv(fileout, sep='\t', index=False)

