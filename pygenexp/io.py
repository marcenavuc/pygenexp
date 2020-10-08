import pandas as pd
import GEOparse
import csv
import os
import re


def read_illumina(filename):
    df = pd.read_csv(filename, sep="\t")
    return df


def read_illumina(filename, GSE="GSE40561"):
    df = pd.read_csv(filename, sep="\t")
    df.columns = ["Probe_Id"] + list(df.columns[1:])
    cols = list(filter(lambda x: not x.startswith("Detect"), df.columns))
    df = df[cols]
    res_df = pd.DataFrame()
    res_df["Probe_Id"] = df["Probe_Id"]
    gse = GEOparse.get_GEO(GSE)
    geneNames = list(gse.gsms.keys())

    for gene in geneNames:
        new_df = pd.DataFrame()
        new_df["Probe_Id"] = gse.gsms[gene].table["ID_REF"]
        new_df[gene] = gse.gsms[gene].table["VALUE"]
        res_df = pd.merge(res_df, new_df)

    return res_df


def read_ngd(filename):
    pass


def read_xys(xys_files, sep="\t"):
    for xys_file in xys_files:
        assert xys_file.endswith('.xys'), "You must specify the path to the .xys files"
        assert os.path.exists(xys_file), "One of the .xys files does not exist"
    new_df = pd.DataFrame()

    for xys in xys_files:
        xys_df = pd.read_csv(xys, sep=sep, skiprows=1)  # TO DO: add param
        assert ("SIGNAL" in xys_df), ".xys file must contain 'SIGNAL' column"
        new_df[os.path.basename(xys)] = xys_df['SIGNAL']

    return new_df


def read_bgx(filename):
    meta_data = {}
    with open(filename) as file:
        csv_reader = csv.reader(file, delimiter="\t")
        for i, line in enumerate(csv_reader):
            if len(line) > 1:
                meta_data[line[0]] = line[1]
            if line[0] == "[Probes]":
                break

    return meta_data, pd.read_csv(filename, sep="\t", skiprows=i)


