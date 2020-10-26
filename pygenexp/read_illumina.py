import pandas as pd
import GEOparse


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
