# In plot_utils.py
import matplotlib.pyplot as plt

def plot_avg_arrival_gap(station_stats):
    plt.figure(figsize=(12, 6))
    plt.barh(station_stats['Stations'], station_stats['Avg_Gap'], color='skyblue')
    plt.xlabel('Average Arrival Gap (minutes)')
    plt.title('Average Arrival Gap by Station')
    plt.tight_layout()
    plt.show()

def plot_top_avg_gaps(station_stats, top_n=10):
    top = station_stats.nlargest(top_n, 'Avg_Gap')
    plt.figure(figsize=(12, 6))
    plt.barh(top['Stations'], top['Avg_Gap'], color='orange')
    plt.xlabel('Average Arrival Gap (minutes)')
    plt.title(f'Top {top_n} Busiest Stations by Average Arrival Gap')
    plt.tight_layout()
    plt.show()

def plot_dwell_time_extremes(df_pivot, top_n=10):
    dwell = df_pivot.groupby('Stations')['Dwell Time'].mean()
    top = dwell.nlargest(top_n)
    bottom = dwell.nsmallest(top_n)

    plt.figure(figsize=(10, 5))
    plt.barh(top.index, top.values, color='green')
    plt.xlabel('Average Dwell Time (minutes)')
    plt.title(f'Longest Dwell Times (Top {top_n})')
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 5))
    plt.barh(bottom.index, bottom.values, color='red')
    plt.xlabel('Average Dwell Time (minutes)')
    plt.title(f'Shortest Dwell Times (Bottom {top_n})')
    plt.tight_layout()
    plt.show()


def plot_dwell_time_distribution(df_sorted):
    
    plt.figure(figsize=(14, 8))
    plt.barh(df_sorted["Stations"], df_sorted["Avg_Gap"], xerr=df_sorted["Gap_Std"], capsize=4)
    plt.xlabel("Average Gap (minutes)")
    plt.title("Station Gap Analysis: Avg_Gap with Std Deviation")
    plt.grid(True, axis='x', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()
