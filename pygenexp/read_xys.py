import os
import pandas as pd


def read_xys(xys_files, sep="\t"):
    for xys_file in xys_files:
        assert xys_file.endswith(".xys"), "You must specify the path to the .xys files"
        assert os.path.exists(xys_file), "One of the .xys files does not exist"
    new_df = pd.DataFrame()

    for xys in xys_files:
        xys_df = pd.read_csv(xys, sep=sep, skiprows=1)  # TO DO: add param
        assert "SIGNAL" in xys_df, ".xys file must contain 'SIGNAL' column"
        new_df[os.path.basename(xys)] = xys_df["SIGNAL"]

    return new_df
