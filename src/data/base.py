from sqlalchemy import create_engine
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TellcoBaseAnalyzer:
    def __init__(self, connection_string):
        """Initialize with database connection"""
        self.engine = create_engine(connection_string)
        
    def load_data(self):
        """Load data from database"""
        try:
            query = "SELECT * FROM xdr_data"
            return pd.read_sql(query, self.engine)
        except Exception as e:
            logger.error(f"Error loading data: {e}")
            raise

    def handle_missing_values(self, df):
        """Handle missing values in dataframe"""
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        categorical_cols = df.select_dtypes(exclude=[np.number]).columns
        
        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
        df[categorical_cols] = df[categorical_cols].fillna(df[categorical_cols].mode().iloc[0])
        
        return df

    def handle_outliers(self, df, columns, method='iqr'):
        """Handle outliers using IQR method"""
        for column in columns:
            if method == 'iqr':
                Q1 = df[column].quantile(0.25)
                Q3 = df[column].quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - 1.5 * IQR
                upper_bound = Q3 + 1.5 * IQR
                df[column] = df[column].clip(lower=lower_bound, upper=upper_bound)
        return df