import pandas as pd

def load_data(filepath):
    df = pd.read_csv(filepath)
    return df

# In data_cleaning_utils.py
def drop_high_nan_columns(df, threshold=0.9):
    nan_cols = df.columns[df.isna().mean() > threshold]
    print(f"Dropping columns with > {threshold*100}% NaNs:", list(nan_cols))
    return df.drop(columns=nan_cols)


# In train_schedule_utils.py
import pandas as pd

def melt_and_pivot_train_schedule(df):
    df = df.copy()
    df['arrival_departure'] = ['Arrival' if i % 2 == 0 else 'Departure' for i in range(len(df))]
    
    id_vars = ['Stations', 'station_id', 'arrival_departure']
    value_vars = [col for col in df.columns if col not in id_vars]
    
    df_melted = df.melt(id_vars=id_vars, value_vars=value_vars,
                        var_name='train_id', value_name='time')
    
    df_pivot = df_melted.pivot_table(
        index=['Stations', 'station_id', 'train_id'],
        columns='arrival_departure',
        values='time',
        aggfunc='first'
    ).reset_index()
    
    df_pivot['Arrival'] = pd.to_datetime(df_pivot['Arrival'], errors='coerce')
    df_pivot = df_pivot.rename(columns=lambda x: x.strip())  # Clean column names
    df_pivot['Departure'] = pd.to_datetime(df_pivot['Departure'], errors='coerce')
    
    return df_pivot


def calculate_dwell_time(df):
     
     df = df.copy()
     # Fill missing Arrival and Departure with station averages + overall fallback
     for col in ['Arrival', 'Departure']:
        station_avg = df.groupby('station_id')[col].transform('mean')
        overall_avg = df[col].mean(skipna=True)
        df[col] = df[col].fillna(station_avg).fillna(overall_avg)

     # Fix swapped times where Departure < Arrival
     neg_mask = df['Departure'] < df['Arrival']
     df.loc[neg_mask, ['Arrival', 'Departure']] = df.loc[neg_mask, ['Departure', 'Arrival']].values
     
     # Calculate dwell time (Departure - Arrival)
     df['Dwell Time'] = df['Departure'] - df['Arrival']
     return df

def calculate_dwell_time(df):
    df = df.copy()
    # Fill missing Arrival and Departure with station averages + overall fallback
    for col in ['Arrival', 'Departure']:
        station_avg = df.groupby('station_id')[col].transform('mean')
        overall_avg = df[col].mean(skipna=True)
        df[col] = df[col].fillna(station_avg).fillna(overall_avg)

    # Fix swapped times where Departure < Arrival
    neg_mask = df['Departure'] < df['Arrival']
    df.loc[neg_mask, ['Arrival', 'Departure']] = df.loc[neg_mask, ['Departure', 'Arrival']].values
    
    # Calculate dwell time (Departure - Arrival)
    df['Dwell Time'] = df['Departure'] - df['Arrival']
    
    return df

# In train_schedule_utils.py
def compute_station_gap_stats(df):
    df = df.copy()
    df_sorted = df.sort_values(['Stations', 'Arrival'])
    df_sorted['Next_Arrival'] = df_sorted.groupby('Stations')['Arrival'].shift(-1)
    df_sorted['Arrival_Gap'] = (df_sorted['Next_Arrival'] - df_sorted['Arrival']).dt.total_seconds() / 60

    df_gaps = df_sorted.dropna(subset=['Arrival_Gap'])

    station_stats = df_gaps.groupby('Stations')['Arrival_Gap'].agg(
        Avg_Gap='mean',
        Min_Gap='min',
        Max_Gap='max',
        Gap_Std='std'
    ).reset_index()

    station_stats = station_stats.sort_values('Avg_Gap')
    print("Computed station gap stats:")
    print(station_stats.head())

    return station_stats

def fill_missing_times_with_station_avg(df):
    df = df.copy()

    for col in ['Arrival', 'Departure']:
        station_avg = df.groupby('station_id')[col].transform('mean')
        overall_avg = df[col].mean(skipna=True)
        df[col] = df[col].fillna(station_avg).fillna(overall_avg)
        #print(f"Filled missing {col} times with station averages of {station_avg} and overall fallback of {overall_avg}.")

    return df

def check_null(df):
    print(df.isnull().mean() * 100)

