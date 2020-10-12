import numpy as np
import pandas as pd


def quantile_normalization(df):
    # From https://github.com/ShawnLYU/Quantile_Normalize
    work_df = df.copy()
    dic = {column: sorted(work_df[column]) for column in work_df}

    sorted_df = pd.DataFrame(dic)
    rank = sorted_df.mean(axis=1).tolist()
    # sort
    for col in work_df:
        t = np.searchsorted(np.sort(work_df[col]), work_df[col])
        work_df[col] = [rank[i] for i in t]
    return work_df
