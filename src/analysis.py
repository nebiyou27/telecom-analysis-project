import pandas as pd

def aggregate_data(df):
    """Aggregate data for analysis."""
    # Example aggregation: sum of total data usage per user
    df['total_data_usage'] = df['download'] + df['upload']
    return df.groupby('user_id')['total_data_usage'].sum()

def analyze_user_behavior(df):
    """Perform analysis on user behavior."""
    top_10_users = df.nlargest(10, 'total_data_usage')
    return top_10_users