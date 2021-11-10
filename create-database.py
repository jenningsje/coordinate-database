
import CifFile
import pandas as pd
import io
from pathlib import Path
import gzip
import sys
import os

directory = input("Enter the path of your file: ")
df = pd.DataFrame()
for crystal_file in Path(directory).glob('*.cif.gz'):

    if str(crystal_file) != "posix.DirEntry":

        with gzip.open(crystal_file, 'rb') as ip:
            cf = CifFile.ReadCif(ip)
            all_data = cf.first_block()
            atom_data = all_data.GetLoop("_atom_site.group_PDB")
            df1 = pd.DataFrame.from_dict(atom_data)
            df1=df1.assign(protein_id=lambda x : all_data['_pdbx_database_status.entry_id'])
            print(df1)
            df = df.append(df1, ignore_index=True)

print(df)
df.to_csv("df.csv")
