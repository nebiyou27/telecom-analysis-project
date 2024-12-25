"""
utils.py

This module contains reusable utility functions.
"""

import os

def save_dataframe_to_csv(df, file_path):
    """
    Save a DataFrame to a CSV file.
    
    Parameters:
        df (pd.DataFrame): DataFrame to save.
        file_path (str): Path to save the CSV file.
    """
    df.to_csv(file_path, index=False)

def create_directory(directory_path):
    """
    Create a directory if it does not exist.
    
    Parameters:
        directory_path (str): Path to the directory.
    """
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)