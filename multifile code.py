# Import libraries

import glob
import pandas as pd
import numpy as np
import scipy as sp
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

#%% Get the Data we Need

df110 = df110[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df120 = df120[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df130 = df130[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df150 = df150[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df170 = df170[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]

#%% Account for EMG Offset

df110['BF EMG (Offset)'] = df110['BF EMG (Trigger)'] - np.mean(df110['BF EMG (Trigger)'])
df110['MH EMG (Offset)'] = df110['MH EMG (Trigger)'] - np.mean(df110['MH EMG (Trigger)'])
df120['BF EMG (Offset)'] = df120['BF EMG (Trigger)'] - np.mean(df120['BF EMG (Trigger)'])
df120['MH EMG (Offset)'] = df120['MH EMG (Trigger)'] - np.mean(df120['MH EMG (Trigger)'])
df130['BF EMG (Offset)'] = df130['BF EMG (Trigger)'] - np.mean(df130['BF EMG (Trigger)'])
df130['MH EMG (Offset)'] = df130['MH EMG (Trigger)'] - np.mean(df130['MH EMG (Trigger)'])
df150['BF EMG (Offset)'] = df150['BF EMG (Trigger)'] - np.mean(df150['BF EMG (Trigger)'])
df150['MH EMG (Offset)'] = df150['MH EMG (Trigger)'] - np.mean(df150['MH EMG (Trigger)'])
df170['BF EMG (Offset)'] = df170['BF EMG (Trigger)'] - np.mean(df170['BF EMG (Trigger)'])
df170['MH EMG (Offset)'] = df170['MH EMG (Trigger)'] - np.mean(df170['MH EMG (Trigger)'])

#%% Build and Apply Filter

high = 13/(1000/2)
low = 500/(1000/2)
b, a = sp.signal.butter(4, [high,low], btype='bandpass', analog=True)

BF_filtered = sp.signal.filtfilt(b, a, df110['BF EMG (Offset)'])
MH_filtered = sp.signal.filtfilt(b, a, df110['MH EMG (Offset)'])
df110['BF Filtered'] = BF_filtered
df110['MH Filtered'] = MH_filtered

BF_filtered = sp.signal.filtfilt(b, a, df120['BF EMG (Offset)'])
MH_filtered = sp.signal.filtfilt(b, a, df120['MH EMG (Offset)'])
df120['BF Filtered'] = BF_filtered
df120['MH Filtered'] = MH_filtered

BF_filtered = sp.signal.filtfilt(b, a, df130['BF EMG (Offset)'])
MH_filtered = sp.signal.filtfilt(b, a, df130['MH EMG (Offset)'])
df130['BF Filtered'] = BF_filtered
df130['MH Filtered'] = MH_filtered

BF_filtered = sp.signal.filtfilt(b, a, df150['BF EMG (Offset)'])
MH_filtered = sp.signal.filtfilt(b, a, df150['MH EMG (Offset)'])
df150['BF Filtered'] = BF_filtered
df150['MH Filtered'] = MH_filtered

BF_filtered = sp.signal.filtfilt(b, a, df170['BF EMG (Offset)'])
MH_filtered = sp.signal.filtfilt(b, a, df170['MH EMG (Offset)'])
df170['BF Filtered'] = BF_filtered
df170['MH Filtered'] = MH_filtered

#%% Descriptiors

des110 = df110.describe()
des120 = df120.describe()
des130 = df130.describe()
des150 = df150.describe()
des170 = df170.describe()

alldes = ([['110', des110], ['120', des120], ['130', des130],
           ['150', des150], ['170', des170]])























