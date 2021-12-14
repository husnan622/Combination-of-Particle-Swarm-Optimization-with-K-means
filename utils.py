import numpy


def normalize(x: numpy.ndarray):
    return (x - x.min(axis=0)) / (x.max(axis=0) - x.min(axis=0))


def standardize(x: numpy.ndarray):
    return (x - x.mean(axis=0)) / numpy.std(x, axis=0)

def maximum_absolute_scaling(df):
    df_scaled = df.copy()
    for column in df_scaled.columns:
        df_scaled[column] = df_scaled[column]  / df_scaled[column].abs().max()
    return df_scaled