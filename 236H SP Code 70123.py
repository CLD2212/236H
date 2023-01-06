# Import libraries

import glob
import pandas as pd
import numpy as np
import scipy as sp
import sys
import os

#%% Set Working directory, Import all files and create dfs

os.chdir('C:/Users/cleed/Desktop/Data/Participant 01/SP/Session 1/TMS/5/Iso')

df110_5_S1 = pd.concat([pd.read_csv(file110, skiprows = 23) for file110 in glob.glob('01_AMT 110%*.csv')], ignore_index = True)
df120_5_S1 = pd.concat([pd.read_csv(file120, skiprows = 23) for file120 in glob.glob('01_AMT 120%*.csv')], ignore_index = True)
df130_5_S1 = pd.concat([pd.read_csv(file130, skiprows = 23) for file130 in glob.glob('01_AMT 130%*.csv')], ignore_index = True)
df150_5_S1 = pd.concat([pd.read_csv(file150, skiprows = 23) for file150 in glob.glob('01_AMT 150%*.csv')], ignore_index = True)
df170_5_S1 = pd.concat([pd.read_csv(file170, skiprows = 23) for file170 in glob.glob('01_AMT 170%*.csv')], ignore_index = True)

#%% Get S1 MVC

os.chdir('C:/Users/cleed/Desktop/Data/Participant 01/SP/Session 1/Strength')

dfmvc_S1 = pd.concat([pd.read_csv(mvc, skiprows = 23) for mvc in glob.glob('01_Hamstring_MVC*.csv')], ignore_index = True)
mmax_S1 = dfmvc_S1['Torque'].min() * -1

#%% Get the Data we Need and Filter by Position

df110_5_S1 = df110_5_S1[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df110_5_S1 = df110_5_S1.ffill()
df110_5_S1 = df110_5_S1.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df110_5_S1 = df110_5_S1.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df120_5_S1 = df120_5_S1[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df120_5_S1 = df120_5_S1.ffill()
df120_5_S1 = df120_5_S1.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df120_5_S1 = df120_5_S1.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df130_5_S1 = df130_5_S1[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df130_5_S1 = df130_5_S1.ffill()
df130_5_S1 = df130_5_S1.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df130_5_S1 = df130_5_S1.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df150_5_S1 = df150_5_S1[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df130_5_S1 = df130_5_S1.ffill()
df150_5_S1 = df150_5_S1.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32")
#df150_5_S1 = df150_5_S1.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df170_5_S1 = df170_5_S1[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df170_5_S1 = df170_5_S1.ffill()
df170_5_S1 = df170_5_S1.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df170_5_S1 = df170_5_S1.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 


#%% Account for EMG Offset

df110_5_S1['BF EMG (Offset)'] = df110_5_S1['BF EMG (Trigger)'] - np.mean(df110_5_S1['BF EMG (Trigger)'])
df110_5_S1['MH EMG (Offset)'] = df110_5_S1['MH EMG (Trigger)'] - np.mean(df110_5_S1['MH EMG (Trigger)'])
df120_5_S1['BF EMG (Offset)'] = df120_5_S1['BF EMG (Trigger)'] - np.mean(df120_5_S1['BF EMG (Trigger)'])
df120_5_S1['MH EMG (Offset)'] = df120_5_S1['MH EMG (Trigger)'] - np.mean(df120_5_S1['MH EMG (Trigger)'])
df130_5_S1['BF EMG (Offset)'] = df130_5_S1['BF EMG (Trigger)'] - np.mean(df130_5_S1['BF EMG (Trigger)'])
df130_5_S1['MH EMG (Offset)'] = df130_5_S1['MH EMG (Trigger)'] - np.mean(df130_5_S1['MH EMG (Trigger)'])
df150_5_S1['BF EMG (Offset)'] = df150_5_S1['BF EMG (Trigger)'] - np.mean(df150_5_S1['BF EMG (Trigger)'])
df150_5_S1['MH EMG (Offset)'] = df150_5_S1['MH EMG (Trigger)'] - np.mean(df150_5_S1['MH EMG (Trigger)'])
df170_5_S1['BF EMG (Offset)'] = df170_5_S1['BF EMG (Trigger)'] - np.mean(df170_5_S1['BF EMG (Trigger)'])
df170_5_S1['MH EMG (Offset)'] = df170_5_S1['MH EMG (Trigger)'] - np.mean(df170_5_S1['MH EMG (Trigger)'])

#%% Build and Apply Filter

high = 13/(1000/2)
low = 500/(1000/2)
b, a = sp.signal.butter(4, [high,low], btype='bandpass', analog=True)

df110_5_S1['BF Filtered'] = sp.signal.filtfilt(b, a, df110_5_S1['BF EMG (Offset)'])
df110_5_S1['MH Filtered'] = sp.signal.filtfilt(b, a, df110_5_S1['MH EMG (Offset)'])
df120_5_S1['BF Filtered'] = sp.signal.filtfilt(b, a, df120_5_S1['BF EMG (Offset)'])
df120_5_S1['MH Filtered'] = sp.signal.filtfilt(b, a, df120_5_S1['MH EMG (Offset)'])
df130_5_S1['BF Filtered'] = sp.signal.filtfilt(b, a, df130_5_S1['BF EMG (Offset)'])
df130_5_S1['MH Filtered'] = sp.signal.filtfilt(b, a, df130_5_S1['MH EMG (Offset)'])
df150_5_S1['BF Filtered'] = sp.signal.filtfilt(b, a, df150_5_S1['BF EMG (Offset)'])
df150_5_S1['MH Filtered'] = sp.signal.filtfilt(b, a, df150_5_S1['MH EMG (Offset)'])
df170_5_S1['BF Filtered'] = sp.signal.filtfilt(b, a, df170_5_S1['BF EMG (Offset)'])
df170_5_S1['MH Filtered'] = sp.signal.filtfilt(b, a, df170_5_S1['MH EMG (Offset)'])

#%% Append MVC

df110_5_S1['MVC'] =  mmax_S1
df120_5_S1['MVC'] =  mmax_S1
df130_5_S1['MVC'] =  mmax_S1
df150_5_S1['MVC'] =  mmax_S1
df170_5_S1['MVC'] =  mmax_S1

#%% Descriptiors

alldes_5_S1 = ([['110', df110_5_S1.describe()], ['120', df120_5_S1.describe()], ['130', df130_5_S1.describe()],
           ['150', df150_5_S1.describe()], ['170', df170_5_S1.describe()]])
print([alldes_5_S1])

#%% Write to csv

df110_5_S1.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/df110_5_S1.csv')
df120_5_S1.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/df120_5_S1.csv')
df130_5_S1.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/df130_5_S1.csv')
df150_5_S1.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/df150_5_S1.csv')
df170_5_S1.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/df170_5_S1.csv')

#%%*************************************************************************************************************************%%#
#%% Session 1 10%

os.chdir('C:/Users/cleed/Desktop/Data/Participant 01/SP/Session 1/TMS/10/Iso')

df110_10_S1 = pd.concat([pd.read_csv(file110, skiprows = 23) for file110 in glob.glob('01_AMT 110%*.csv')], ignore_index = True)
df120_10_S1 = pd.concat([pd.read_csv(file120, skiprows = 23) for file120 in glob.glob('01_AMT 120%*.csv')], ignore_index = True)
df130_10_S1 = pd.concat([pd.read_csv(file130, skiprows = 23) for file130 in glob.glob('01_AMT 130%*.csv')], ignore_index = True)
df150_10_S1 = pd.concat([pd.read_csv(file150, skiprows = 23) for file150 in glob.glob('01_AMT 150%*.csv')], ignore_index = True)
df170_10_S1 = pd.concat([pd.read_csv(file170, skiprows = 23) for file170 in glob.glob('01_AMT 170%*.csv')], ignore_index = True)

#%% Get the Data we Need and Filter by Position

df110_10_S1 = df110_10_S1[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df110_10_S1 = df110_10_S1.ffill()
df110_10_S1 = df110_10_S1.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df110_10_S1 = df110_10_S1.query("`BF max rmsEMG (Trigger)` >= 0.7 and `BF max rmsEMG (Trigger)` <= 0.13") 

df120_10_S1 = df120_10_S1[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df120_10_S1 = df120_10_S1.ffill()
df120_10_S1 = df120_10_S1.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df120_10_S1 = df120_10_S1.query("`BF max rmsEMG (Trigger)` >= 0.7 and `BF max rmsEMG (Trigger)` <= 0.13") 

df130_10_S1 = df130_10_S1[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df130_5_S1 = df130_10_S1.ffill()
df130_10_S1 = df130_10_S1.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df130_10_S1 = df130_10_S1.query("`BF max rmsEMG (Trigger)` >= 0.7 and `BF max rmsEMG (Trigger)` <= 0.13")  

df150_10_S1 = df150_10_S1[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df130_10_S1 = df130_10_S1.ffill()
df150_10_S1 = df150_10_S1.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32")
#df150_10_S1 = df150_10_S1.query("`BF max rmsEMG (Trigger)` >= 0.7 and `BF max rmsEMG (Trigger)` <= 0.13") 

df170_10_S1 = df170_10_S1[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df170_10_S1 = df170_10_S1.ffill()
df170_10_S1 = df170_10_S1.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df170_10_S1 = df170_10_S1.query("`BF max rmsEMG (Trigger)` >= 0.7 and `BF max rmsEMG (Trigger)` <= 0.13") 


#%% Account for EMG Offset

df110_10_S1['BF EMG (Offset)'] = df110_10_S1['BF EMG (Trigger)'] - np.mean(df110_10_S1['BF EMG (Trigger)'])
df110_10_S1['MH EMG (Offset)'] = df110_10_S1['MH EMG (Trigger)'] - np.mean(df110_10_S1['MH EMG (Trigger)'])
df120_10_S1['BF EMG (Offset)'] = df120_10_S1['BF EMG (Trigger)'] - np.mean(df120_10_S1['BF EMG (Trigger)'])
df120_10_S1['MH EMG (Offset)'] = df120_10_S1['MH EMG (Trigger)'] - np.mean(df120_10_S1['MH EMG (Trigger)'])
df130_10_S1['BF EMG (Offset)'] = df130_10_S1['BF EMG (Trigger)'] - np.mean(df130_10_S1['BF EMG (Trigger)'])
df130_10_S1['MH EMG (Offset)'] = df130_10_S1['MH EMG (Trigger)'] - np.mean(df130_10_S1['MH EMG (Trigger)'])
df150_10_S1['BF EMG (Offset)'] = df150_10_S1['BF EMG (Trigger)'] - np.mean(df150_10_S1['BF EMG (Trigger)'])
df150_10_S1['MH EMG (Offset)'] = df150_10_S1['MH EMG (Trigger)'] - np.mean(df150_10_S1['MH EMG (Trigger)'])
df170_10_S1['BF EMG (Offset)'] = df170_10_S1['BF EMG (Trigger)'] - np.mean(df170_10_S1['BF EMG (Trigger)'])
df170_10_S1['MH EMG (Offset)'] = df170_10_S1['MH EMG (Trigger)'] - np.mean(df170_10_S1['MH EMG (Trigger)'])

#%% Build and Apply Filter

high = 13/(1000/2)
low = 500/(1000/2)
b, a = sp.signal.butter(4, [high,low], btype='bandpass', analog=True)

df110_10_S1['BF Filtered'] = sp.signal.filtfilt(b, a, df110_10_S1['BF EMG (Offset)'])
df110_10_S1['MH Filtered'] = sp.signal.filtfilt(b, a, df110_10_S1['MH EMG (Offset)'])
df120_10_S1['BF Filtered'] = sp.signal.filtfilt(b, a, df120_10_S1['BF EMG (Offset)'])
df120_10_S1['MH Filtered'] = sp.signal.filtfilt(b, a, df120_10_S1['MH EMG (Offset)'])
df130_10_S1['BF Filtered'] = sp.signal.filtfilt(b, a, df130_10_S1['BF EMG (Offset)'])
df130_10_S1['MH Filtered'] = sp.signal.filtfilt(b, a, df130_10_S1['MH EMG (Offset)'])
df150_10_S1['BF Filtered'] = sp.signal.filtfilt(b, a, df150_10_S1['BF EMG (Offset)'])
df150_10_S1['MH Filtered'] = sp.signal.filtfilt(b, a, df150_10_S1['MH EMG (Offset)'])
df170_10_S1['BF Filtered'] = sp.signal.filtfilt(b, a, df170_10_S1['BF EMG (Offset)'])
df170_10_S1['MH Filtered'] = sp.signal.filtfilt(b, a, df170_10_S1['MH EMG (Offset)'])

#%% Append MVC

df110_10_S1['MVC'] =  mmax_S1
df120_10_S1['MVC'] =  mmax_S1
df130_10_S1['MVC'] =  mmax_S1
df150_10_S1['MVC'] =  mmax_S1
df170_10_S1['MVC'] =  mmax_S1

#%% Descriptiors

alldes_10_S1 = ([['110', df110_10_S1.describe()], ['120', df120_10_S1.describe()], ['130', df130_10_S1.describe()],
           ['150', df150_10_S1.describe()], ['170', df170_10_S1.describe()]])
print([alldes_10_S1])

#%% Write to csv

df110_10_S1.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/df110_10_S1.csv')
df120_10_S1.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/df120_10_S1.csv')
df130_10_S1.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/df130_10_S1.csv')
df150_10_S1.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/df150_10_S1.csv')
df170_10_S1.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/df170_10_S1.csv')

#%%*************************************************************************************************************************%%#
#%% Session 2

os.chdir('C:/Users/cleed/Desktop/Data/Participant 01/SP/Session 2/TMS/5/Iso')

df110_5_S2 = pd.concat([pd.read_csv(file110, skiprows = 23) for file110 in glob.glob('01_AMT 110%*.csv')], ignore_index = True)
df120_5_S2 = pd.concat([pd.read_csv(file120, skiprows = 23) for file120 in glob.glob('01_AMT 120%*.csv')], ignore_index = True)
df130_5_S2 = pd.concat([pd.read_csv(file130, skiprows = 23) for file130 in glob.glob('01_AMT 130%*.csv')], ignore_index = True)
df150_5_S2 = pd.concat([pd.read_csv(file150, skiprows = 23) for file150 in glob.glob('01_AMT 150%*.csv')], ignore_index = True)
df170_5_S2 = pd.concat([pd.read_csv(file170, skiprows = 23) for file170 in glob.glob('01_AMT 170%*.csv')], ignore_index = True)

#%% Get S2 MVC

os.chdir('C:/Users/cleed/Desktop/Data/Participant 01/SP/Session 2/Strength')

dfmvc_S2 = pd.concat([pd.read_csv(mvc, skiprows = 23) for mvc in glob.glob('01_Hamstring_MVC*.csv')], ignore_index = True)
mmax_S2 = dfmvc_S1['Torque'].min() * -1

#%% Get the Data we Need and Filter by Position

df110_5_S2 = df110_5_S2[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df110_5_S2 = df110_5_S2.ffill()
df110_5_S2 = df110_5_S2.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df110_5_S2 = df110_5_S2.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df120_5_S2 = df120_5_S2[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df120_5_S2 = df120_5_S2.ffill()
df120_5_S2 = df120_5_S2.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df120_5_S2 = df120_5_S2.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df130_5_S2 = df130_5_S2[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df130_5_S2 = df130_5_S2.ffill()
df130_5_S2 = df130_5_S2.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df130_5_S2 = df130_5_S2.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df150_5_S2 = df150_5_S2[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df130_5_S2 = df130_5_S2.ffill()
df150_5_S2 = df150_5_S2.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32")
#df150_5_S2 = df150_5_S2.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 

df170_5_S2 = df170_5_S2[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df170_5_S2 = df170_5_S2.ffill()
df170_5_S2 = df170_5_S2.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df170_5_S2 = df170_5_S2.query("`BF max rmsEMG (Trigger)` >= 0.3 and `BF max rmsEMG (Trigger)` <= 0.7") 


#%% Account for EMG Offset

df110_5_S2['BF EMG (Offset)'] = df110_5_S2['BF EMG (Trigger)'] - np.mean(df110_5_S2['BF EMG (Trigger)'])
df110_5_S2['MH EMG (Offset)'] = df110_5_S2['MH EMG (Trigger)'] - np.mean(df110_5_S2['MH EMG (Trigger)'])
df120_5_S2['BF EMG (Offset)'] = df120_5_S2['BF EMG (Trigger)'] - np.mean(df120_5_S2['BF EMG (Trigger)'])
df120_5_S2['MH EMG (Offset)'] = df120_5_S2['MH EMG (Trigger)'] - np.mean(df120_5_S2['MH EMG (Trigger)'])
df130_5_S2['BF EMG (Offset)'] = df130_5_S2['BF EMG (Trigger)'] - np.mean(df130_5_S2['BF EMG (Trigger)'])
df130_5_S2['MH EMG (Offset)'] = df130_5_S2['MH EMG (Trigger)'] - np.mean(df130_5_S2['MH EMG (Trigger)'])
df150_5_S2['BF EMG (Offset)'] = df150_5_S2['BF EMG (Trigger)'] - np.mean(df150_5_S2['BF EMG (Trigger)'])
df150_5_S2['MH EMG (Offset)'] = df150_5_S2['MH EMG (Trigger)'] - np.mean(df150_5_S2['MH EMG (Trigger)'])
df170_5_S2['BF EMG (Offset)'] = df170_5_S2['BF EMG (Trigger)'] - np.mean(df170_5_S2['BF EMG (Trigger)'])
df170_5_S2['MH EMG (Offset)'] = df170_5_S2['MH EMG (Trigger)'] - np.mean(df170_5_S2['MH EMG (Trigger)'])

#%% Build and Apply Filter

high = 13/(1000/2)
low = 500/(1000/2)
b, a = sp.signal.butter(4, [high,low], btype='bandpass', analog=True)

df110_5_S2['BF Filtered'] = sp.signal.filtfilt(b, a, df110_5_S2['BF EMG (Offset)'])
df110_5_S2['MH Filtered'] = sp.signal.filtfilt(b, a, df110_5_S2['MH EMG (Offset)'])
df120_5_S2['BF Filtered'] = sp.signal.filtfilt(b, a, df120_5_S2['BF EMG (Offset)'])
df120_5_S2['MH Filtered'] = sp.signal.filtfilt(b, a, df120_5_S2['MH EMG (Offset)'])
df130_5_S2['BF Filtered'] = sp.signal.filtfilt(b, a, df130_5_S2['BF EMG (Offset)'])
df130_5_S2['MH Filtered'] = sp.signal.filtfilt(b, a, df130_5_S2['MH EMG (Offset)'])
df150_5_S2['BF Filtered'] = sp.signal.filtfilt(b, a, df150_5_S2['BF EMG (Offset)'])
df150_5_S2['MH Filtered'] = sp.signal.filtfilt(b, a, df150_5_S2['MH EMG (Offset)'])
df170_5_S2['BF Filtered'] = sp.signal.filtfilt(b, a, df170_5_S2['BF EMG (Offset)'])
df170_5_S2['MH Filtered'] = sp.signal.filtfilt(b, a, df170_5_S2['MH EMG (Offset)'])

#%% Append MVC

df110_5_S2['MVC'] =  mmax_S2
df120_5_S2['MVC'] =  mmax_S2
df130_5_S2['MVC'] =  mmax_S2
df150_5_S2['MVC'] =  mmax_S2
df170_5_S2['MVC'] =  mmax_S2

#%% Descriptiors

alldes_5_S2 = ([['110', df110_5_S2.describe()], ['120', df120_5_S2.describe()], ['130', df130_5_S2.describe()],
           ['150', df150_5_S2.describe()], ['170', df170_5_S2.describe()]])
print([alldes_5_S2])

#%% Write to csv

df110_5_S2.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/df110_5_S2.csv')
df120_5_S2.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/df120_5_S2.csv')
df130_5_S2.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/df130_5_S2.csv')
df150_5_S2.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/df150_5_S2.csv')
df170_5_S2.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/df170_5_S2.csv')

#%%*************************************************************************************************************************%%#
#%% Session 2 10%

os.chdir('C:/Users/cleed/Desktop/Data/Participant 01/SP/Session 2/TMS/10/Iso')

df110_10_S2 = pd.concat([pd.read_csv(file110, skiprows = 23) for file110 in glob.glob('01_AMT 110%*.csv')], ignore_index = True)
df120_10_S2 = pd.concat([pd.read_csv(file120, skiprows = 23) for file120 in glob.glob('01_AMT 120%*.csv')], ignore_index = True)
df130_10_S2 = pd.concat([pd.read_csv(file130, skiprows = 23) for file130 in glob.glob('01_AMT 130%*.csv')], ignore_index = True)
df150_10_S2 = pd.concat([pd.read_csv(file150, skiprows = 23) for file150 in glob.glob('01_AMT 150%*.csv')], ignore_index = True)
df170_10_S2 = pd.concat([pd.read_csv(file170, skiprows = 23) for file170 in glob.glob('01_AMT 170%*.csv')], ignore_index = True)

#%% Get the Data we Need and Filter by Position

df110_10_S2 = df110_10_S2[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df110_10_S2 = df110_10_S2.ffill()
df110_10_S2 = df110_10_S2.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df110_10_S2 = df110_10_S2.query("`BF max rmsEMG (Trigger)` >= 0.7 and `BF max rmsEMG (Trigger)` <= 0.13") 

df120_10_S2 = df120_10_S2[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df120_10_S2 = df120_10_S2.ffill()
df120_10_S2 = df120_10_S2.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df120_10_S2 = df120_10_S2.query("`BF max rmsEMG (Trigger)` >= 0.7 and `BF max rmsEMG (Trigger)` <= 0.13") 

df130_10_S2 = df130_10_S2[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df130_10_S2 = df130_10_S2.ffill()
df130_10_S2 = df130_10_S2.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df130_10_S2 = df130_10_S2.query("`BF max rmsEMG (Trigger)` >= 0.7 and `BF max rmsEMG (Trigger)` <= 0.13")  

df150_10_S2 = df150_10_S2[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df130_10_S2 = df130_10_S2.ffill()
df150_10_S2 = df150_10_S2.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32")
#df150_10_S2 = df150_10_S2.query("`BF max rmsEMG (Trigger)` >= 0.7 and `BF max rmsEMG (Trigger)` <= 0.13") 

df170_10_S2 = df170_10_S2[['BF EMG (Trigger)', 'MH EMG (Trigger)', 'BF max rmsEMG (Trigger)', 'Postition (Trigger)']]
df170_10_S2 = df170_10_S2.ffill()
df170_10_S2 = df170_10_S2.query("`Postition (Trigger)` >= 28 and `Postition (Trigger)` <= 32") 
#df170_10_S2 = df170_10_S2.query("`BF max rmsEMG (Trigger)` >= 0.7 and `BF max rmsEMG (Trigger)` <= 0.13") 


#%% Account for EMG Offset

df110_10_S2['BF EMG (Offset)'] = df110_10_S2['BF EMG (Trigger)'] - np.mean(df110_10_S2['BF EMG (Trigger)'])
df110_10_S2['MH EMG (Offset)'] = df110_10_S2['MH EMG (Trigger)'] - np.mean(df110_10_S2['MH EMG (Trigger)'])
df120_10_S2['BF EMG (Offset)'] = df120_10_S2['BF EMG (Trigger)'] - np.mean(df120_10_S2['BF EMG (Trigger)'])
df120_10_S2['MH EMG (Offset)'] = df120_10_S2['MH EMG (Trigger)'] - np.mean(df120_10_S2['MH EMG (Trigger)'])
df130_10_S2['BF EMG (Offset)'] = df130_10_S2['BF EMG (Trigger)'] - np.mean(df130_10_S2['BF EMG (Trigger)'])
df130_10_S2['MH EMG (Offset)'] = df130_10_S2['MH EMG (Trigger)'] - np.mean(df130_10_S2['MH EMG (Trigger)'])
df150_10_S2['BF EMG (Offset)'] = df150_10_S2['BF EMG (Trigger)'] - np.mean(df150_10_S2['BF EMG (Trigger)'])
df150_10_S2['MH EMG (Offset)'] = df150_10_S2['MH EMG (Trigger)'] - np.mean(df150_10_S2['MH EMG (Trigger)'])
df170_10_S2['BF EMG (Offset)'] = df170_10_S2['BF EMG (Trigger)'] - np.mean(df170_10_S2['BF EMG (Trigger)'])
df170_10_S2['MH EMG (Offset)'] = df170_10_S2['MH EMG (Trigger)'] - np.mean(df170_10_S2['MH EMG (Trigger)'])

#%% Build and Apply Filter

high = 13/(1000/2)
low = 500/(1000/2)
b, a = sp.signal.butter(4, [high,low], btype='bandpass', analog=True)

df110_10_S2['BF Filtered'] = sp.signal.filtfilt(b, a, df110_10_S2['BF EMG (Offset)'])
df110_10_S2['MH Filtered'] = sp.signal.filtfilt(b, a, df110_10_S2['MH EMG (Offset)'])
df120_10_S2['BF Filtered'] = sp.signal.filtfilt(b, a, df120_10_S2['BF EMG (Offset)'])
df120_10_S2['MH Filtered'] = sp.signal.filtfilt(b, a, df120_10_S2['MH EMG (Offset)'])
df130_10_S2['BF Filtered'] = sp.signal.filtfilt(b, a, df130_10_S2['BF EMG (Offset)'])
df130_10_S2['MH Filtered'] = sp.signal.filtfilt(b, a, df130_10_S2['MH EMG (Offset)'])
df150_10_S2['BF Filtered'] = sp.signal.filtfilt(b, a, df150_10_S2['BF EMG (Offset)'])
df150_10_S2['MH Filtered'] = sp.signal.filtfilt(b, a, df150_10_S2['MH EMG (Offset)'])
df170_10_S2['BF Filtered'] = sp.signal.filtfilt(b, a, df170_10_S2['BF EMG (Offset)'])
df170_10_S2['MH Filtered'] = sp.signal.filtfilt(b, a, df170_10_S2['MH EMG (Offset)'])

#%% Append MVC

df110_10_S2['MVC'] =  mmax_S2
df120_10_S2['MVC'] =  mmax_S2
df130_10_S2['MVC'] =  mmax_S2
df150_10_S2['MVC'] =  mmax_S2
df170_10_S2['MVC'] =  mmax_S2

#%% Descriptiors

alldes_10_S2 = ([['110', df110_10_S2.describe()], ['120', df120_10_S2.describe()], ['130', df130_10_S2.describe()],
           ['150', df150_10_S2.describe()], ['170', df170_10_S2.describe()]])
print([alldes_10_S2])

#%% Write to csv

df110_10_S2.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/df110_10_S2.csv')
df120_10_S2.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/df120_10_S2.csv')
df130_10_S2.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/df130_10_S2.csv')
df150_10_S2.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/df150_10_S2.csv')
df170_10_S2.to_csv('C:/Users/cleed/Desktop/Data/Outputs/Participant_1/df170_10_S2.csv')






















