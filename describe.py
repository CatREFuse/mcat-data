import pandas as pd
import numpy as np
from scipy import stats

def summary(df):
    summary_df = pd.DataFrame(columns=['column_name', 'sample_size', 'mean', 'std', 'std_error', 'ci_lower', 'ci_upper', 'min', 'max'])
    
    for column in df.columns:
        data = df[column]
        n = len(data)
        mean = np.mean(data)
        std = np.std(data)
        std_error = std / np.sqrt(n)
        ci = stats.t.interval(0.95, n-1, loc=mean, scale=std_error)
        ci_lower = ci[0]
        ci_upper = ci[1]
        minimum = np.min(data)
        maximum = np.max(data)
        
        summary_df = summary_df.append({'column_name': column, 'sample_size': n, 'mean': mean, 
                                        'std': std, 'std_error': std_error, 'ci_lower': ci_lower, 
                                        'ci_upper': ci_upper, 'min': minimum, 'max': maximum}, ignore_index=True)
    
    return summary_df