#%%
import os
import csv
import math
import numpy as np
import pandas as pd
from scipy.misc import central_diff_weights

#%%
path_result =  '/Users/fai/Desktop/Social-Distancing-using-YOLOv5/results'

#%%
for count,file in enumerate(os.listdir(path_result)):
    fullpath = os.path.join(path_result,file)
    df = pd.read_csv(fullpath)
    x = (df['x1'] + df['x2'])/2
    y = (df['y1'] + df['y2'])/2
    df["centroid_x"] = x
    df["centroid_y"] = y
    df['w'] = (df['x2']-df['x1'])
    df['h'] = (df['y2']-df['y1'])
    df.to_csv(fullpath, index=False)
# #%%
# %%
