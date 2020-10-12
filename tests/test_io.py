import os
import sys

import pandas as pd
import pytest

from pygenexp.io import read_xys


@pytest.yield_fixture()
def set_path():
    print(sys.path[0])
    os.chdir(sys.path[0])
    yield
    os.chdir("../")


def test_read_xys(set_path):
    xys_files = list(
        filter(lambda x: x.endswith(".xys"), os.listdir("tests_data/xys/"))
    )

    xys_files = list(
        map(lambda dir_name: os.path.join("tests_data/xys/", dir_name), xys_files)
    )

    df1 = read_xys(xys_files)

    df2 = pd.read_csv("tests_data/xys.csv", sep=",")
    df2 = df2.drop(df2.columns[0], axis=1)

    df1 = df1.dropna()
    df2 = df2.dropna()

    assert set(df1.columns) == set(df2.columns)

    for col in df1.columns:
        assert df1[col].equals(df2[col])
