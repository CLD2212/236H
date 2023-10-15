"""
Created on Tues Aug 29 17:24:06 2023
Modified on Tues Sep 26

@author: cleed
"""

import numpy as np
import os
import pandas as pd
import re
import scipy.signal as sp
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from collections import defaultdict

#%% Load Strength Files

def load_MVC_files(participant, session_code):
    base_path = "C:/Users/cleed/OneDrive/Desktop/Data"
    
    # Map session codes to their respective directory paths
    folder_mapping = {
        'SP1': os.path.join(participant, 'SP', 'Session 1', 'Strength'),
        'SP2': os.path.join(participant, 'SP', 'Session 2', 'Strength'),
        'PP1': os.path.join(participant, 'PP', 'Session 1', 'Strength'),
        'PP2': os.path.join(participant, 'PP', 'Session 2', 'Strength')
    }
    
    folder_path = os.path.join(base_path, folder_mapping[session_code])
    
    print(f"Checking folder: {folder_path}")
    
    # List all files in the directory
    all_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    # Use regex to filter for files that match the MVC pattern
    mvc_files = [file for file in all_files if re.match(r"\d+_Hamstring_MVC_\d+.csv", file)]
    
    print(f"Files found: {mvc_files}")
    
    mvc_files_list = []
    for file in mvc_files:
        filepath = os.path.join(folder_path, file)
        df = pd.read_csv(filepath, skiprows=23)  # Adjust the number of rows to skip if needed
        mvc_files_list.append(df)
        
    return mvc_files_list

def rolling_rms(series, window_size):
    return series.rolling(window=window_size).apply(lambda x: np.sqrt(np.mean(x**2)))

def max_rolling_rms_for_session(files_list):
    max_rms_values = []

    for df in files_list:
        rms_values = rolling_rms(df['BF EMG'], 100)
        max_rms_values.append(rms_values.max())

    return max_rms_values

participant = 'Participant 04'
sessions = ['SP1', 'SP2', 'PP1', 'PP2']

# Create an empty DataFrame to store results
rms_df = pd.DataFrame(columns=['Participant', 'Session', 'Max Rolling RMS'])

for session_code in sessions:
    files = load_MVC_files(participant, session_code)
    max_rms_values = max_rolling_rms_for_session(files)

    # Populate results DataFrame
    for idx, value in enumerate(max_rms_values):
        new_row = pd.DataFrame({
            'Participant': [participant],
            'Session': [session_code],
            'Max Rolling RMS': [value]
        })
        rms_df = pd.concat([rms_df, new_row], ignore_index=True)
        
#%% Data Import and Filters

# Use file pathway to specify participant(s)
base_path = "C:\\Users\\cleed\\OneDrive\\Desktop\\Data\\"
participants = ["Participant 04"]
filtered_files_list = []

# Look directly at file names to extract relevant info 
def extract_file_info(filename):
    #'(\d{2})_' two digits followed by an underscore for participant number
    participant = re.search(r'(\d{2})_', filename)
    participant = participant.group(1) if participant else None

    #'(AMT|ICF|SICI)' searches for the relevant test type
    test_type = re.search(r'(AMT|ICF|SICI)', filename)
    test_type = test_type.group(1) if test_type else None

    #'(\d+%)' one or more digits followed by a percentage sign for intensity
    stim_intensity_match = re.search(r'(\d+%)', filename)
    stim_intensity = stim_intensity_match.group(1) if stim_intensity_match else None

    #'(\d{2} \d{3})' two digits, a space then three digits for paired pulse intensities
    pair_pulse_match = re.search(r'(\d{2} \d{3})', filename)
    pair_pulse = pair_pulse_match.group(1) if pair_pulse_match else None

    # Extract the single pulse intensity if available, for example '130' or '150'
    single_pulse_match = re.search(r'_(\d{3})', filename)
    single_pulse = single_pulse_match.group(1) if single_pulse_match else None

    #'(_\d{2}$)' last two digits of the file name to find the stimulation number
    stim_number_match = re.search(r'_\d{2}$', filename)
    stim_number = stim_number_match.group().replace("_", "") if stim_number_match else None

    # Create a dictionary of the information
    return {
        'Participant': participant,
        'Test Type': test_type,
        'Stimulation Intensity': stim_intensity,
        'Pair Pulse': pair_pulse,
        'Stimulation Number': stim_number,
        'Single Pulse': single_pulse
    }

def apply_filters(df, intensity, filepath, rms_df):
    # Extracting session and participant info from filepath
    session_info = re.search(r'(SP|PP)\\Session (\d)', filepath)
    # Combine session_info into session (e.g. SP\1 becomes SP1)
    session = f"{session_info.group(1)}{session_info.group(2)}" if session_info else None

    participant_info = re.search(r'Participant (\d{2})', filepath)
    participant = participant_info.group(1) if participant_info else None

    # If the DataFrame is too short, return None
    if len(df) <= 27:
        return None

    # Does 'Position (Trigger)' exist?
    if 'Position (Trigger)' not in df.columns:
        print("Warning: 'Position (Trigger)' column not found in the data. Skipping file...")
        return None

    # Build butterworth filter
    high = 13 / (1000 / 2)
    low = 499 / (1000 / 2)
    b, a = sp.butter(4, [high, low], btype='bandpass', analog=False)

    # Apply the filter
    df['BF EMG (Filtered)'] = sp.filtfilt(b, a, df['BF EMG (Trigger)'])

    # Normalizing 'BF EMG (Filtered)' using Max Rolling RMS from rms_df
    if session and participant:
        # For Paired Pulse sessions, check the type of paired pulse stimulation
        if session.startswith('PP'):
            file_info = extract_file_info(filepath)
            single_pulse = file_info.get('Single Pulse')
            pair_pulse = file_info.get('Pair Pulse')

            if pair_pulse and single_pulse:
                # Get the max RMS value corresponding to the single pulse for normalization
                max_rms_value = rms_df[(rms_df['Participant'] == "Participant " + participant) & 
                                       (rms_df['Session'] == session) & 
                                       (rms_df['Stimulation Intensity'] == single_pulse)]['Max Rolling RMS'].max()
            else:
                # For other files, use the overall max RMS value for normalization
                max_rms_value = rms_df[(rms_df['Participant'] == "Participant " + participant) & 
                                       (rms_df['Session'] == session)]['Max Rolling RMS'].max()
        else:
            # For other sessions (not PP), use the overall max RMS value for normalization
            max_rms_value = rms_df[(rms_df['Participant'] == "Participant " + participant) & 
                                   (rms_df['Session'] == session)]['Max Rolling RMS'].max()

        df['BF EMG (Filtered)'] = df['BF EMG (Filtered)'] / max_rms_value

    # Check the 201st data point in 'Position (Trigger)' column
    if df['Position (Trigger)'].iloc[200] >= 27 and df['Position (Trigger)'].iloc[200] <= 33:
        return df
    else:
        return None 

    # Calculate RMS for indices 101 to 200
    def calculate_rms(segment):
        return np.sqrt(np.mean(np.square(segment)))

    segment = df['BF EMG (Filtered)'].iloc[101:200]
    rms_value = calculate_rms(segment)

    # Define the rms range based on the intensity
    if intensity == '10':
        valid_rms_range = (0.07, 0.13)
    elif intensity == '5':
        valid_rms_range = (0.03, 0.07)
    else:
        print(f"Unexpected intensity value: {intensity}. Skipping file...")
        return None

    # Check the rms value against the valid range
    if not valid_rms_range[0] <= rms_value <= valid_rms_range[1]:
        # If outside the valid_rms_range, skip the file 
        return None

    return df 

#%%

for participant in participants:
    for stim_type in ['SP', 'PP']:
        for session in ['Session 1', 'Session 2']:
            # Extracting the session number directly from the session string
            session_number = re.search(r'(\d)', session).group(1)

            for intensity in ['5', '10']:
                for contraction in ['Iso', 'Ecc']:
                    folder_path = os.path.join(base_path, participant, stim_type, session, 'TMS', intensity, contraction)

                    print(f"Checking path: {folder_path}")
                    if os.path.exists(folder_path):
                        print(f"Importing data from: {folder_path}")
                        all_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
                        
                        for file in all_files:
                            df = pd.read_csv(file, skiprows=23)
                            df.rename(columns={"Postition (Trigger)": "Position (Trigger)"}, inplace=True)  # Fixing the typo
                            file_info = extract_file_info(os.path.basename(file))
                            
                                                     
                            df['Participant ID'] = file_info['Participant']
                            df['Test Type'] = file_info['Test Type']
                            df['Stimulation Intensity'] = file_info['Stimulation Intensity']
                            df['Pair Pulse'] = file_info['Pair Pulse']
                            df['Stimulation Number'] = file_info['Stimulation Number']
                            df['Stimulation Type'] = stim_type
                            df['Intensity'] = intensity
                            df['Contraction Mode'] = contraction
                            df['Session Number'] = session_number  # Adding the session number column

                            df = df.reset_index(drop=True)
                            df['row_id'] = df.index  # Assigning the index to row_id for file

                            df_filtered = apply_filters(df, intensity, file, rms_df)

                            # Only append to the list if the filtered DataFrame is not None
                            if df_filtered is not None:
                                filtered_files_list.append(df_filtered)
    
#%% Concatenate 

# Concatenate all filtered dataframes
df_combined = pd.concat(filtered_files_list, axis=0)
df_combined = df_combined.reset_index(drop=True)

# Get unique values of Pair Pulse
unique_pair_pulse_values = df_combined['Pair Pulse'].unique()
unique_test_types_values = df_combined['Test Type'].unique()

print("Unique values in 'Pair Pulse':", unique_pair_pulse_values)
print("Unique values in 'Test Type':", unique_test_types_values)

#%% Mask and Drop Pair Pulse

# Create a mask for ICF or SICI
mask_ICF_SICI = df_combined['Test Type'].isin(['ICF', 'SICI'])

# Fill the 'Stimulation Intensity' with values from 'Pair Pulse' where mask_ICF_SICI is True
df_combined.loc[mask_ICF_SICI, 'Stimulation Intensity'] = df_combined.loc[mask_ICF_SICI, 'Stimulation Intensity'].fillna(df_combined['Pair Pulse'])

# Checking unique values of 'Stimulation Intensity'
unique_stim_intensity = df_combined['Stimulation Intensity'].unique()
unique_test_types = df_combined['Test Type'].unique()

print("Unique values in 'Stimulation Intensity':", unique_stim_intensity)
print("Unique values in 'Test Type':", unique_test_types)

# Drop the 'Pair Pulse' column
df_combined.drop(columns='Pair Pulse', inplace=True)

#%% Split the dataframe based on Test Type

df_AMT = df_combined[df_combined['Test Type'] == 'AMT']
df_SICI = df_combined[df_combined['Test Type'] == 'SICI']
df_ICF = df_combined[df_combined['Test Type'] == 'ICF']

print(df_AMT.head())
print(df_SICI.head())
print(df_ICF.head())

#%% Group the data

# Group by the conditions and row_id
group_cols = ['Stimulation Type', 'Intensity', 'Contraction Mode', 'Session Number', 'Stimulation Intensity', 'Test Type', 'Participant ID', 'row_id']
df_AMT = df_AMT.groupby(group_cols).head(10)
df_SICI = df_SICI.groupby(group_cols).head(10)
df_ICF = df_AMT.groupby(group_cols).head(10)

agg_functions = {'BF EMG (Filtered)': ['mean', 'std']}

# AMT
averaged_AMT_data = df_AMT.groupby(group_cols).agg({'BF EMG (Filtered)': ['mean', 'std']}).reset_index()
averaged_AMT_data.columns = [col[0] if col[1] == '' else '_'.join(col).strip() for col in averaged_AMT_data.columns.values]

# SICI
averaged_SICI_data = df_SICI.groupby(group_cols).agg({'BF EMG (Filtered)': ['mean', 'std']}).reset_index()
averaged_SICI_data.columns = [col[0] if col[1] == '' else '_'.join(col).strip() for col in averaged_SICI_data.columns.values]

# ICF
averaged_ICF_data = df_ICF.groupby(group_cols).agg({'BF EMG (Filtered)': ['mean', 'std']}).reset_index()
averaged_ICF_data.columns = [col[0] if col[1] == '' else '_'.join(col).strip() for col in averaged_ICF_data.columns.values]


#%%

print(averaged_AMT_data.columns)

#%% Plots for AMT

# This assumes participants is predefined
# Also assumes only a single participant in the participants list
# E.g. participants = ["Participant 04"]

# Group by columns excluding 'row_id' for plotting purposes
group_cols_without_rowid = ['Stimulation Type', 'Intensity', 'Contraction Mode', 'Session Number', 'Stimulation Intensity', 'Test Type', 'Participant ID']
grouped = averaged_AMT_data.groupby(group_cols_without_rowid)

# Extract the individual grouped dataframes based on the grouping columns
grouped_dfs = [grouped.get_group(g) for g in grouped.groups.keys()]

# Extract participant number
participant_name = participants[0]  # This gets "Participant 04"
participant_number = participant_name.split(" ")[1]  # This extracts "04" from "Participant 04"
pdf_filename = f"Participant{participant_number}_AMT_plots.pdf"

with PdfPages(pdf_filename) as pdf:
    for df_group in grouped_dfs:
        if not df_group.empty:
            # Extract the unique condition values for the current grouped dataframe
            conditions = tuple(df_group[col].iloc[0] for col in group_cols_without_rowid)  
            title_conditions = ", ".join([f"{col}: {val}" for col, val in zip(group_cols_without_rowid, conditions)])

            plt.figure(figsize=(10, 6))
            
            # Plotting the mean data
            plt.plot(df_group['row_id'], df_group['BF EMG (Filtered)_mean'], label='BF EMG (Filtered) Mean', color='blue')
            
            # Add the standard deviation as a shaded region around the mean
            plt.fill_between(df_group['row_id'], 
                             df_group['BF EMG (Filtered)_mean'] - df_group['BF EMG (Filtered)_std'], 
                             df_group['BF EMG (Filtered)_mean'] + df_group['BF EMG (Filtered)_std'], 
                             color='blue', alpha=0.2, label='1 Std Deviation')
            
            # Setting the title using the conditions and labels
            plt.title(f"{title_conditions}")
            plt.xlabel('Row ID')
            plt.ylabel('BF EMG (Filtered)')
            plt.legend()
            
            plt.grid(True)
            plt.tight_layout()
            
            # Save the current figure to the PDF
            pdf.savefig(plt.gcf())  # Save the current figure to the pdf
            plt.close()  # Close the figure to free up memory
        
        plt.grid(True)
        plt.tight_layout()
        plt.show()
        
#%% Plots for SICI

# Same Assumptions for AMT

# Group by columns excluding 'row_id' for plotting purposes
group_cols_without_rowid = ['Stimulation Type', 'Intensity', 'Contraction Mode', 'Session Number', 'Stimulation Intensity', 'Test Type', 'Participant ID']
grouped = averaged_SICI_data.groupby(group_cols_without_rowid)

# Extract the individual grouped dataframes based on the grouping columns
grouped_dfs = [grouped.get_group(g) for g in grouped.groups.keys()]

# Extract participant number
participant_name = participants[0]  # This gets "Participant 04"
participant_number = participant_name.split(" ")[1]  # This extracts "04" from "Participant 04"
pdf_filename = f"Participant{participant_number}_SICI_plots.pdf"

with PdfPages(pdf_filename) as pdf:
    for df_group in grouped_dfs:
        if not df_group.empty:
            # Extract the unique condition values for the current grouped dataframe
            conditions = tuple(df_group[col].iloc[0] for col in group_cols_without_rowid)  
            title_conditions = ", ".join([f"{col}: {val}" for col, val in zip(group_cols_without_rowid, conditions)])

            plt.figure(figsize=(10, 6))
            
            # Plotting the mean data
            plt.plot(df_group['row_id'], df_group['BF EMG (Filtered)_mean'], label='BF EMG (Filtered) Mean', color='blue')
            
            # Add the standard deviation as a shaded region around the mean
            plt.fill_between(df_group['row_id'], 
                             df_group['BF EMG (Filtered)_mean'] - df_group['BF EMG (Filtered)_std'], 
                             df_group['BF EMG (Filtered)_mean'] + df_group['BF EMG (Filtered)_std'], 
                             color='blue', alpha=0.2, label='1 Std Deviation')
            
            # Setting the title using the conditions and labels
            plt.title(f"{title_conditions}")
            plt.xlabel('Row ID')
            plt.ylabel('BF EMG (Filtered)')
            plt.legend()
            
            plt.grid(True)
            plt.tight_layout()
            
            # Save the current figure to the PDF
            pdf.savefig(plt.gcf())  # Save the current figure to the pdf
            plt.close()  # Close the figure to free up memory
#%% Plots for ICF

# Same Assumptions as AMT/SICI

# Group by columns excluding 'row_id' for plotting purposes
group_cols_without_rowid = ['Stimulation Type', 'Intensity', 'Contraction Mode', 'Session Number', 'Stimulation Intensity', 'Test Type', 'Participant ID']
grouped = averaged_ICF_data.groupby(group_cols_without_rowid)

# Extract the individual grouped dataframes based on the grouping columns
grouped_dfs = [grouped.get_group(g) for g in grouped.groups.keys()]

# Extract participant number
participant_name = participants[0]  # This gets "Participant 04"
participant_number = participant_name.split(" ")[1]  # This extracts "04" from "Participant 04"
pdf_filename = f"Participant{participant_number}_ICF_plots.pdf"

with PdfPages(pdf_filename) as pdf:
    for df_group in grouped_dfs:
        if not df_group.empty:
            # Extract the unique condition values for the current grouped dataframe
            conditions = tuple(df_group[col].iloc[0] for col in group_cols_without_rowid)  
            title_conditions = ", ".join([f"{col}: {val}" for col, val in zip(group_cols_without_rowid, conditions)])

            plt.figure(figsize=(10, 6))
            
            # Plotting the mean data
            plt.plot(df_group['row_id'], df_group['BF EMG (Filtered)_mean'], label='BF EMG (Filtered) Mean', color='blue')
            
            # Add the standard deviation as a shaded region around the mean
            plt.fill_between(df_group['row_id'], 
                             df_group['BF EMG (Filtered)_mean'] - df_group['BF EMG (Filtered)_std'], 
                             df_group['BF EMG (Filtered)_mean'] + df_group['BF EMG (Filtered)_std'], 
                             color='blue', alpha=0.2, label='1 Std Deviation')
            
            # Setting the title using the conditions and labels
            plt.title(f"{title_conditions}")
            plt.xlabel('Row ID')
            plt.ylabel('BF EMG (Filtered)')
            plt.legend()
            
            plt.grid(True)
            plt.tight_layout()
            
            # Save the current figure to the PDF
            pdf.savefig(plt.gcf())  # Save the current figure to the pdf
            plt.close()  # Close the figure to free up memory


#%% 








