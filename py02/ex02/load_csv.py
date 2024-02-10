from pandas import DataFrame as Dataset, read_csv


def load(path: str) -> Dataset:
    """Returns a dataset from the provided CSV file"""
    try:
        if read_csv(path).empty:
            return None
    except FileNotFoundError:
        return None
    ds = read_csv(path)
    print("Loading dataset of dimensions", ds.shape)
    return ds
