import numpy as np
import pandas as pd
import os
from collections import defaultdict
train_df = pd.read_csv("train.csv")
d = defaultdict()
for i in range(len(train_df)):
    d[train_df.iloc[i,0]+'_'+str(train_df.iloc[i,1])] = train_df.iloc[i,2]

Image_Id_ClassID = []
EncodedPixels = []
for i in os.listdir('train_images/'):
    for j in ['_1','_2','_3','_4']:
        Image_Id_ClassID.append(i+j)
        try:
            EncodedPixels.append(d[i+j])
        except:
            EncodedPixels.append(np.nan)
df = pd.DataFrame(data={'Image_Id_ClassID':Image_Id_ClassID,'EncodedPixels':EncodedPixels})
df.to_csv('train.csv',index=False)