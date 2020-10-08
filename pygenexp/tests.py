import os
import pandas as pd
from pygenexp.io import read_xys


def test_5010():
    xys_files = list(filter(lambda x: x.endswith(".xys"), os.listdir("./test_data/5010/")))
    xys_files = list(map(lambda dir_name: os.path.join("./test_data/5010/", dir_name), xys_files))
    df1 = read_xys(xys_files)

    df2 = pd.read_csv("./test_data/5010.csv", sep=',')
    df2 = df2.drop(df2.columns[0], axis=1)

    assert df1.equals(df2)
