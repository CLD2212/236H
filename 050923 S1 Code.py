"""
Created on Tues Aug 29 17:24:06 2023

@author: cleed
"""

import numpy as np
import os
import pandas as pd
import re
import scipy.signal as sp
import matplotlib.pyplot as plt

#%% Step 1: Data Import and Filters

base_path = "C:\\Users\\cleed\\OneDrive\\Desktop\\Data\\"
participants = ["Participant 04"]
filtered_files_list = []

def extract_file_info(filename):
    participant = re.search(r'(\d{2})_', filename)
    participant = participant.group(1) if participant else None

    test_type = re.search(r'(AMT|ICF|SICI)', filename)
    test_type = test_type.group(1) if test_type else None

    stim_intensity_match = re.search(r'(\d+%)', filename)
    stim_intensity = stim_intensity_match.group(1) if stim_intensity_match else None

    pair_pulse_match = re.search(r'(\d{2} \d{3})', filename)
    pair_pulse = pair_pulse_match.group(1) if pair_pulse_match else None

    stim_number_match = re.search(r'_\d{2}$', filename)
    stim_number = stim_number_match.group().replace("_", "") if stim_number_match else None

    return {
        'Participant': participant,
        'Test Type': test_type,
        'Stimulation Intensity': stim_intensity,
        'Pair Pulse': pair_pulse,
        'Stimulation Number': stim_number
    }

def apply_filters(df):
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

    # Filtering the dataframe based on 'Position (Trigger)'
    df = df[(df['Position (Trigger)'] >= 27) & (df['Position (Trigger)'] <= 33)]

    # Position filter
    start_indices = df[df['Position (Trigger)'] == 27].index

    # List of indices to drop
    to_drop = []

    for start in start_indices:
        rms_value = df.at[start, 'BF max rmsEMG (Trigger)']

    # Define acceptable rms range based on the intensity
    if intensity == '10':
        valid_rms_range = (0.7, 1.3)
    elif intensity == '5':
        valid_rms_range = (0.3, 0.7)
    else:
        print(f"Unexpected intensity value: {intensity}. Skipping file...")
        return None

    # Check the rms value against the valid range
    if not valid_rms_range[0] <= rms_value <= valid_rms_range[1]:
        # If the rmsEMG is outside of the range, collect indices for the entire repetition
        to_drop.extend(range(start, start + len(df[(df['Position (Trigger)'] >= 27) & (df['Position (Trigger)'] <= 33)])))

    df.drop(to_drop, inplace=True)

    return df


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

                            # Reset the index before adding row_id
                            df = df.reset_index(drop=True)
                            group_cols = ['Stimulation Type', 'Intensity', 'Contraction Mode', 'Session Number', 'Stimulation Intensity', 'Test Type', 'Participant ID']
                            df['row_id'] = df.groupby(group_cols).cumcount()

                            df_filtered = apply_filters(df)

                            # Only append to the list if the filtered DataFrame is not None
                            if df_filtered is not None:
                                filtered_files_list.append(df_filtered)


#%% Average the traces

# Concatenate all filtered dataframes
df_combined = pd.concat(filtered_files_list, axis=0)

# Group by the conditions and row_id
group_cols = ['Stimulation Type', 'Intensity', 'Contraction Mode', 'Session Number', 'Stimulation Intensity', 'Test Type', 'Participant ID', 'row_id']
averaged_data = df_combined.groupby(group_cols).agg({'BF EMG (Filtered)': 'mean'}).reset_index()


#%% Split the Average Traces into Different Frames

grouped_dfs = [group for _, group in averaged_data.groupby(group_cols[:-1])]

#%% Using grouped_dfs, generate plots

for df_group in grouped_dfs:
    conditions = tuple(df_group[col].iloc[0] for col in group_cols[:-1])  
    title_conditions = ", ".join([f"{col}: {val}" for col, val in zip(group_cols[:-1], conditions)])
    
    plt.figure(figsize=(10, 6))
    
    # Plotting the data
    plt.plot(df_group['row_id'], df_group['BF EMG (Filtered)'], label='BF EMG (Filtered)')
    
    # Setting the title using the conditions and labels
    plt.title(f"BF EMG (Filtered) for Conditions: {title_conditions}")
    plt.xlabel('Row ID')
    plt.ylabel('BF EMG (Filtered)')
    plt.legend()
    
    plt.grid(True)
    plt.tight_layout()
    plt.show()

#%% Load Strength Files

def load_MVC_files(participant, session_name):
    base_path = "C:/Users/cleed/OneDrive/Data"
    stim_types = ['SP', 'PP']
    
    mvc_files_list = []

    for stim_type in stim_types:
        folder_path = os.path.join(base_path, participant, stim_type, session_name, 'Strength')
        
        print(f"Checking folder: {folder_path}")
        
        # List all files in the directory
        all_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

        # Use regex to filter for files that match the MVC pattern
        mvc_files = [file for file in all_files if re.match(r"\d+_Hamstring_MVC_\d+.csv", file)]
        
        print(f"Files found: {mvc_files}")

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

sessions_mapping = {
    'SP1': 'Session 1',
    'SP2': 'Session 2',
    'PP1': 'Session 1',
    'PP2': 'Session 2'
}

# Create an empty DataFrame to store results
results_df = pd.DataFrame(columns=['Participant', 'Session', 'Max Rolling RMS'])

for session_code in sessions:
    session_name = sessions_mapping[session_code]
    files = load_MVC_files(participant, session_name)
    max_rms_values = max_rolling_rms_for_session(files)

    # Populate results DataFrame
    for idx, value in enumerate(max_rms_values):
        new_row = pd.DataFrame({
            'Participant': [participant],
            'Session': [session_code],
            'Max Rolling RMS': [value]
        })
        results_df = pd.concat([results_df, new_row], ignore_index=True)
        
#%% 








