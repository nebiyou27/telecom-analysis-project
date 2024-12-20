import matplotlib.pyplot as plt
import seaborn as sns

def plot_data_usage(df):
    """Plot total data usage for the top 10 users."""
    top_10_users = df.nlargest(10, 'total_data_usage')
    plt.figure(figsize=(10, 6))
    sns.barplot(x='user_id', y='total_data_usage', data=top_10_users)
    plt.title('Top 10 Users by Total Data Usage')
    plt.xlabel('User ID')
    plt.ylabel('Total Data Usage')
    plt.xticks(rotation=45)
    plt.show()
