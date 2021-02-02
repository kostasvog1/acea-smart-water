import pandas as pd
from datetime import datetime, date

def get_time_features(df):
    df['year'] = df.Date.apply(lambda x: x.split('/')[2] if x==x else x)
    df['month'] = df.Date.apply(lambda x: x.split('/')[1]if x==x else x)
    df['day_in_year'] = df.Date.apply(lambda x: datetime(int(x.split('/')[2]), int(x.split('/')[1]), int(x.split('/')[0]), 0, 0).timetuple().tm_yday if x==x else x)
    df['week_in_year'] = df.day_in_year.apply(lambda x: int(x/7) if x==x else x)
    return df

def get_column_category(x):
    if 'Date' in x:
        return 'Date'
    elif 'Rainfall' in x:
        return 'Rainfall'
    elif 'Depth' in x:
        return 'Depth to Groundwater'
    elif 'Temperature' in x:
        return 'Temperature'
    elif 'Volume' in x:
        return 'Volume'
    elif 'Hydrometry' in x:
        return 'Hydrometry'
    elif 'Lake_Level' in x:
        return 'Lake Level'
    elif 'Flow_Rate' in x:
        return 'Flow Rate'
    else:
        return x
    
def remove_erroneous_temp_values(df, col):
    abnormal_temp_changes_mask = (abs(df[col].diff().shift(-1))>=10)
    implausible_imputed_values_mask = (df[col].shift() != df[col])
    return np.where(abnormal_temp_changes_mask | ~implausible_imputed_values_mask, np.nan, df[col])
