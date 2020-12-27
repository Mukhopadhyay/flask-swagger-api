import os
import pickle
import pandas as pd

def save_as_pkl(obj, path:list) -> None:
    steps = os.path.split(path) if isinstance(path, str) else path
    if os.path.exists(os.path.join(*steps[:-1])):
        save_loc = os.path.join(*path) if isinstance(path, list) else path
        with open(save_loc, 'wb') as file:
            pickle.dump(obj, file)
        print(f'[IO] File saved at {save_loc}')
    else:
        raise NotImplementedError

def read_from_pkl(path:list) -> pd.DataFrame:
    steps = os.path.split(path) if isinstance(path, str) else path
    if os.path.exists(os.path.join(*steps[:-1])):
        read_loc = os.path.join(*path) if isinstance(path, list) else path
        with open(read_loc, 'rb') as file:
            return pickle.load(file)
    else:
        raise NotImplementedError

