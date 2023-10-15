"""
Created on Mon Sep  4 09:40:32 2023

@author: cleed
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import shutil

#%%
# Create an empty list to store copied files and their new locations
copied_files_log = []

base_path = "C:\\Users\\cleed\\OneDrive\\Desktop\\Data\\"
participants = ["Participant 15"]

def file_checker(base_path, participant):
    new_base_path = "C:\\Users\\cleed\\OneDrive\\Desktop\\CData\\"

    for stim_type in ['SP', 'PP']:
        for session in ['Session 1', 'Session 2']:
            for intensity in ['5', '10']:
                for contraction in ['Iso', 'Ecc']:
                    folder_path = os.path.join(base_path, participant, stim_type, session, 'TMS', intensity, contraction)
                    new_folder_path = os.path.join(new_base_path, participant, stim_type, session, 'TMS', intensity, contraction)

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
                                if keep in ['yes', 'y']:
                                    # Ensure the new directory structure exists
                                    if not os.path.exists(new_folder_path):
                                        os.makedirs(new_folder_path)
                                    # Copy the file to the new location
                                    destination_path = os.path.join(new_folder_path, os.path.basename(file))
                                    shutil.copy2(file, destination_path)
                                    print(f"File copied to: {destination_path}")
                                    
                                    # Append the original and new location to the log list
                                    copied_files_log.append((file, destination_path))

# Running the function for each participant
for participant in participants:
    file_checker(base_path, participant)

print("All files for the participant have been processed!")

# Write the copied files and their new locations to a log file
for participant in participants:
    log_file_path = os.path.join(base_path, participant, "copied_files_log.txt")
    with open(log_file_path, "w") as log_file:
        for original, new in copied_files_log:
            log_file.write(f"Original: {original}\nNew Location: {new}\n\n")
