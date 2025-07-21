import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

# =============================================================================
# Task 1 & 2: Data Loading and Preparation
# =============================================================================

def load_and_prepare_data(filepath, line_prefix):
    """
    Loads passenger flow data and prepares it by reordering station columns.

    Args:
        filepath (str): The path to the CSV file.
        line_prefix (str): The prefix for the line (e.g., 'EW', 'NS').

    Returns:
        pandas.DataFrame: The prepared DataFrame.
    """
    df = pd.read_csv(filepath)
    # Reorder columns to follow the line order (e.g., EW1, EW2, ...)
    station_cols = sorted(
        [col for col in df.columns if col.startswith(line_prefix)],
        key=lambda x: int(x[len(line_prefix):])
    )
    all_cols = ['Station'] + station_cols
    df = df[all_cols]
    return df

def basic_checks(df):
    """
    Performs and prints basic DataFrame checks.
    """
    print("--- Shape ---")
    print(df.shape)
    print("\n--- Info ---")
    df.info()
    print("\n--- Null Values ---")
    print(df.isnull().sum())
    print("\n--- Descriptive Statistics ---")
    print(df.describe())

# =============================================================================
# Task 3 & 7: Total Flow Analysis
# =============================================================================

def add_total_flow(df):
    """
    Calculates and adds a 'TotalFlow' column to the DataFrame.
    """
    df['TotalFlow'] = df.drop('Station', axis=1).sum(axis=1)
    return df

def plot_total_flow_per_station(df, title):
    """
    Plots a bar chart of the total passenger flow for each station.
    """
    df.sort_values('TotalFlow', ascending=False).plot(
        x='Station', y='TotalFlow', kind='bar', figsize=(12, 6),
        title=title, legend=False
    )
    plt.ylabel("Total Passenger Flow")
    plt.tight_layout()
    plt.show()

def get_top_bottom_stations(df, n=5):
    """
    Returns the top and bottom N stations by total flow.
    """
    sorted_df = df[['Station', 'TotalFlow']].sort_values('TotalFlow', ascending=False)
    top = sorted_df.head(n)
    bottom = sorted_df.tail(n)
    return top, bottom

# =============================================================================
# Task 4: Hourly/Segment Flow Analysis
# =============================================================================

def plot_flow_by_column(df, title):
    """
    Plots a bar chart summing passenger flow for each station code column.
    """
    flow_by_code = df.drop(['Station', 'TotalFlow'], axis=1, errors='ignore').sum().sort_index()
    flow_by_code.plot(kind='bar', figsize=(12, 5), title=title)
    plt.ylabel("Total Passenger Flow")
    plt.tight_layout()
    plt.show()

# =============================================================================
# Task 5: Heatmap Visualization
# =============================================================================

def plot_flow_heatmap(df, title):
    """
    Generates a heatmap of passenger flow by station.
    """
    plt.figure(figsize=(16, 10))
    sns.heatmap(df.set_index('Station').drop('TotalFlow', axis=1, errors='ignore'),
                cmap='YlGnBu', annot=False) # Annot set to False for clarity on larger datasets
    plt.title(title, fontsize=16)
    plt.show()

# =============================================================================
# Task 6: Station Clustering
# =============================================================================

def plot_station_clusters(df, n_clusters=3, title="Clustering Stations by Flow Pattern"):
    """
    Performs PCA and K-Means clustering to find stations with similar flow patterns.
    """
    X = df.drop(['Station', 'TotalFlow'], axis=1, errors='ignore')
    X_scaled = StandardScaler().fit_transform(X)

    # PCA for dimensionality reduction
    pca = PCA(n_components=2, random_state=42)
    X_pca = pca.fit_transform(X_scaled)

    # K-Means clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    labels = kmeans.fit_predict(X_scaled)

    # Plotting
    plt.figure(figsize=(10, 8))
    sns.scatterplot(x=X_pca[:, 0], y=X_pca[:, 1], hue=labels, palette='viridis', s=100)
    
    # Annotate points with station names
    for i, txt in enumerate(df['Station']):
        plt.annotate(txt, (X_pca[i, 0], X_pca[i, 1]), textcoords="offset points", xytext=(0,5), ha='center')
        
    plt.title(title, fontsize=16)
    plt.xlabel("Principal Component 1")
    plt.ylabel("Principal Component 2")
    plt.grid(True)
    plt.show()


# =============================================================================
# Task 8: Summary Table
# =============================================================================

def create_summary_table(df):
    """
    Creates a summary table with total flow, busiest, and least used station codes.
    """
    # Exclude non-station-code columns before finding min/max
    station_code_df = df.drop(['Station', 'TotalFlow'], axis=1, errors='ignore')

    summary = pd.DataFrame({
        'Station': df['Station'],
        'Total Flow': df['TotalFlow'],
        'Busiest Code': station_code_df.idxmax(axis=1),
        'Least Used Code': station_code_df.idxmin(axis=1),
    })
    return summary.sort_values('Total Flow', ascending=False).reset_index(drop=True)