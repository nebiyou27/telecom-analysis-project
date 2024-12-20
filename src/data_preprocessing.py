import pandas as pd

def load_data(file_path):
    """Load the dataset from a CSV file."""
    return pd.read_csv(file_path)

def clean_data(df):
    """Clean the dataset by handling missing values and outliers."""
    # Handle missing values by replacing them with the column mean
    df.fillna(df.mean(), inplace=True)
    
    # Handle outliers (e.g., using IQR to remove outliers)
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1
    df = df[~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)]
    
    return df

def preprocess():
    """Load and clean the data."""
    file_path = r"C:\Users\neba\Downloads\Copy of Week2_challenge_data_source(CSV).csv"
    df = load_data(file_path)
    df = clean_data(df)
    return df
