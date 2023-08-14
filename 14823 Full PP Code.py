# Import libraries

import glob
import pandas as pd
import numpy as np
import scipy as sp
import sys
import os

#%% Set Working directory, Import all files and create dfs

os.chdir('C:/Users/cleed/Desktop/Data/Participant 01/PP/Session 1/TMS/5/Iso')

df130PP_5_S1 = pd.concat([pd.read_csv(file110, skiprows = 23) for file110 in glob.glob('01_AMT 130%*.csv')], ignore_index = True)
df150PP_5_S1 = pd.concat([pd.read_csv(file120, skiprows = 23) for file120 in glob.glob('01_AMT 150%*.csv')], ignore_index = True)
df_SICI_70_130_5_S1 = pd.concat([pd.read_csv(file70130, skiprows = 23) for file70130 in glob.glob('01_SICI 70 130*.csv')], ignore_index = True)
df_SICI_70_150_5_S1 = pd.concat([pd.read_csv(file70150, skiprows = 23) for file70150 in glob.glob('01_SICI 70 150*.csv')], ignore_index = True)
df_SICI_80_130_5_S1 = pd.concat([pd.read_csv(file80130, skiprows = 23) for file80130 in glob.glob('01_SICI 70 130*.csv')], ignore_index = True)
df_SICI_80_150_5_S1 = pd.concat([pd.read_csv(file80150, skiprows = 23) for file80150 in glob.glob('01_SICI 70 150*.csv')], ignore_index = True)
df_ICF_70_130_5_S1 = pd.concat([pd.read_csv(file70130, skiprows = 23) for file70130 in glob.glob('01_ICF 70 130*.csv')], ignore_index = True)
df_ICF_70_150_5_S1 = pd.concat([pd.read_csv(file70150, skiprows = 23) for file70150 in glob.glob('01_ICF 70 150*.csv')], ignore_index = True)
df_ICF_80_130_5_S1 = pd.concat([pd.read_csv(file80130, skiprows = 23) for file80130 in glob.glob('01_ICF 70 130*.csv')], ignore_index = True)
df_ICF_80_150_5_S1 = pd.concat([pd.read_csv(file80150, skiprows = 23) for file80150 in glob.glob('01_ICF 70 150*.csv')], ignore_index = True)

#%% Get MVC

os.chdir('C:/Users/cleed/Desktop/Data/Participant 01/PP/Session 1/Strength')

dfmvc_S1 = pd.concat([pd.read_csv(mvc, skiprows = 23) for mvc in glob.glob('01_Hamstring_MVC*.csv')], ignore_index = True)
mmax_S1 = dfmvc_S1['Torque'].min() * -1

#%% Get the Data we Need and Filter by Position

df130PP_5_S1 = df130PP_5_S1[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df130PP_5_S1 = df130PP_5_S1.ffill()
df130PP_5_S1 = df130PP_5_S1.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df130PP_5_S1 = df130PP_5_S1.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df150PP_5_S1 = df150PP_5_S1[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df150PP_5_S1 = df150PP_5_S1.ffill()
df150PP_5_S1 = df150PP_5_S1.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df150PP_5_S1 = df150PP_5_S1.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_SICI_70_130_5_S1 = df_SICI_70_130_5_S1[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_SICI_70_130_5_S1 = df_SICI_70_130_5_S1.ffill()
df_SICI_70_130_5_S1 = df_SICI_70_130_5_S1.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_SICI_70_130_5_S1 = df_SICI_70_130_5_S1.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_SICI_70_150_5_S1 = df_SICI_70_150_5_S1[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_SICI_70_150_5_S1 = df_SICI_70_150_5_S1.ffill()
df_SICI_70_150_5_S1 = df_SICI_70_150_5_S1.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_SICI_70_150_5_S1 = df_SICI_70_150_5_S1.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_SICI_80_130_5_S1 = df_SICI_80_130_5_S1[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_SICI_80_130_5_S1 = df_SICI_80_130_5_S1.ffill()
df_SICI_80_130_5_S1 = df_SICI_80_130_5_S1.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_SICI_80_130_5_S1 = df_SICI_80_130_5_S1.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_SICI_80_150_5_S1 = df_SICI_80_150_5_S1[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_SICI_80_150_5_S1 = df_SICI_80_150_5_S1.ffill()
df_SICI_80_150_5_S1 = df_SICI_80_150_5_S1.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_SICI_80_150_5_S1 = df_SICI_80_150_5_S1.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_ICF_70_130_5_S1 = df_ICF_70_130_5_S1[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_ICF_70_130_5_S1 = df_ICF_70_130_5_S1.ffill()
df_ICF_70_130_5_S1 = df_ICF_70_130_5_S1.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_ICF_70_130_5_S1 = df_ICF_70_130_5_S1.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_ICF_70_150_5_S1 = df_ICF_70_150_5_S1[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_ICF_70_150_5_S1 = df_ICF_70_150_5_S1.ffill()
df_ICF_70_150_5_S1 = df_ICF_70_150_5_S1.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_ICF_70_150_5_S1 = df_ICF_70_150_5_S1.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_ICF_80_130_5_S1 = df_ICF_80_130_5_S1[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_ICF_80_130_5_S1 = df_ICF_80_130_5_S1.ffill()
df_ICF_80_130_5_S1 = df_ICF_80_130_5_S1.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_ICF_80_130_5_S1 = df_ICF_80_130_5_S1.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_ICF_80_150_5_S1 = df_ICF_80_150_5_S1[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_ICF_80_150_5_S1 = df_ICF_80_150_5_S1.ffill()
df_ICF_80_150_5_S1 = df_ICF_80_150_5_S1.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_ICF_80_150_5_S1 = df_ICF_80_150_5_S1.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

#%% Account for EMG Offset

df130PP_5_S1['BF EMG (Offset)'] = df130PP_5_S1['BF EMG (Trigger)'] - np.mean(df130PP_5_S1['BF EMG (Trigger)'])
df150PP_5_S1['BF EMG (Offset)'] = df150PP_5_S1['BF EMG (Trigger)'] - np.mean(df150PP_5_S1['BF EMG (Trigger)'])

df_SICI_70_130_5_S1['BF EMG (Offset)'] = df_SICI_70_130_5_S1['BF EMG (Trigger)'] - np.mean(df_ICF_70_130_5_S1['BF EMG (Trigger)'])
df_SICI_70_150_5_S1['BF EMG (Offset)'] = df_SICI_70_150_5_S1['BF EMG (Trigger)'] - np.mean(df_ICF_70_150_5_S1['BF EMG (Trigger)'])
df_SICI_80_130_5_S1['BF EMG (Offset)'] = df_SICI_80_130_5_S1['BF EMG (Trigger)'] - np.mean(df_ICF_80_130_5_S1['BF EMG (Trigger)'])
df_SICI_80_150_5_S1['BF EMG (Offset)'] = df_SICI_80_150_5_S1['BF EMG (Trigger)'] - np.mean(df_SICI_80_150_5_S1['BF EMG (Trigger)'])

df_ICF_70_130_5_S1['BF EMG (Offset)'] = df_ICF_70_130_5_S1['BF EMG (Trigger)'] - np.mean(df_ICF_70_130_5_S1['BF EMG (Trigger)'])
df_ICF_70_150_5_S1['BF EMG (Offset)'] = df_ICF_70_150_5_S1['BF EMG (Trigger)'] - np.mean(df_ICF_70_150_5_S1['BF EMG (Trigger)'])
df_ICF_80_130_5_S1['BF EMG (Offset)'] = df_ICF_80_130_5_S1['BF EMG (Trigger)'] - np.mean(df_ICF_80_130_5_S1['BF EMG (Trigger)'])
df_ICF_80_150_5_S1['BF EMG (Offset)'] = df_ICF_80_150_5_S1['BF EMG (Trigger)'] - np.mean(df_ICF_80_150_5_S1['BF EMG (Trigger)'])

#%% Build and Apply Filter

high = 13/(1000/2)
low = 500/(1000/2)
b, a = sp.signal.butter(4, [high,low], btype='bandpass', analog=True)

df130PP_5_S1['BF Filtered'] = sp.signal.filtfilt(b, a, df130PP_5_S1['BF EMG (Offset)'])
df150PP_5_S1['BF Filtered'] = sp.signal.filtfilt(b, a, df150PP_5_S1['BF EMG (Offset)'])

df_SICI_70_130_5_S1['BF Filtered'] = sp.signal.filtfilt(b, a, df_SICI_70_130_5_S1['BF EMG (Offset)'])
df_SICI_70_150_5_S1['BF Filtered'] = sp.signal.filtfilt(b, a, df_SICI_70_150_5_S1['BF EMG (Offset)'])
df_SICI_80_130_5_S1['BF Filtered'] = sp.signal.filtfilt(b, a, df_SICI_80_130_5_S1['BF EMG (Offset)'])
df_SICI_80_150_5_S1['BF Filtered'] = sp.signal.filtfilt(b, a, df_SICI_80_150_5_S1['BF EMG (Offset)'])

df_ICF_70_130_5_S1['BF Filtered'] = sp.signal.filtfilt(b, a, df_ICF_70_130_5_S1['BF EMG (Offset)'])
df_ICF_70_150_5_S1['BF Filtered'] = sp.signal.filtfilt(b, a, df_ICF_70_150_5_S1['BF EMG (Offset)'])
df_ICF_80_130_5_S1['BF Filtered'] = sp.signal.filtfilt(b, a, df_ICF_80_130_5_S1['BF EMG (Offset)'])
df_ICF_80_150_5_S1['BF Filtered'] = sp.signal.filtfilt(b, a, df_ICF_80_150_5_S1['BF EMG (Offset)'])

#%% Append MVC

df130PP_5_S1['MVC'] =  mmax_S1
df150PP_5_S1['MVC'] =  mmax_S1

df_ICF_70_130_5_S1['MVC'] =  mmax_S1
df_ICF_70_150_5_S1['MVC'] =  mmax_S1
df_ICF_80_130_5_S1['MVC'] =  mmax_S1
df_ICF_80_150_5_S1['MVC'] =  mmax_S1

df_ICF_70_130_5_S1['MVC'] =  mmax_S1
df_ICF_70_150_5_S1['MVC'] =  mmax_S1
df_ICF_80_130_5_S1['MVC'] =  mmax_S1
df_ICF_80_150_5_S1['MVC'] =  mmax_S1

#%% Write to csv

df130PP_5_S1.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/df130PP_5_S1.csv')
df150PP_5_S1.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/df150PP_5_S1.csv')

df_SICI_70_130_5_S1.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/df_SICI_70_130_5_S1.csv')
df_SICI_70_150_5_S1.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/df_SICI_70_150_5_S1.csv')
df_SICI_80_130_5_S1.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/df_SICI_80_130_5_S1.csv')
df_SICI_80_150_5_S1.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/df_SICI_80_150_5_S1.csv')

df_ICF_70_130_5_S1.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/df_ICF_70_130_5_S1.csv')
df_ICF_70_150_5_S1.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/df_ICF_70_150_5_S1.csv')
df_ICF_80_130_5_S1.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/df_ICF_80_130_5_S1.csv')
df_ICF_80_150_5_S1.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/df_ICF_80_150_5_S1.csv')

#%%*************************************************************************************************************************%%#
#%% Session 1 10% 

os.chdir('C:/Users/cleed/Desktop/Data/Participant 01/PP/Session 1/TMS/10/Iso')

df130PP_10_S1 = pd.concat([pd.read_csv(file110, skiprows = 23) for file110 in glob.glob('01_AMT 130%*.csv')], ignore_index = True)
df150PP_10_S1 = pd.concat([pd.read_csv(file120, skiprows = 23) for file120 in glob.glob('01_AMT 150%*.csv')], ignore_index = True)
df_SICI_70_130_10_S1 = pd.concat([pd.read_csv(file70130, skiprows = 23) for file70130 in glob.glob('01_SICI 70 130*.csv')], ignore_index = True)
df_SICI_70_150_10_S1 = pd.concat([pd.read_csv(file70150, skiprows = 23) for file70150 in glob.glob('01_SICI 70 150*.csv')], ignore_index = True)
df_SICI_80_130_10_S1 = pd.concat([pd.read_csv(file80130, skiprows = 23) for file80130 in glob.glob('01_SICI 70 130*.csv')], ignore_index = True)
df_SICI_80_150_10_S1 = pd.concat([pd.read_csv(file80150, skiprows = 23) for file80150 in glob.glob('01_SICI 70 150*.csv')], ignore_index = True)
df_ICF_70_130_10_S1 = pd.concat([pd.read_csv(file70130, skiprows = 23) for file70130 in glob.glob('01_ICF 70 130*.csv')], ignore_index = True)
df_ICF_70_150_10_S1 = pd.concat([pd.read_csv(file70150, skiprows = 23) for file70150 in glob.glob('01_ICF 70 150*.csv')], ignore_index = True)
df_ICF_80_130_10_S1 = pd.concat([pd.read_csv(file80130, skiprows = 23) for file80130 in glob.glob('01_ICF 70 130*.csv')], ignore_index = True)
df_ICF_80_150_10_S1 = pd.concat([pd.read_csv(file80150, skiprows = 23) for file80150 in glob.glob('01_ICF 70 150*.csv')], ignore_index = True)


#%% Get the Data we Need and Filter by Position

df130PP_10_S1 = df130PP_10_S1[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df130PP_10_S1 = df130PP_10_S1.ffill()
df130PP_10_S1 = df130PP_10_S1.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df130PP_10_S1 = df130PP_10_S1.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df150PP_10_S1 = df150PP_10_S1[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df150PP_10_S1 = df150PP_10_S1.ffill()
df150PP_10_S1 = df150PP_10_S1.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df150PP_10_S1 = df150PP_10_S1.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_SICI_70_130_10_S1 = df_SICI_70_130_10_S1[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_SICI_70_130_10_S1 = df_SICI_70_130_10_S1.ffill()
df_SICI_70_130_10_S1 = df_SICI_70_130_10_S1.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_SICI_70_130_10_S1 = df_SICI_70_130_10_S1.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_SICI_70_150_10_S1 = df_SICI_70_150_10_S1[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_SICI_70_150_10_S1 = df_SICI_70_150_10_S1.ffill()
df_SICI_70_150_10_S1 = df_SICI_70_150_10_S1.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_SICI_70_150_10_S1 = df_SICI_70_150_10_S1.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_SICI_80_130_10_S1 = df_SICI_80_130_10_S1[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_SICI_80_130_10_S1 = df_SICI_80_130_10_S1.ffill()
df_SICI_80_130_10_S1 = df_SICI_80_130_10_S1.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_SICI_80_130_10_S1 = df_SICI_80_130_10_S1.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_SICI_80_150_10_S1 = df_SICI_80_150_10_S1[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_SICI_80_150_10_S1 = df_SICI_80_150_10_S1.ffill()
df_SICI_80_150_10_S1 = df_SICI_80_150_10_S1.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_SICI_80_150_10_S1 = df_SICI_80_150_10_S1.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_ICF_70_130_10_S1 = df_ICF_70_130_10_S1[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_ICF_70_130_10_S1 = df_ICF_70_130_10_S1.ffill()
df_ICF_70_130_10_S1 = df_ICF_70_130_10_S1.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_ICF_70_130_10_S1 = df_ICF_70_130_10_S1.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_ICF_70_150_10_S1 = df_ICF_70_150_10_S1[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_ICF_70_150_10_S1 = df_ICF_70_150_10_S1.ffill()
df_ICF_70_150_10_S1 = df_ICF_70_150_10_S1.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_ICF_70_150_10_S1 = df_ICF_70_150_10_S1.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_ICF_80_130_10_S1 = df_ICF_80_130_10_S1[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_ICF_80_130_10_S1 = df_ICF_80_130_10_S1.ffill()
df_ICF_80_130_10_S1 = df_ICF_80_130_10_S1.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_ICF_80_130_10_S1 = df_ICF_80_130_10_S1.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_ICF_80_150_10_S1 = df_ICF_80_150_10_S1[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_ICF_80_150_10_S1 = df_ICF_80_150_10_S1.ffill()
df_ICF_80_150_10_S1 = df_ICF_80_150_10_S1.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_ICF_80_150_10_S1 = df_ICF_80_150_10_S1.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

#%% Account for EMG Offset

df130PP_10_S1['BF EMG (Offset)'] = df130PP_10_S1['BF EMG (Trigger)'] - np.mean(df130PP_10_S1['BF EMG (Trigger)'])
df150PP_10_S1['BF EMG (Offset)'] = df150PP_10_S1['BF EMG (Trigger)'] - np.mean(df150PP_10_S1['BF EMG (Trigger)'])

df_SICI_70_130_10_S1['BF EMG (Offset)'] = df_SICI_70_130_10_S1['BF EMG (Trigger)'] - np.mean(df_ICF_70_130_10_S1['BF EMG (Trigger)'])
df_SICI_70_150_10_S1['BF EMG (Offset)'] = df_SICI_70_150_10_S1['BF EMG (Trigger)'] - np.mean(df_ICF_70_150_10_S1['BF EMG (Trigger)'])
df_SICI_80_130_10_S1['BF EMG (Offset)'] = df_SICI_80_130_10_S1['BF EMG (Trigger)'] - np.mean(df_ICF_80_130_10_S1['BF EMG (Trigger)'])
df_SICI_80_150_10_S1['BF EMG (Offset)'] = df_SICI_80_150_10_S1['BF EMG (Trigger)'] - np.mean(df_SICI_80_150_10_S1['BF EMG (Trigger)'])

df_ICF_70_130_10_S1['BF EMG (Offset)'] = df_ICF_70_130_10_S1['BF EMG (Trigger)'] - np.mean(df_ICF_70_130_10_S1['BF EMG (Trigger)'])
df_ICF_70_150_10_S1['BF EMG (Offset)'] = df_ICF_70_150_10_S1['BF EMG (Trigger)'] - np.mean(df_ICF_70_150_10_S1['BF EMG (Trigger)'])
df_ICF_80_130_10_S1['BF EMG (Offset)'] = df_ICF_80_130_10_S1['BF EMG (Trigger)'] - np.mean(df_ICF_80_130_10_S1['BF EMG (Trigger)'])
df_ICF_80_150_10_S1['BF EMG (Offset)'] = df_ICF_80_150_10_S1['BF EMG (Trigger)'] - np.mean(df_ICF_80_150_10_S1['BF EMG (Trigger)'])

#%% Build and Apply Filter

high = 13/(1000/2)
low = 500/(1000/2)
b, a = sp.signal.butter(4, [high,low], btype='bandpass', analog=True)

df130PP_10_S1['BF Filtered'] = sp.signal.filtfilt(b, a, df130PP_10_S1['BF EMG (Offset)'])
df150PP_10_S1['BF Filtered'] = sp.signal.filtfilt(b, a, df150PP_10_S1['BF EMG (Offset)'])

df_SICI_70_130_10_S1['BF Filtered'] = sp.signal.filtfilt(b, a, df_SICI_70_130_10_S1['BF EMG (Offset)'])
df_SICI_70_150_10_S1['BF Filtered'] = sp.signal.filtfilt(b, a, df_SICI_70_150_10_S1['BF EMG (Offset)'])
df_SICI_80_130_10_S1['BF Filtered'] = sp.signal.filtfilt(b, a, df_SICI_80_130_10_S1['BF EMG (Offset)'])
df_SICI_80_150_10_S1['BF Filtered'] = sp.signal.filtfilt(b, a, df_SICI_80_150_10_S1['BF EMG (Offset)'])

df_ICF_70_130_10_S1['BF Filtered'] = sp.signal.filtfilt(b, a, df_ICF_70_130_10_S1['BF EMG (Offset)'])
df_ICF_70_150_10_S1['BF Filtered'] = sp.signal.filtfilt(b, a, df_ICF_70_150_10_S1['BF EMG (Offset)'])
df_ICF_80_130_10_S1['BF Filtered'] = sp.signal.filtfilt(b, a, df_ICF_80_130_10_S1['BF EMG (Offset)'])
df_ICF_80_150_10_S1['BF Filtered'] = sp.signal.filtfilt(b, a, df_ICF_80_150_10_S1['BF EMG (Offset)'])

#%% Append MVC

df130PP_10_S1['MVC'] =  mmax_S1
df150PP_10_S1['MVC'] =  mmax_S1

df_ICF_70_130_10_S1['MVC'] =  mmax_S1
df_ICF_70_150_10_S1['MVC'] =  mmax_S1
df_ICF_80_130_10_S1['MVC'] =  mmax_S1
df_ICF_80_150_10_S1['MVC'] =  mmax_S1

df_ICF_70_130_10_S1['MVC'] =  mmax_S1
df_ICF_70_150_10_S1['MVC'] =  mmax_S1
df_ICF_80_130_10_S1['MVC'] =  mmax_S1
df_ICF_80_150_10_S1['MVC'] =  mmax_S1

#%% Write to csv

df130PP_10_S1.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/df130PP_10_S1.csv')
df150PP_10_S1.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/df150PP_10_S1.csv')

df_SICI_70_130_10_S1.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/df_SICI_70_130_10_S1.csv')
df_SICI_70_150_10_S1.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/df_SICI_70_150_10_S1.csv')
df_SICI_80_130_10_S1.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/df_SICI_80_130_10_S1.csv')
df_SICI_80_150_10_S1.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/df_SICI_80_150_10_S1.csv')

df_ICF_70_130_10_S1.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/df_ICF_70_130_10_S1.csv')
df_ICF_70_150_10_S1.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/df_ICF_70_150_10_S1.csv')
df_ICF_80_130_10_S1.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/df_ICF_80_130_10_S1.csv')
df_ICF_80_150_10_S1.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/df_ICF_80_150_10_S1.csv')

#%%*************************************************************************************************************************%%#
#%% Session 2

os.chdir('C:/Users/cleed/Desktop/Data/Participant 01/PP/Session 2/TMS/5/Iso')

df130PP_5_S2 = pd.concat([pd.read_csv(file110, skiprows = 23) for file110 in glob.glob('01_AMT 130%*.csv')], ignore_index = True)
df150PP_5_S2 = pd.concat([pd.read_csv(file120, skiprows = 23) for file120 in glob.glob('01_AMT 150%*.csv')], ignore_index = True)
df_SICI_70_130_5_S2 = pd.concat([pd.read_csv(file70130, skiprows = 23) for file70130 in glob.glob('01_SICI 70 130*.csv')], ignore_index = True)
df_SICI_70_150_5_S2 = pd.concat([pd.read_csv(file70150, skiprows = 23) for file70150 in glob.glob('01_SICI 70 150*.csv')], ignore_index = True)
df_SICI_80_130_5_S2 = pd.concat([pd.read_csv(file80130, skiprows = 23) for file80130 in glob.glob('01_SICI 70 130*.csv')], ignore_index = True)
df_SICI_80_150_5_S2 = pd.concat([pd.read_csv(file80150, skiprows = 23) for file80150 in glob.glob('01_SICI 70 150*.csv')], ignore_index = True)
df_ICF_70_130_5_S2 = pd.concat([pd.read_csv(file70130, skiprows = 23) for file70130 in glob.glob('01_ICF 70 130*.csv')], ignore_index = True)
df_ICF_70_150_5_S2 = pd.concat([pd.read_csv(file70150, skiprows = 23) for file70150 in glob.glob('01_ICF 70 150*.csv')], ignore_index = True)
df_ICF_80_130_5_S2 = pd.concat([pd.read_csv(file80130, skiprows = 23) for file80130 in glob.glob('01_ICF 70 130*.csv')], ignore_index = True)
df_ICF_80_150_5_S2 = pd.concat([pd.read_csv(file80150, skiprows = 23) for file80150 in glob.glob('01_ICF 70 150*.csv')], ignore_index = True)

#%% Get MVC

os.chdir('C:/Users/cleed/Desktop/Data/Participant 01/PP/Session 2/Strength')

dfmvc_S2 = pd.concat([pd.read_csv(mvc, skiprows = 23) for mvc in glob.glob('01_Hamstring_MVC*.csv')], ignore_index = True)
mmax_S2 = dfmvc_S2['Torque'].min() * -1

#%% Get the Data we Need and Filter by Position

df130PP_5_S2 = df130PP_5_S2[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df130PP_5_S2 = df130PP_5_S2.ffill()
df130PP_5_S2 = df130PP_5_S2.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df130PP_5_S2 = df130PP_5_S2.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df150PP_5_S2 = df150PP_5_S2[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df150PP_5_S2 = df150PP_5_S2.ffill()
df150PP_5_S2 = df150PP_5_S2.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df150PP_5_S2 = df150PP_5_S2.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_SICI_70_130_5_S2 = df_SICI_70_130_5_S2[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_SICI_70_130_5_S2 = df_SICI_70_130_5_S2.ffill()
df_SICI_70_130_5_S2 = df_SICI_70_130_5_S2.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_SICI_70_130_5_S2 = df_SICI_70_130_5_S2.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_SICI_70_150_5_S2 = df_SICI_70_150_5_S2[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_SICI_70_150_5_S2 = df_SICI_70_150_5_S2.ffill()
df_SICI_70_150_5_S2 = df_SICI_70_150_5_S2.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_SICI_70_150_5_S2 = df_SICI_70_150_5_S2.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_SICI_80_130_5_S2 = df_SICI_80_130_5_S2[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_SICI_80_130_5_S2 = df_SICI_80_130_5_S2.ffill()
df_SICI_80_130_5_S2 = df_SICI_80_130_5_S2.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_SICI_80_130_5_S2 = df_SICI_80_130_5_S2.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_SICI_80_150_5_S2 = df_SICI_80_150_5_S2[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_SICI_80_150_5_S2 = df_SICI_80_150_5_S2.ffill()
df_SICI_80_150_5_S2 = df_SICI_80_150_5_S2.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_SICI_80_150_5_S2 = df_SICI_80_150_5_S2.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_ICF_70_130_5_S2 = df_ICF_70_130_5_S2[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_ICF_70_130_5_S2 = df_ICF_70_130_5_S2.ffill()
df_ICF_70_130_5_S2 = df_ICF_70_130_5_S2.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_ICF_70_130_5_S2 = df_ICF_70_130_5_S2.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_ICF_70_150_5_S2 = df_ICF_70_150_5_S2[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_ICF_70_150_5_S2 = df_ICF_70_150_5_S2.ffill()
df_ICF_70_150_5_S2 = df_ICF_70_150_5_S2.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_ICF_70_150_5_S2 = df_ICF_70_150_5_S2.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_ICF_80_130_5_S2 = df_ICF_80_130_5_S2[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_ICF_80_130_5_S2 = df_ICF_80_130_5_S2.ffill()
df_ICF_80_130_5_S2 = df_ICF_80_130_5_S2.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_ICF_80_130_5_S2 = df_ICF_80_130_5_S2.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_ICF_80_150_5_S2 = df_ICF_80_150_5_S2[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_ICF_80_150_5_S2 = df_ICF_80_150_5_S2.ffill()
df_ICF_80_150_5_S2 = df_ICF_80_150_5_S2.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_ICF_80_150_5_S2 = df_ICF_80_150_5_S2.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

#%% Account for EMG Offset

df130PP_5_S2['BF EMG (Offset)'] = df130PP_5_S2['BF EMG (Trigger)'] - np.mean(df130PP_5_S2['BF EMG (Trigger)'])
df150PP_5_S2['BF EMG (Offset)'] = df150PP_5_S2['BF EMG (Trigger)'] - np.mean(df150PP_5_S2['BF EMG (Trigger)'])

df_SICI_70_130_5_S2['BF EMG (Offset)'] = df_SICI_70_130_5_S2['BF EMG (Trigger)'] - np.mean(df_ICF_70_130_5_S2['BF EMG (Trigger)'])
df_SICI_70_150_5_S2['BF EMG (Offset)'] = df_SICI_70_150_5_S2['BF EMG (Trigger)'] - np.mean(df_ICF_70_150_5_S2['BF EMG (Trigger)'])
df_SICI_80_130_5_S2['BF EMG (Offset)'] = df_SICI_80_130_5_S2['BF EMG (Trigger)'] - np.mean(df_ICF_80_130_5_S2['BF EMG (Trigger)'])
df_SICI_80_150_5_S2['BF EMG (Offset)'] = df_SICI_80_150_5_S2['BF EMG (Trigger)'] - np.mean(df_SICI_80_150_5_S2['BF EMG (Trigger)'])

df_ICF_70_130_5_S2['BF EMG (Offset)'] = df_ICF_70_130_5_S2['BF EMG (Trigger)'] - np.mean(df_ICF_70_130_5_S2['BF EMG (Trigger)'])
df_ICF_70_150_5_S2['BF EMG (Offset)'] = df_ICF_70_150_5_S2['BF EMG (Trigger)'] - np.mean(df_ICF_70_150_5_S2['BF EMG (Trigger)'])
df_ICF_80_130_5_S2['BF EMG (Offset)'] = df_ICF_80_130_5_S2['BF EMG (Trigger)'] - np.mean(df_ICF_80_130_5_S2['BF EMG (Trigger)'])
df_ICF_80_150_5_S2['BF EMG (Offset)'] = df_ICF_80_150_5_S2['BF EMG (Trigger)'] - np.mean(df_ICF_80_150_5_S2['BF EMG (Trigger)'])

#%% Build and Apply Filter

high = 13/(1000/2)
low = 500/(1000/2)
b, a = sp.signal.butter(4, [high,low], btype='bandpass', analog=True)

df130PP_5_S2['BF Filtered'] = sp.signal.filtfilt(b, a, df130PP_5_S2['BF EMG (Offset)'])
df150PP_5_S2['BF Filtered'] = sp.signal.filtfilt(b, a, df150PP_5_S2['BF EMG (Offset)'])

df_SICI_70_130_5_S2['BF Filtered'] = sp.signal.filtfilt(b, a, df_SICI_70_130_5_S2['BF EMG (Offset)'])
df_SICI_70_150_5_S2['BF Filtered'] = sp.signal.filtfilt(b, a, df_SICI_70_150_5_S2['BF EMG (Offset)'])
df_SICI_80_130_5_S2['BF Filtered'] = sp.signal.filtfilt(b, a, df_SICI_80_130_5_S2['BF EMG (Offset)'])
df_SICI_80_150_5_S2['BF Filtered'] = sp.signal.filtfilt(b, a, df_SICI_80_150_5_S2['BF EMG (Offset)'])

df_ICF_70_130_5_S2['BF Filtered'] = sp.signal.filtfilt(b, a, df_ICF_70_130_5_S2['BF EMG (Offset)'])
df_ICF_70_150_5_S2['BF Filtered'] = sp.signal.filtfilt(b, a, df_ICF_70_150_5_S2['BF EMG (Offset)'])
df_ICF_80_130_5_S2['BF Filtered'] = sp.signal.filtfilt(b, a, df_ICF_80_130_5_S2['BF EMG (Offset)'])
df_ICF_80_150_5_S2['BF Filtered'] = sp.signal.filtfilt(b, a, df_ICF_80_150_5_S2['BF EMG (Offset)'])

#%% Append MVC

df130PP_5_S2['MVC'] =  mmax_S2
df150PP_5_S2['MVC'] =  mmax_S2

df_ICF_70_130_5_S2['MVC'] =  mmax_S2
df_ICF_70_150_5_S2['MVC'] =  mmax_S2
df_ICF_80_130_5_S2['MVC'] =  mmax_S2
df_ICF_80_150_5_S2['MVC'] =  mmax_S2

df_ICF_70_130_5_S2['MVC'] =  mmax_S2
df_ICF_70_150_5_S2['MVC'] =  mmax_S2
df_ICF_80_130_5_S2['MVC'] =  mmax_S2
df_ICF_80_150_5_S2['MVC'] =  mmax_S2

#%% Write to csv

df130PP_5_S2.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/df130PP_5_S2.csv')
df150PP_5_S2.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/df150PP_5_S2.csv')

df_SICI_70_130_5_S2.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/df_SICI_70_130_5_S2.csv')
df_SICI_70_150_5_S2.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/df_SICI_70_150_5_S2.csv')
df_SICI_80_130_5_S2.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/df_SICI_80_130_5_S2.csv')
df_SICI_80_150_5_S2.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/df_SICI_80_150_5_S2.csv')

df_ICF_70_130_5_S2.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/df_ICF_70_130_5_S2.csv')
df_ICF_70_150_5_S2.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/df_ICF_70_150_5_S2.csv')
df_ICF_80_130_5_S2.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/df_ICF_80_130_5_S2.csv')
df_ICF_80_150_5_S2.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/df_ICF_80_150_5_S2.csv')

#%%*************************************************************************************************************************%%#
#%% Sessions 2 10%

os.chdir('C:/Users/cleed/Desktop/Data/Participant 01/PP/Session 2/TMS/10/Iso')

df130PP_10_S2 = pd.concat([pd.read_csv(file110, skiprows = 23) for file110 in glob.glob('01_AMT 130%*.csv')], ignore_index = True)
df150PP_10_S2 = pd.concat([pd.read_csv(file120, skiprows = 23) for file120 in glob.glob('01_AMT 150%*.csv')], ignore_index = True)
df_SICI_70_130_10_S2 = pd.concat([pd.read_csv(file70130, skiprows = 23) for file70130 in glob.glob('01_SICI 70 130*.csv')], ignore_index = True)
df_SICI_70_150_10_S2 = pd.concat([pd.read_csv(file70150, skiprows = 23) for file70150 in glob.glob('01_SICI 70 150*.csv')], ignore_index = True)
df_SICI_80_130_10_S2 = pd.concat([pd.read_csv(file80130, skiprows = 23) for file80130 in glob.glob('01_SICI 70 130*.csv')], ignore_index = True)
df_SICI_80_150_10_S2 = pd.concat([pd.read_csv(file80150, skiprows = 23) for file80150 in glob.glob('01_SICI 70 150*.csv')], ignore_index = True)
df_ICF_70_130_10_S2 = pd.concat([pd.read_csv(file70130, skiprows = 23) for file70130 in glob.glob('01_ICF 70 130*.csv')], ignore_index = True)
df_ICF_70_150_10_S2 = pd.concat([pd.read_csv(file70150, skiprows = 23) for file70150 in glob.glob('01_ICF 70 150*.csv')], ignore_index = True)
df_ICF_80_130_10_S2 = pd.concat([pd.read_csv(file80130, skiprows = 23) for file80130 in glob.glob('01_ICF 70 130*.csv')], ignore_index = True)
df_ICF_80_150_10_S2 = pd.concat([pd.read_csv(file80150, skiprows = 23) for file80150 in glob.glob('01_ICF 70 150*.csv')], ignore_index = True)

#%% Get the Data we Need and Filter by Position

df130PP_10_S2 = df130PP_10_S2[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df130PP_10_S2 = df130PP_10_S2.ffill()
df130PP_10_S2 = df130PP_10_S2.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df130PP_10_S2 = df130PP_10_S2.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df150PP_10_S2 = df150PP_10_S2[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df150PP_10_S2 = df150PP_10_S2.ffill()
df150PP_10_S2 = df150PP_10_S2.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df150PP_10_S2 = df150PP_10_S2.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_SICI_70_130_10_S2 = df_SICI_70_130_10_S2[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_SICI_70_130_10_S2 = df_SICI_70_130_10_S2.ffill()
df_SICI_70_130_10_S2 = df_SICI_70_130_10_S2.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_SICI_70_130_10_S2 = df_SICI_70_130_10_S2.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_SICI_70_150_10_S2 = df_SICI_70_150_10_S2[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_SICI_70_150_10_S2 = df_SICI_70_150_10_S2.ffill()
df_SICI_70_150_10_S2 = df_SICI_70_150_10_S2.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_SICI_70_150_10_S2 = df_SICI_70_150_10_S2.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_SICI_80_130_10_S2 = df_SICI_80_130_10_S2[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_SICI_80_130_10_S2 = df_SICI_80_130_10_S2.ffill()
df_SICI_80_130_10_S2 = df_SICI_80_130_10_S2.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_SICI_80_130_10_S2 = df_SICI_80_130_10_S2.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_SICI_80_150_10_S2 = df_SICI_80_150_10_S2[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_SICI_80_150_10_S2 = df_SICI_80_150_10_S2.ffill()
df_SICI_80_150_10_S2 = df_SICI_80_150_10_S2.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_SICI_80_150_10_S2 = df_SICI_80_150_10_S2.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_ICF_70_130_10_S2 = df_ICF_70_130_10_S2[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_ICF_70_130_10_S2 = df_ICF_70_130_10_S2.ffill()
df_ICF_70_130_10_S2 = df_ICF_70_130_10_S2.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_ICF_70_130_10_S2 = df_ICF_70_130_10_S2.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_ICF_70_150_10_S2 = df_ICF_70_150_10_S2[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_ICF_70_150_10_S2 = df_ICF_70_150_10_S2.ffill()
df_ICF_70_150_10_S2 = df_ICF_70_150_10_S2.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_ICF_70_150_10_S2 = df_ICF_70_150_10_S2.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_ICF_80_130_10_S2 = df_ICF_80_130_10_S2[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_ICF_80_130_10_S2 = df_ICF_80_130_10_S2.ffill()
df_ICF_80_130_10_S2 = df_ICF_80_130_10_S2.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_ICF_80_130_10_S2 = df_ICF_80_130_10_S2.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_ICF_80_150_10_S2 = df_ICF_80_150_10_S2[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_ICF_80_150_10_S2 = df_ICF_80_150_10_S2.ffill()
df_ICF_80_150_10_S2 = df_ICF_80_150_10_S2.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_ICF_80_150_10_S2 = df_ICF_80_150_10_S2.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

#%% Account for EMG Offset

df130PP_10_S2['BF EMG (Offset)'] = df130PP_10_S2['BF EMG (Trigger)'] - np.mean(df130PP_10_S2['BF EMG (Trigger)'])
df150PP_10_S2['BF EMG (Offset)'] = df150PP_10_S2['BF EMG (Trigger)'] - np.mean(df150PP_10_S2['BF EMG (Trigger)'])

df_SICI_70_130_10_S2['BF EMG (Offset)'] = df_SICI_70_130_10_S2['BF EMG (Trigger)'] - np.mean(df_ICF_70_130_10_S2['BF EMG (Trigger)'])
df_SICI_70_150_10_S2['BF EMG (Offset)'] = df_SICI_70_150_10_S2['BF EMG (Trigger)'] - np.mean(df_ICF_70_150_10_S2['BF EMG (Trigger)'])
df_SICI_80_130_10_S2['BF EMG (Offset)'] = df_SICI_80_130_10_S2['BF EMG (Trigger)'] - np.mean(df_ICF_80_130_10_S2['BF EMG (Trigger)'])
df_SICI_80_150_10_S2['BF EMG (Offset)'] = df_SICI_80_150_10_S2['BF EMG (Trigger)'] - np.mean(df_SICI_80_150_10_S2['BF EMG (Trigger)'])

df_ICF_70_130_10_S2['BF EMG (Offset)'] = df_ICF_70_130_10_S2['BF EMG (Trigger)'] - np.mean(df_ICF_70_130_10_S2['BF EMG (Trigger)'])
df_ICF_70_150_10_S2['BF EMG (Offset)'] = df_ICF_70_150_10_S2['BF EMG (Trigger)'] - np.mean(df_ICF_70_150_10_S2['BF EMG (Trigger)'])
df_ICF_80_130_10_S2['BF EMG (Offset)'] = df_ICF_80_130_10_S2['BF EMG (Trigger)'] - np.mean(df_ICF_80_130_10_S2['BF EMG (Trigger)'])
df_ICF_80_150_10_S2['BF EMG (Offset)'] = df_ICF_80_150_10_S2['BF EMG (Trigger)'] - np.mean(df_ICF_80_150_10_S2['BF EMG (Trigger)'])

#%% Build and Apply Filter

high = 13/(1000/2)
low = 500/(1000/2)
b, a = sp.signal.butter(4, [high,low], btype='bandpass', analog=True)

df130PP_10_S2['BF Filtered'] = sp.signal.filtfilt(b, a, df130PP_10_S2['BF EMG (Offset)'])
df150PP_10_S2['BF Filtered'] = sp.signal.filtfilt(b, a, df150PP_10_S2['BF EMG (Offset)'])

df_SICI_70_130_10_S2['BF Filtered'] = sp.signal.filtfilt(b, a, df_SICI_70_130_10_S2['BF EMG (Offset)'])
df_SICI_70_150_10_S2['BF Filtered'] = sp.signal.filtfilt(b, a, df_SICI_70_150_10_S2['BF EMG (Offset)'])
df_SICI_80_130_10_S2['BF Filtered'] = sp.signal.filtfilt(b, a, df_SICI_80_130_10_S2['BF EMG (Offset)'])
df_SICI_80_150_10_S2['BF Filtered'] = sp.signal.filtfilt(b, a, df_SICI_80_150_10_S2['BF EMG (Offset)'])

df_ICF_70_130_10_S2['BF Filtered'] = sp.signal.filtfilt(b, a, df_ICF_70_130_10_S2['BF EMG (Offset)'])
df_ICF_70_150_10_S2['BF Filtered'] = sp.signal.filtfilt(b, a, df_ICF_70_150_10_S2['BF EMG (Offset)'])
df_ICF_80_130_10_S2['BF Filtered'] = sp.signal.filtfilt(b, a, df_ICF_80_130_10_S2['BF EMG (Offset)'])
df_ICF_80_150_10_S2['BF Filtered'] = sp.signal.filtfilt(b, a, df_ICF_80_150_10_S2['BF EMG (Offset)'])

#%% Append MVC

df130PP_10_S2['MVC'] =  mmax_S2
df150PP_10_S2['MVC'] =  mmax_S2

df_ICF_70_130_10_S2['MVC'] =  mmax_S2
df_ICF_70_150_10_S2['MVC'] =  mmax_S2
df_ICF_80_130_10_S2['MVC'] =  mmax_S2
df_ICF_80_150_10_S2['MVC'] =  mmax_S2

df_ICF_70_130_10_S2['MVC'] =  mmax_S2
df_ICF_70_150_10_S2['MVC'] =  mmax_S2
df_ICF_80_130_10_S2['MVC'] =  mmax_S2
df_ICF_80_150_10_S2['MVC'] =  mmax_S2

#%% Write to csv

df130PP_10_S2.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/df130PP_10_S2.csv')
df150PP_10_S2.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/df150PP_10_S2.csv')

df_SICI_70_130_10_S2.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/df_SICI_70_130_10_S2.csv')
df_SICI_70_150_10_S2.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/df_SICI_70_150_10_S2.csv')
df_SICI_80_130_10_S2.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/df_SICI_80_130_10_S2.csv')
df_SICI_80_150_10_S2.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/df_SICI_80_150_10_S2.csv')

df_ICF_70_130_10_S2.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/df_ICF_70_130_10_S2.csv')
df_ICF_70_150_10_S2.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/df_ICF_70_150_10_S2.csv')
df_ICF_80_130_10_S2.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/df_ICF_80_130_10_S2.csv')
df_ICF_80_150_10_S2.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/df_ICF_80_150_10_S2.csv')

#%% ECC *****************************************************************************************************************************

#%% Set Working directory, Import all files and create dfs

os.chdir('C:/Users/cleed/Desktop/Data/Participant 01/PP/Session 1/TMS/5/Ecc')

df130PP_5_S1 = pd.concat([pd.read_csv(file110, skiprows = 23) for file110 in glob.glob('01_AMT 130%*.csv')], ignore_index = True)
df150PP_5_S1 = pd.concat([pd.read_csv(file120, skiprows = 23) for file120 in glob.glob('01_AMT 150%*.csv')], ignore_index = True)
df_SICI_70_130_5_S1 = pd.concat([pd.read_csv(file70130, skiprows = 23) for file70130 in glob.glob('01_SICI 70 130*.csv')], ignore_index = True)
df_SICI_70_150_5_S1 = pd.concat([pd.read_csv(file70150, skiprows = 23) for file70150 in glob.glob('01_SICI 70 150*.csv')], ignore_index = True)
df_SICI_80_130_5_S1 = pd.concat([pd.read_csv(file80130, skiprows = 23) for file80130 in glob.glob('01_SICI 70 130*.csv')], ignore_index = True)
df_SICI_80_150_5_S1 = pd.concat([pd.read_csv(file80150, skiprows = 23) for file80150 in glob.glob('01_SICI 70 150*.csv')], ignore_index = True)
df_ICF_70_130_5_S1 = pd.concat([pd.read_csv(file70130, skiprows = 23) for file70130 in glob.glob('01_ICF 70 130*.csv')], ignore_index = True)
df_ICF_70_150_5_S1 = pd.concat([pd.read_csv(file70150, skiprows = 23) for file70150 in glob.glob('01_ICF 70 150*.csv')], ignore_index = True)
df_ICF_80_130_5_S1 = pd.concat([pd.read_csv(file80130, skiprows = 23) for file80130 in glob.glob('01_ICF 70 130*.csv')], ignore_index = True)
df_ICF_80_150_5_S1 = pd.concat([pd.read_csv(file80150, skiprows = 23) for file80150 in glob.glob('01_ICF 70 150*.csv')], ignore_index = True)

#%% Get MVC

os.chdir('C:/Users/cleed/Desktop/Data/Participant 01/PP/Session 1/Strength')

dfmvc_S1 = pd.concat([pd.read_csv(mvc, skiprows = 23) for mvc in glob.glob('01_Hamstring_MVC*.csv')], ignore_index = True)
mmax_S1 = dfmvc_S1['Torque'].min() * -1

#%% Get the Data we Need and Filter by Position

df130PP_5_S1 = df130PP_5_S1[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df130PP_5_S1 = df130PP_5_S1.ffill()
df130PP_5_S1 = df130PP_5_S1.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df130PP_5_S1 = df130PP_5_S1.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df150PP_5_S1 = df150PP_5_S1[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df150PP_5_S1 = df150PP_5_S1.ffill()
df150PP_5_S1 = df150PP_5_S1.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df150PP_5_S1 = df150PP_5_S1.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_SICI_70_130_5_S1 = df_SICI_70_130_5_S1[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_SICI_70_130_5_S1 = df_SICI_70_130_5_S1.ffill()
df_SICI_70_130_5_S1 = df_SICI_70_130_5_S1.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_SICI_70_130_5_S1 = df_SICI_70_130_5_S1.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_SICI_70_150_5_S1 = df_SICI_70_150_5_S1[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_SICI_70_150_5_S1 = df_SICI_70_150_5_S1.ffill()
df_SICI_70_150_5_S1 = df_SICI_70_150_5_S1.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_SICI_70_150_5_S1 = df_SICI_70_150_5_S1.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_SICI_80_130_5_S1 = df_SICI_80_130_5_S1[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_SICI_80_130_5_S1 = df_SICI_80_130_5_S1.ffill()
df_SICI_80_130_5_S1 = df_SICI_80_130_5_S1.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_SICI_80_130_5_S1 = df_SICI_80_130_5_S1.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_SICI_80_150_5_S1 = df_SICI_80_150_5_S1[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_SICI_80_150_5_S1 = df_SICI_80_150_5_S1.ffill()
df_SICI_80_150_5_S1 = df_SICI_80_150_5_S1.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_SICI_80_150_5_S1 = df_SICI_80_150_5_S1.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_ICF_70_130_5_S1 = df_ICF_70_130_5_S1[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_ICF_70_130_5_S1 = df_ICF_70_130_5_S1.ffill()
df_ICF_70_130_5_S1 = df_ICF_70_130_5_S1.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_ICF_70_130_5_S1 = df_ICF_70_130_5_S1.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_ICF_70_150_5_S1 = df_ICF_70_150_5_S1[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_ICF_70_150_5_S1 = df_ICF_70_150_5_S1.ffill()
df_ICF_70_150_5_S1 = df_ICF_70_150_5_S1.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_ICF_70_150_5_S1 = df_ICF_70_150_5_S1.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_ICF_80_130_5_S1 = df_ICF_80_130_5_S1[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_ICF_80_130_5_S1 = df_ICF_80_130_5_S1.ffill()
df_ICF_80_130_5_S1 = df_ICF_80_130_5_S1.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_ICF_80_130_5_S1 = df_ICF_80_130_5_S1.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_ICF_80_150_5_S1 = df_ICF_80_150_5_S1[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_ICF_80_150_5_S1 = df_ICF_80_150_5_S1.ffill()
df_ICF_80_150_5_S1 = df_ICF_80_150_5_S1.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_ICF_80_150_5_S1 = df_ICF_80_150_5_S1.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

#%% Account for EMG Offset

df130PP_5_S1['BF EMG (Offset)'] = df130PP_5_S1['BF EMG (Trigger)'] - np.mean(df130PP_5_S1['BF EMG (Trigger)'])
df150PP_5_S1['BF EMG (Offset)'] = df150PP_5_S1['BF EMG (Trigger)'] - np.mean(df150PP_5_S1['BF EMG (Trigger)'])

df_SICI_70_130_5_S1['BF EMG (Offset)'] = df_SICI_70_130_5_S1['BF EMG (Trigger)'] - np.mean(df_ICF_70_130_5_S1['BF EMG (Trigger)'])
df_SICI_70_150_5_S1['BF EMG (Offset)'] = df_SICI_70_150_5_S1['BF EMG (Trigger)'] - np.mean(df_ICF_70_150_5_S1['BF EMG (Trigger)'])
df_SICI_80_130_5_S1['BF EMG (Offset)'] = df_SICI_80_130_5_S1['BF EMG (Trigger)'] - np.mean(df_ICF_80_130_5_S1['BF EMG (Trigger)'])
df_SICI_80_150_5_S1['BF EMG (Offset)'] = df_SICI_80_150_5_S1['BF EMG (Trigger)'] - np.mean(df_SICI_80_150_5_S1['BF EMG (Trigger)'])

df_ICF_70_130_5_S1['BF EMG (Offset)'] = df_ICF_70_130_5_S1['BF EMG (Trigger)'] - np.mean(df_ICF_70_130_5_S1['BF EMG (Trigger)'])
df_ICF_70_150_5_S1['BF EMG (Offset)'] = df_ICF_70_150_5_S1['BF EMG (Trigger)'] - np.mean(df_ICF_70_150_5_S1['BF EMG (Trigger)'])
df_ICF_80_130_5_S1['BF EMG (Offset)'] = df_ICF_80_130_5_S1['BF EMG (Trigger)'] - np.mean(df_ICF_80_130_5_S1['BF EMG (Trigger)'])
df_ICF_80_150_5_S1['BF EMG (Offset)'] = df_ICF_80_150_5_S1['BF EMG (Trigger)'] - np.mean(df_ICF_80_150_5_S1['BF EMG (Trigger)'])

#%% Build and Apply Filter

high = 13/(1000/2)
low = 500/(1000/2)
b, a = sp.signal.butter(4, [high,low], btype='bandpass', analog=True)

df130PP_5_S1['BF Filtered'] = sp.signal.filtfilt(b, a, df130PP_5_S1['BF EMG (Offset)'])
df150PP_5_S1['BF Filtered'] = sp.signal.filtfilt(b, a, df150PP_5_S1['BF EMG (Offset)'])

df_SICI_70_130_5_S1['BF Filtered'] = sp.signal.filtfilt(b, a, df_SICI_70_130_5_S1['BF EMG (Offset)'])
df_SICI_70_150_5_S1['BF Filtered'] = sp.signal.filtfilt(b, a, df_SICI_70_150_5_S1['BF EMG (Offset)'])
df_SICI_80_130_5_S1['BF Filtered'] = sp.signal.filtfilt(b, a, df_SICI_80_130_5_S1['BF EMG (Offset)'])
df_SICI_80_150_5_S1['BF Filtered'] = sp.signal.filtfilt(b, a, df_SICI_80_150_5_S1['BF EMG (Offset)'])

df_ICF_70_130_5_S1['BF Filtered'] = sp.signal.filtfilt(b, a, df_ICF_70_130_5_S1['BF EMG (Offset)'])
df_ICF_70_150_5_S1['BF Filtered'] = sp.signal.filtfilt(b, a, df_ICF_70_150_5_S1['BF EMG (Offset)'])
df_ICF_80_130_5_S1['BF Filtered'] = sp.signal.filtfilt(b, a, df_ICF_80_130_5_S1['BF EMG (Offset)'])
df_ICF_80_150_5_S1['BF Filtered'] = sp.signal.filtfilt(b, a, df_ICF_80_150_5_S1['BF EMG (Offset)'])

#%% Append MVC

df130PP_5_S1['MVC'] =  mmax_S1
df150PP_5_S1['MVC'] =  mmax_S1

df_ICF_70_130_5_S1['MVC'] =  mmax_S1
df_ICF_70_150_5_S1['MVC'] =  mmax_S1
df_ICF_80_130_5_S1['MVC'] =  mmax_S1
df_ICF_80_150_5_S1['MVC'] =  mmax_S1

df_ICF_70_130_5_S1['MVC'] =  mmax_S1
df_ICF_70_150_5_S1['MVC'] =  mmax_S1
df_ICF_80_130_5_S1['MVC'] =  mmax_S1
df_ICF_80_150_5_S1['MVC'] =  mmax_S1

#%% Write to csv

df130PP_5_S1.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/ECCdf130PP_5_S1.csv')
df150PP_5_S1.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/ECCdf150PP_5_S1.csv')

df_SICI_70_130_5_S1.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/ECCdf_SICI_70_130_5_S1.csv')
df_SICI_70_150_5_S1.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/ECCdf_SICI_70_150_5_S1.csv')
df_SICI_80_130_5_S1.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/ECCdf_SICI_80_130_5_S1.csv')
df_SICI_80_150_5_S1.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/df_SICI_80_150_5_S1.csv')

df_ICF_70_130_5_S1.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/ECCdf_ICF_70_130_5_S1.csv')
df_ICF_70_150_5_S1.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/ECCdf_ICF_70_150_5_S1.csv')
df_ICF_80_130_5_S1.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/ECCdf_ICF_80_130_5_S1.csv')
df_ICF_80_150_5_S1.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/ECCdf_ICF_80_150_5_S1.csv')

#%%*************************************************************************************************************************%%#
#%% Session 1 10% 

os.chdir('C:/Users/cleed/Desktop/Data/Participant 01/PP/Session 1/TMS/10/Ecc')

df130PP_10_S1 = pd.concat([pd.read_csv(file110, skiprows = 23) for file110 in glob.glob('01_AMT 130%*.csv')], ignore_index = True)
df150PP_10_S1 = pd.concat([pd.read_csv(file120, skiprows = 23) for file120 in glob.glob('01_AMT 150%*.csv')], ignore_index = True)
df_SICI_70_130_10_S1 = pd.concat([pd.read_csv(file70130, skiprows = 23) for file70130 in glob.glob('01_SICI 70 130*.csv')], ignore_index = True)
df_SICI_70_150_10_S1 = pd.concat([pd.read_csv(file70150, skiprows = 23) for file70150 in glob.glob('01_SICI 70 150*.csv')], ignore_index = True)
df_SICI_80_130_10_S1 = pd.concat([pd.read_csv(file80130, skiprows = 23) for file80130 in glob.glob('01_SICI 70 130*.csv')], ignore_index = True)
df_SICI_80_150_10_S1 = pd.concat([pd.read_csv(file80150, skiprows = 23) for file80150 in glob.glob('01_SICI 70 150*.csv')], ignore_index = True)
df_ICF_70_130_10_S1 = pd.concat([pd.read_csv(file70130, skiprows = 23) for file70130 in glob.glob('01_ICF 70 130*.csv')], ignore_index = True)
df_ICF_70_150_10_S1 = pd.concat([pd.read_csv(file70150, skiprows = 23) for file70150 in glob.glob('01_ICF 70 150*.csv')], ignore_index = True)
df_ICF_80_130_10_S1 = pd.concat([pd.read_csv(file80130, skiprows = 23) for file80130 in glob.glob('01_ICF 70 130*.csv')], ignore_index = True)
df_ICF_80_150_10_S1 = pd.concat([pd.read_csv(file80150, skiprows = 23) for file80150 in glob.glob('01_ICF 70 150*.csv')], ignore_index = True)


#%% Get the Data we Need and Filter by Position

df130PP_10_S1 = df130PP_10_S1[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df130PP_10_S1 = df130PP_10_S1.ffill()
df130PP_10_S1 = df130PP_10_S1.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df130PP_10_S1 = df130PP_10_S1.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df150PP_10_S1 = df150PP_10_S1[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df150PP_10_S1 = df150PP_10_S1.ffill()
df150PP_10_S1 = df150PP_10_S1.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df150PP_10_S1 = df150PP_10_S1.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_SICI_70_130_10_S1 = df_SICI_70_130_10_S1[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_SICI_70_130_10_S1 = df_SICI_70_130_10_S1.ffill()
df_SICI_70_130_10_S1 = df_SICI_70_130_10_S1.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_SICI_70_130_10_S1 = df_SICI_70_130_10_S1.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_SICI_70_150_10_S1 = df_SICI_70_150_10_S1[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_SICI_70_150_10_S1 = df_SICI_70_150_10_S1.ffill()
df_SICI_70_150_10_S1 = df_SICI_70_150_10_S1.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_SICI_70_150_10_S1 = df_SICI_70_150_10_S1.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_SICI_80_130_10_S1 = df_SICI_80_130_10_S1[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_SICI_80_130_10_S1 = df_SICI_80_130_10_S1.ffill()
df_SICI_80_130_10_S1 = df_SICI_80_130_10_S1.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_SICI_80_130_10_S1 = df_SICI_80_130_10_S1.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_SICI_80_150_10_S1 = df_SICI_80_150_10_S1[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_SICI_80_150_10_S1 = df_SICI_80_150_10_S1.ffill()
df_SICI_80_150_10_S1 = df_SICI_80_150_10_S1.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_SICI_80_150_10_S1 = df_SICI_80_150_10_S1.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_ICF_70_130_10_S1 = df_ICF_70_130_10_S1[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_ICF_70_130_10_S1 = df_ICF_70_130_10_S1.ffill()
df_ICF_70_130_10_S1 = df_ICF_70_130_10_S1.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_ICF_70_130_10_S1 = df_ICF_70_130_10_S1.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_ICF_70_150_10_S1 = df_ICF_70_150_10_S1[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_ICF_70_150_10_S1 = df_ICF_70_150_10_S1.ffill()
df_ICF_70_150_10_S1 = df_ICF_70_150_10_S1.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_ICF_70_150_10_S1 = df_ICF_70_150_10_S1.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_ICF_80_130_10_S1 = df_ICF_80_130_10_S1[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_ICF_80_130_10_S1 = df_ICF_80_130_10_S1.ffill()
df_ICF_80_130_10_S1 = df_ICF_80_130_10_S1.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_ICF_80_130_10_S1 = df_ICF_80_130_10_S1.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_ICF_80_150_10_S1 = df_ICF_80_150_10_S1[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_ICF_80_150_10_S1 = df_ICF_80_150_10_S1.ffill()
df_ICF_80_150_10_S1 = df_ICF_80_150_10_S1.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_ICF_80_150_10_S1 = df_ICF_80_150_10_S1.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

#%% Account for EMG Offset

df130PP_10_S1['BF EMG (Offset)'] = df130PP_10_S1['BF EMG (Trigger)'] - np.mean(df130PP_10_S1['BF EMG (Trigger)'])
df150PP_10_S1['BF EMG (Offset)'] = df150PP_10_S1['BF EMG (Trigger)'] - np.mean(df150PP_10_S1['BF EMG (Trigger)'])

df_SICI_70_130_10_S1['BF EMG (Offset)'] = df_SICI_70_130_10_S1['BF EMG (Trigger)'] - np.mean(df_ICF_70_130_10_S1['BF EMG (Trigger)'])
df_SICI_70_150_10_S1['BF EMG (Offset)'] = df_SICI_70_150_10_S1['BF EMG (Trigger)'] - np.mean(df_ICF_70_150_10_S1['BF EMG (Trigger)'])
df_SICI_80_130_10_S1['BF EMG (Offset)'] = df_SICI_80_130_10_S1['BF EMG (Trigger)'] - np.mean(df_ICF_80_130_10_S1['BF EMG (Trigger)'])
df_SICI_80_150_10_S1['BF EMG (Offset)'] = df_SICI_80_150_10_S1['BF EMG (Trigger)'] - np.mean(df_SICI_80_150_10_S1['BF EMG (Trigger)'])

df_ICF_70_130_10_S1['BF EMG (Offset)'] = df_ICF_70_130_10_S1['BF EMG (Trigger)'] - np.mean(df_ICF_70_130_10_S1['BF EMG (Trigger)'])
df_ICF_70_150_10_S1['BF EMG (Offset)'] = df_ICF_70_150_10_S1['BF EMG (Trigger)'] - np.mean(df_ICF_70_150_10_S1['BF EMG (Trigger)'])
df_ICF_80_130_10_S1['BF EMG (Offset)'] = df_ICF_80_130_10_S1['BF EMG (Trigger)'] - np.mean(df_ICF_80_130_10_S1['BF EMG (Trigger)'])
df_ICF_80_150_10_S1['BF EMG (Offset)'] = df_ICF_80_150_10_S1['BF EMG (Trigger)'] - np.mean(df_ICF_80_150_10_S1['BF EMG (Trigger)'])

#%% Build and Apply Filter

high = 13/(1000/2)
low = 500/(1000/2)
b, a = sp.signal.butter(4, [high,low], btype='bandpass', analog=True)

df130PP_10_S1['BF Filtered'] = sp.signal.filtfilt(b, a, df130PP_10_S1['BF EMG (Offset)'])
df150PP_10_S1['BF Filtered'] = sp.signal.filtfilt(b, a, df150PP_10_S1['BF EMG (Offset)'])

df_SICI_70_130_10_S1['BF Filtered'] = sp.signal.filtfilt(b, a, df_SICI_70_130_10_S1['BF EMG (Offset)'])
df_SICI_70_150_10_S1['BF Filtered'] = sp.signal.filtfilt(b, a, df_SICI_70_150_10_S1['BF EMG (Offset)'])
df_SICI_80_130_10_S1['BF Filtered'] = sp.signal.filtfilt(b, a, df_SICI_80_130_10_S1['BF EMG (Offset)'])
df_SICI_80_150_10_S1['BF Filtered'] = sp.signal.filtfilt(b, a, df_SICI_80_150_10_S1['BF EMG (Offset)'])

df_ICF_70_130_10_S1['BF Filtered'] = sp.signal.filtfilt(b, a, df_ICF_70_130_10_S1['BF EMG (Offset)'])
df_ICF_70_150_10_S1['BF Filtered'] = sp.signal.filtfilt(b, a, df_ICF_70_150_10_S1['BF EMG (Offset)'])
df_ICF_80_130_10_S1['BF Filtered'] = sp.signal.filtfilt(b, a, df_ICF_80_130_10_S1['BF EMG (Offset)'])
df_ICF_80_150_10_S1['BF Filtered'] = sp.signal.filtfilt(b, a, df_ICF_80_150_10_S1['BF EMG (Offset)'])

#%% Append MVC

df130PP_10_S1['MVC'] =  mmax_S1
df150PP_10_S1['MVC'] =  mmax_S1

df_ICF_70_130_10_S1['MVC'] =  mmax_S1
df_ICF_70_150_10_S1['MVC'] =  mmax_S1
df_ICF_80_130_10_S1['MVC'] =  mmax_S1
df_ICF_80_150_10_S1['MVC'] =  mmax_S1

df_ICF_70_130_10_S1['MVC'] =  mmax_S1
df_ICF_70_150_10_S1['MVC'] =  mmax_S1
df_ICF_80_130_10_S1['MVC'] =  mmax_S1
df_ICF_80_150_10_S1['MVC'] =  mmax_S1

#%% Write to csv

df130PP_10_S1.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/ECCdf130PP_10_S1.csv')
df150PP_10_S1.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/ECCdf150PP_10_S1.csv')

df_SICI_70_130_10_S1.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/ECCdf_SICI_70_130_10_S1.csv')
df_SICI_70_150_10_S1.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/ECCdf_SICI_70_150_10_S1.csv')
df_SICI_80_130_10_S1.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/ECCdf_SICI_80_130_10_S1.csv')
df_SICI_80_150_10_S1.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/ECCdf_SICI_80_150_10_S1.csv')

df_ICF_70_130_10_S1.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/ECCdf_ICF_70_130_10_S1.csv')
df_ICF_70_150_10_S1.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/ECCdf_ICF_70_150_10_S1.csv')
df_ICF_80_130_10_S1.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/ECCdf_ICF_80_130_10_S1.csv')
df_ICF_80_150_10_S1.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/ECCdf_ICF_80_150_10_S1.csv')

#%%*************************************************************************************************************************%%#
#%% Session 2

os.chdir('C:/Users/cleed/Desktop/Data/Participant 01/PP/Session 2/TMS/5/Ecc')

df130PP_5_S2 = pd.concat([pd.read_csv(file110, skiprows = 23) for file110 in glob.glob('01_AMT 130%*.csv')], ignore_index = True)
df150PP_5_S2 = pd.concat([pd.read_csv(file120, skiprows = 23) for file120 in glob.glob('01_AMT 150%*.csv')], ignore_index = True)
df_SICI_70_130_5_S2 = pd.concat([pd.read_csv(file70130, skiprows = 23) for file70130 in glob.glob('01_SICI 70 130*.csv')], ignore_index = True)
df_SICI_70_150_5_S2 = pd.concat([pd.read_csv(file70150, skiprows = 23) for file70150 in glob.glob('01_SICI 70 150*.csv')], ignore_index = True)
df_SICI_80_130_5_S2 = pd.concat([pd.read_csv(file80130, skiprows = 23) for file80130 in glob.glob('01_SICI 70 130*.csv')], ignore_index = True)
df_SICI_80_150_5_S2 = pd.concat([pd.read_csv(file80150, skiprows = 23) for file80150 in glob.glob('01_SICI 70 150*.csv')], ignore_index = True)
df_ICF_70_130_5_S2 = pd.concat([pd.read_csv(file70130, skiprows = 23) for file70130 in glob.glob('01_ICF 70 130*.csv')], ignore_index = True)
df_ICF_70_150_5_S2 = pd.concat([pd.read_csv(file70150, skiprows = 23) for file70150 in glob.glob('01_ICF 70 150*.csv')], ignore_index = True)
df_ICF_80_130_5_S2 = pd.concat([pd.read_csv(file80130, skiprows = 23) for file80130 in glob.glob('01_ICF 70 130*.csv')], ignore_index = True)
df_ICF_80_150_5_S2 = pd.concat([pd.read_csv(file80150, skiprows = 23) for file80150 in glob.glob('01_ICF 70 150*.csv')], ignore_index = True)

#%% Get MVC

os.chdir('C:/Users/cleed/Desktop/Data/Participant 01/PP/Session 2/Strength')

dfmvc_S2 = pd.concat([pd.read_csv(mvc, skiprows = 23) for mvc in glob.glob('01_Hamstring_MVC*.csv')], ignore_index = True)
mmax_S2 = dfmvc_S2['Torque'].min() * -1

#%% Get the Data we Need and Filter by Position

df130PP_5_S2 = df130PP_5_S2[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df130PP_5_S2 = df130PP_5_S2.ffill()
df130PP_5_S2 = df130PP_5_S2.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df130PP_5_S2 = df130PP_5_S2.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df150PP_5_S2 = df150PP_5_S2[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df150PP_5_S2 = df150PP_5_S2.ffill()
df150PP_5_S2 = df150PP_5_S2.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df150PP_5_S2 = df150PP_5_S2.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_SICI_70_130_5_S2 = df_SICI_70_130_5_S2[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_SICI_70_130_5_S2 = df_SICI_70_130_5_S2.ffill()
df_SICI_70_130_5_S2 = df_SICI_70_130_5_S2.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_SICI_70_130_5_S2 = df_SICI_70_130_5_S2.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_SICI_70_150_5_S2 = df_SICI_70_150_5_S2[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_SICI_70_150_5_S2 = df_SICI_70_150_5_S2.ffill()
df_SICI_70_150_5_S2 = df_SICI_70_150_5_S2.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_SICI_70_150_5_S2 = df_SICI_70_150_5_S2.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_SICI_80_130_5_S2 = df_SICI_80_130_5_S2[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_SICI_80_130_5_S2 = df_SICI_80_130_5_S2.ffill()
df_SICI_80_130_5_S2 = df_SICI_80_130_5_S2.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_SICI_80_130_5_S2 = df_SICI_80_130_5_S2.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_SICI_80_150_5_S2 = df_SICI_80_150_5_S2[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_SICI_80_150_5_S2 = df_SICI_80_150_5_S2.ffill()
df_SICI_80_150_5_S2 = df_SICI_80_150_5_S2.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_SICI_80_150_5_S2 = df_SICI_80_150_5_S2.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_ICF_70_130_5_S2 = df_ICF_70_130_5_S2[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_ICF_70_130_5_S2 = df_ICF_70_130_5_S2.ffill()
df_ICF_70_130_5_S2 = df_ICF_70_130_5_S2.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_ICF_70_130_5_S2 = df_ICF_70_130_5_S2.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_ICF_70_150_5_S2 = df_ICF_70_150_5_S2[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_ICF_70_150_5_S2 = df_ICF_70_150_5_S2.ffill()
df_ICF_70_150_5_S2 = df_ICF_70_150_5_S2.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_ICF_70_150_5_S2 = df_ICF_70_150_5_S2.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_ICF_80_130_5_S2 = df_ICF_80_130_5_S2[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_ICF_80_130_5_S2 = df_ICF_80_130_5_S2.ffill()
df_ICF_80_130_5_S2 = df_ICF_80_130_5_S2.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_ICF_80_130_5_S2 = df_ICF_80_130_5_S2.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_ICF_80_150_5_S2 = df_ICF_80_150_5_S2[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_ICF_80_150_5_S2 = df_ICF_80_150_5_S2.ffill()
df_ICF_80_150_5_S2 = df_ICF_80_150_5_S2.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_ICF_80_150_5_S2 = df_ICF_80_150_5_S2.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

#%% Account for EMG Offset

df130PP_5_S2['BF EMG (Offset)'] = df130PP_5_S2['BF EMG (Trigger)'] - np.mean(df130PP_5_S2['BF EMG (Trigger)'])
df150PP_5_S2['BF EMG (Offset)'] = df150PP_5_S2['BF EMG (Trigger)'] - np.mean(df150PP_5_S2['BF EMG (Trigger)'])

df_SICI_70_130_5_S2['BF EMG (Offset)'] = df_SICI_70_130_5_S2['BF EMG (Trigger)'] - np.mean(df_ICF_70_130_5_S2['BF EMG (Trigger)'])
df_SICI_70_150_5_S2['BF EMG (Offset)'] = df_SICI_70_150_5_S2['BF EMG (Trigger)'] - np.mean(df_ICF_70_150_5_S2['BF EMG (Trigger)'])
df_SICI_80_130_5_S2['BF EMG (Offset)'] = df_SICI_80_130_5_S2['BF EMG (Trigger)'] - np.mean(df_ICF_80_130_5_S2['BF EMG (Trigger)'])
df_SICI_80_150_5_S2['BF EMG (Offset)'] = df_SICI_80_150_5_S2['BF EMG (Trigger)'] - np.mean(df_SICI_80_150_5_S2['BF EMG (Trigger)'])

df_ICF_70_130_5_S2['BF EMG (Offset)'] = df_ICF_70_130_5_S2['BF EMG (Trigger)'] - np.mean(df_ICF_70_130_5_S2['BF EMG (Trigger)'])
df_ICF_70_150_5_S2['BF EMG (Offset)'] = df_ICF_70_150_5_S2['BF EMG (Trigger)'] - np.mean(df_ICF_70_150_5_S2['BF EMG (Trigger)'])
df_ICF_80_130_5_S2['BF EMG (Offset)'] = df_ICF_80_130_5_S2['BF EMG (Trigger)'] - np.mean(df_ICF_80_130_5_S2['BF EMG (Trigger)'])
df_ICF_80_150_5_S2['BF EMG (Offset)'] = df_ICF_80_150_5_S2['BF EMG (Trigger)'] - np.mean(df_ICF_80_150_5_S2['BF EMG (Trigger)'])

#%% Build and Apply Filter

high = 13/(1000/2)
low = 500/(1000/2)
b, a = sp.signal.butter(4, [high,low], btype='bandpass', analog=True)

df130PP_5_S2['BF Filtered'] = sp.signal.filtfilt(b, a, df130PP_5_S2['BF EMG (Offset)'])
df150PP_5_S2['BF Filtered'] = sp.signal.filtfilt(b, a, df150PP_5_S2['BF EMG (Offset)'])

df_SICI_70_130_5_S2['BF Filtered'] = sp.signal.filtfilt(b, a, df_SICI_70_130_5_S2['BF EMG (Offset)'])
df_SICI_70_150_5_S2['BF Filtered'] = sp.signal.filtfilt(b, a, df_SICI_70_150_5_S2['BF EMG (Offset)'])
df_SICI_80_130_5_S2['BF Filtered'] = sp.signal.filtfilt(b, a, df_SICI_80_130_5_S2['BF EMG (Offset)'])
df_SICI_80_150_5_S2['BF Filtered'] = sp.signal.filtfilt(b, a, df_SICI_80_150_5_S2['BF EMG (Offset)'])

df_ICF_70_130_5_S2['BF Filtered'] = sp.signal.filtfilt(b, a, df_ICF_70_130_5_S2['BF EMG (Offset)'])
df_ICF_70_150_5_S2['BF Filtered'] = sp.signal.filtfilt(b, a, df_ICF_70_150_5_S2['BF EMG (Offset)'])
df_ICF_80_130_5_S2['BF Filtered'] = sp.signal.filtfilt(b, a, df_ICF_80_130_5_S2['BF EMG (Offset)'])
df_ICF_80_150_5_S2['BF Filtered'] = sp.signal.filtfilt(b, a, df_ICF_80_150_5_S2['BF EMG (Offset)'])

#%% Append MVC

df130PP_5_S2['MVC'] =  mmax_S2
df150PP_5_S2['MVC'] =  mmax_S2

df_ICF_70_130_5_S2['MVC'] =  mmax_S2
df_ICF_70_150_5_S2['MVC'] =  mmax_S2
df_ICF_80_130_5_S2['MVC'] =  mmax_S2
df_ICF_80_150_5_S2['MVC'] =  mmax_S2

df_ICF_70_130_5_S2['MVC'] =  mmax_S2
df_ICF_70_150_5_S2['MVC'] =  mmax_S2
df_ICF_80_130_5_S2['MVC'] =  mmax_S2
df_ICF_80_150_5_S2['MVC'] =  mmax_S2

#%% Write to csv

df130PP_5_S2.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/ECCdf130PP_5_S2.csv')
df150PP_5_S2.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/ECCdf150PP_5_S2.csv')

df_SICI_70_130_5_S2.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/ECCdf_SICI_70_130_5_S2.csv')
df_SICI_70_150_5_S2.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/ECCdf_SICI_70_150_5_S2.csv')
df_SICI_80_130_5_S2.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/ECCdf_SICI_80_130_5_S2.csv')
df_SICI_80_150_5_S2.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/ECCdf_SICI_80_150_5_S2.csv')

df_ICF_70_130_5_S2.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/ECCdf_ICF_70_130_5_S2.csv')
df_ICF_70_150_5_S2.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/ECCdf_ICF_70_150_5_S2.csv')
df_ICF_80_130_5_S2.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/ECCdf_ICF_80_130_5_S2.csv')
df_ICF_80_150_5_S2.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/ECCdf_ICF_80_150_5_S2.csv')

#%%*************************************************************************************************************************%%#
#%% Sessions 2 10%

os.chdir('C:/Users/cleed/Desktop/Data/Participant 01/PP/Session 2/TMS/10/Ecc')

df130PP_10_S2 = pd.concat([pd.read_csv(file110, skiprows = 23) for file110 in glob.glob('01_AMT 130%*.csv')], ignore_index = True)
df150PP_10_S2 = pd.concat([pd.read_csv(file120, skiprows = 23) for file120 in glob.glob('01_AMT 150%*.csv')], ignore_index = True)
df_SICI_70_130_10_S2 = pd.concat([pd.read_csv(file70130, skiprows = 23) for file70130 in glob.glob('01_SICI 70 130*.csv')], ignore_index = True)
df_SICI_70_150_10_S2 = pd.concat([pd.read_csv(file70150, skiprows = 23) for file70150 in glob.glob('01_SICI 70 150*.csv')], ignore_index = True)
df_SICI_80_130_10_S2 = pd.concat([pd.read_csv(file80130, skiprows = 23) for file80130 in glob.glob('01_SICI 70 130*.csv')], ignore_index = True)
df_SICI_80_150_10_S2 = pd.concat([pd.read_csv(file80150, skiprows = 23) for file80150 in glob.glob('01_SICI 70 150*.csv')], ignore_index = True)
df_ICF_70_130_10_S2 = pd.concat([pd.read_csv(file70130, skiprows = 23) for file70130 in glob.glob('01_ICF 70 130*.csv')], ignore_index = True)
df_ICF_70_150_10_S2 = pd.concat([pd.read_csv(file70150, skiprows = 23) for file70150 in glob.glob('01_ICF 70 150*.csv')], ignore_index = True)
df_ICF_80_130_10_S2 = pd.concat([pd.read_csv(file80130, skiprows = 23) for file80130 in glob.glob('01_ICF 70 130*.csv')], ignore_index = True)
df_ICF_80_150_10_S2 = pd.concat([pd.read_csv(file80150, skiprows = 23) for file80150 in glob.glob('01_ICF 70 150*.csv')], ignore_index = True)

#%% Get the Data we Need and Filter by Position

df130PP_10_S2 = df130PP_10_S2[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df130PP_10_S2 = df130PP_10_S2.ffill()
df130PP_10_S2 = df130PP_10_S2.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df130PP_10_S2 = df130PP_10_S2.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df150PP_10_S2 = df150PP_10_S2[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df150PP_10_S2 = df150PP_10_S2.ffill()
df150PP_10_S2 = df150PP_10_S2.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df150PP_10_S2 = df150PP_10_S2.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_SICI_70_130_10_S2 = df_SICI_70_130_10_S2[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_SICI_70_130_10_S2 = df_SICI_70_130_10_S2.ffill()
df_SICI_70_130_10_S2 = df_SICI_70_130_10_S2.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_SICI_70_130_10_S2 = df_SICI_70_130_10_S2.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_SICI_70_150_10_S2 = df_SICI_70_150_10_S2[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_SICI_70_150_10_S2 = df_SICI_70_150_10_S2.ffill()
df_SICI_70_150_10_S2 = df_SICI_70_150_10_S2.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_SICI_70_150_10_S2 = df_SICI_70_150_10_S2.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_SICI_80_130_10_S2 = df_SICI_80_130_10_S2[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_SICI_80_130_10_S2 = df_SICI_80_130_10_S2.ffill()
df_SICI_80_130_10_S2 = df_SICI_80_130_10_S2.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_SICI_80_130_10_S2 = df_SICI_80_130_10_S2.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_SICI_80_150_10_S2 = df_SICI_80_150_10_S2[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_SICI_80_150_10_S2 = df_SICI_80_150_10_S2.ffill()
df_SICI_80_150_10_S2 = df_SICI_80_150_10_S2.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_SICI_80_150_10_S2 = df_SICI_80_150_10_S2.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_ICF_70_130_10_S2 = df_ICF_70_130_10_S2[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_ICF_70_130_10_S2 = df_ICF_70_130_10_S2.ffill()
df_ICF_70_130_10_S2 = df_ICF_70_130_10_S2.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_ICF_70_130_10_S2 = df_ICF_70_130_10_S2.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_ICF_70_150_10_S2 = df_ICF_70_150_10_S2[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_ICF_70_150_10_S2 = df_ICF_70_150_10_S2.ffill()
df_ICF_70_150_10_S2 = df_ICF_70_150_10_S2.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_ICF_70_150_10_S2 = df_ICF_70_150_10_S2.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_ICF_80_130_10_S2 = df_ICF_80_130_10_S2[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_ICF_80_130_10_S2 = df_ICF_80_130_10_S2.ffill()
df_ICF_80_130_10_S2 = df_ICF_80_130_10_S2.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_ICF_80_130_10_S2 = df_ICF_80_130_10_S2.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df_ICF_80_150_10_S2 = df_ICF_80_150_10_S2[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df_ICF_80_150_10_S2 = df_ICF_80_150_10_S2.ffill()
df_ICF_80_150_10_S2 = df_ICF_80_150_10_S2.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df_ICF_80_150_10_S2 = df_ICF_80_150_10_S2.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

#%% Account for EMG Offset

df130PP_10_S2['BF EMG (Offset)'] = df130PP_10_S2['BF EMG (Trigger)'] - np.mean(df130PP_10_S2['BF EMG (Trigger)'])
df150PP_10_S2['BF EMG (Offset)'] = df150PP_10_S2['BF EMG (Trigger)'] - np.mean(df150PP_10_S2['BF EMG (Trigger)'])

df_SICI_70_130_10_S2['BF EMG (Offset)'] = df_SICI_70_130_10_S2['BF EMG (Trigger)'] - np.mean(df_ICF_70_130_10_S2['BF EMG (Trigger)'])
df_SICI_70_150_10_S2['BF EMG (Offset)'] = df_SICI_70_150_10_S2['BF EMG (Trigger)'] - np.mean(df_ICF_70_150_10_S2['BF EMG (Trigger)'])
df_SICI_80_130_10_S2['BF EMG (Offset)'] = df_SICI_80_130_10_S2['BF EMG (Trigger)'] - np.mean(df_ICF_80_130_10_S2['BF EMG (Trigger)'])
df_SICI_80_150_10_S2['BF EMG (Offset)'] = df_SICI_80_150_10_S2['BF EMG (Trigger)'] - np.mean(df_SICI_80_150_10_S2['BF EMG (Trigger)'])

df_ICF_70_130_10_S2['BF EMG (Offset)'] = df_ICF_70_130_10_S2['BF EMG (Trigger)'] - np.mean(df_ICF_70_130_10_S2['BF EMG (Trigger)'])
df_ICF_70_150_10_S2['BF EMG (Offset)'] = df_ICF_70_150_10_S2['BF EMG (Trigger)'] - np.mean(df_ICF_70_150_10_S2['BF EMG (Trigger)'])
df_ICF_80_130_10_S2['BF EMG (Offset)'] = df_ICF_80_130_10_S2['BF EMG (Trigger)'] - np.mean(df_ICF_80_130_10_S2['BF EMG (Trigger)'])
df_ICF_80_150_10_S2['BF EMG (Offset)'] = df_ICF_80_150_10_S2['BF EMG (Trigger)'] - np.mean(df_ICF_80_150_10_S2['BF EMG (Trigger)'])

#%% Build and Apply Filter

high = 13/(1000/2)
low = 500/(1000/2)
b, a = sp.signal.butter(4, [high,low], btype='bandpass', analog=True)

df130PP_10_S2['BF Filtered'] = sp.signal.filtfilt(b, a, df130PP_10_S2['BF EMG (Offset)'])
df150PP_10_S2['BF Filtered'] = sp.signal.filtfilt(b, a, df150PP_10_S2['BF EMG (Offset)'])

df_SICI_70_130_10_S2['BF Filtered'] = sp.signal.filtfilt(b, a, df_SICI_70_130_10_S2['BF EMG (Offset)'])
df_SICI_70_150_10_S2['BF Filtered'] = sp.signal.filtfilt(b, a, df_SICI_70_150_10_S2['BF EMG (Offset)'])
df_SICI_80_130_10_S2['BF Filtered'] = sp.signal.filtfilt(b, a, df_SICI_80_130_10_S2['BF EMG (Offset)'])
df_SICI_80_150_10_S2['BF Filtered'] = sp.signal.filtfilt(b, a, df_SICI_80_150_10_S2['BF EMG (Offset)'])

df_ICF_70_130_10_S2['BF Filtered'] = sp.signal.filtfilt(b, a, df_ICF_70_130_10_S2['BF EMG (Offset)'])
df_ICF_70_150_10_S2['BF Filtered'] = sp.signal.filtfilt(b, a, df_ICF_70_150_10_S2['BF EMG (Offset)'])
df_ICF_80_130_10_S2['BF Filtered'] = sp.signal.filtfilt(b, a, df_ICF_80_130_10_S2['BF EMG (Offset)'])
df_ICF_80_150_10_S2['BF Filtered'] = sp.signal.filtfilt(b, a, df_ICF_80_150_10_S2['BF EMG (Offset)'])

#%% Append MVC

df130PP_10_S2['MVC'] =  mmax_S2
df150PP_10_S2['MVC'] =  mmax_S2

df_ICF_70_130_10_S2['MVC'] =  mmax_S2
df_ICF_70_150_10_S2['MVC'] =  mmax_S2
df_ICF_80_130_10_S2['MVC'] =  mmax_S2
df_ICF_80_150_10_S2['MVC'] =  mmax_S2

df_ICF_70_130_10_S2['MVC'] =  mmax_S2
df_ICF_70_150_10_S2['MVC'] =  mmax_S2
df_ICF_80_130_10_S2['MVC'] =  mmax_S2
df_ICF_80_150_10_S2['MVC'] =  mmax_S2

#%% Write to csv

df130PP_10_S2.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/ECCdf130PP_10_S2.csv')
df150PP_10_S2.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/ECCdf150PP_10_S2.csv')

df_SICI_70_130_10_S2.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/ECCdf_SICI_70_130_10_S2.csv')
df_SICI_70_150_10_S2.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/ECCdf_SICI_70_150_10_S2.csv')
df_SICI_80_130_10_S2.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/ECCdf_SICI_80_130_10_S2.csv')
df_SICI_80_150_10_S2.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/ECCdf_SICI_80_150_10_S2.csv')

df_ICF_70_130_10_S2.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/ECCdf_ICF_70_130_10_S2.csv')
df_ICF_70_150_10_S2.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/ECCdf_ICF_70_150_10_S2.csv')
df_ICF_80_130_10_S2.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/ECCdf_ICF_80_130_10_S2.csv')
df_ICF_80_150_10_S2.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/PP/ECCdf_ICF_80_150_10_S2.csv')







