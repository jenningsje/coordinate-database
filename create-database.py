import CifFile
import pandas as pd
import io
from pathlib import Path
import gzip
import sys
import os

print("this program will loop through a directory containing gzipped files")
print("and compress the data within the block _atom_site.group_PDB")
print("in each gzipped file into a single csv file")
print("within a single csv file")

directory = input("Enter the path of your crystallographic information files: ")
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
if df.empty:
    print("Dataframe is empty")
    print("this means that either:")
    print("1: you misspelled in the command prompt")
    print("2: the directory does not exist")
    print("3: the files are not crystallographic information files")
    print("4: your crystallographic information files are empty")
df.to_csv("df.csv")
