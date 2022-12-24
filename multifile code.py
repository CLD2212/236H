# Import libraries

import glob
import pandas as pd
import sys
import os

#%% Set Working directory and Import all file on Percentage

os.chdir('C:/Users/cleed/Desktop/Data/Participant 01/SP/Session 1/TMS/5/Conc')

files110 = glob.glob('01_AMT 110%*.csv')
df110 = [pd.read_csv(file110, skiprows = 23) for file110 in files110]

files120 = glob.glob('01_AMT 120%*.csv')
df120 = [pd.read_csv(file120, skiprows = 23) for file120 in files120]

files130 = glob.glob('01_AMT 130%*.csv')
df130 = [pd.read_csv(file130, skiprows = 23) for file130 in files130]

files150 = glob.glob('01_AMT 150%*.csv')
df150 = [pd.read_csv(file150, skiprows = 23) for file150 in files150]

files170 = glob.glob('01_AMT 170%*.csv')
df170 = [pd.read_csv(file170, skiprows = 23) for file170 in files170]

    
#%% Concatinate all file batches into a data frame

df110 = pd.concat(df110, ignore_index=True)
df120 = pd.concat(df120, ignore_index=True)
df130 = pd.concat(df130, ignore_index=True)
df150 = pd.concat(df150, ignore_index=True)
df170 = pd.concat(df170, ignore_index=True)


