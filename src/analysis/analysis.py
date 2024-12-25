"""
analysis.py

This module performs data analysis and generates insights.
"""

import pandas as pd

def calculate_statistics(df, columns):
    """
    Calculate basic statistics (mean, median, std) for specified columns.
    
    Parameters:
        df (pd.DataFrame): Input DataFrame.
        columns (list): List of columns to calculate statistics for.
    
    Returns:
        pd.DataFrame: DataFrame containing statistics.
    """
    stats = df[columns].describe().T
    return stats

def user_engagement_analysis(df):
    """
    Analyze user engagement metrics.
    
    Parameters:
        df (pd.DataFrame): Input DataFrame.
    
    Returns:
        dict: Summary of engagement metrics.
    """
    engagement_summary = {
        "average_session_duration": df["session_duration"].mean(),
        "total_sessions": df["session_id"].nunique(),
        "average_clicks_per_session": df["clicks"].mean()
    }
    return engagement_summary