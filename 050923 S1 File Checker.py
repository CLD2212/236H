"""
Created on Mon Sep  4 09:40:32 2023

@author: cleed
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import re


#%%

base_path = "C:\\Users\\cleed\\OneDrive\\Desktop\\Data\\"
participants = ["Participant 04"]
filtered_files_list = []

def file_checker(base_path, participant):
    files_to_analyze = []

    for stim_type in ['SP', 'PP']:
        for session in ['Session 1', 'Session 2']:
            for intensity in ['5', '10']:
                for contraction in ['Iso', 'Ecc']:
                    folder_path = os.path.join(base_path, participant, stim_type, session, 'TMS', intensity, contraction)

                    print(f"Checking path: {folder_path}")
                    if os.path.exists(folder_path):
                        print(f"Importing data from: {folder_path}")
                        all_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
                        
                        for file in all_files:
                            if any(term in os.path.basename(file) for term in ['AMT', 'SICI', 'ICF']):
                                df = pd.read_csv(file, skiprows=23)
                                
                                # Plot the 'BF EMG (Trigger)' column
                                plt.figure(figsize=(10,6))
                                plt.plot(df['BF EMG (Trigger)'])
                                plt.title(f"File: {os.path.basename(file)}")
                                plt.xlabel('Data Points')
                                plt.ylabel('Amplitude')
                                plt.show()
                                
                                # Ask the user if they want to keep this file for analysis
                                keep = input(f"Do you want to keep {os.path.basename(file)} for analysis? (yes/no): ").strip().lower()
                                if keep == 'yes':
                                    files_to_analyze.append(file)

    return files_to_analyze

# Running the function for each participant
for participant in participants:
    filtered_files_list.extend(file_checker(base_path, participant))

print("Files kept for analysis:")
print(filtered_files_list)
