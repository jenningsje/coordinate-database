import CifFile
import pandas as pd
import io
from pathlib import Path
import gzip
import sys
import os
import shutil

#description of program
print("this program will loop through a directory containing gzipped files")
print("and compress the data within the block _atom_site.group_PDB")
print("in each gzipped file into a single csv file")
print("within a single csv file")

#computer gives user the option of moving all of their cif files
#within subdirectories to a single directory of their choice
print("if your gzipped cif files are all located within a single directory")
print("it is recommended that you move them to a single directory of your choice?")
print("would you like to do this? (y/n)")

switch (input())
case ("y")
    print("please type in the directory containing all of your gizpped files")
    input(source)
    print("please type in the directory you wish to move your gzipped files to")
    files = os.listdir(source)

for file in files:
    file_name = os.path.join(source, file)
    shutil.move(file_name, destination)
    print("your files have just been moved")
    print("to the following directory:" + str(destination))
    df_a = pd.DataFrame()

for crystal_file in Path(destination).glob('*.cif.gz'):
    #check if the file is a gzipped crystallographic information file
    if str(crystal_file).endswith('.cif.gz'):
    #read the gzipped files
        with gzip.open(crystal_file, 'rb') as ip:
        #check if the file contains crystallographic inforamtion
        #data about a protein

        #if so run the following code below
            if '_atom_site.group_PDB' in ip:
                cf = CifFile.ReadCif(ip)
                all_data = cf.first_block()
                atom_data = all_data.GetLoop("_atom_site.group_PDB")
                df1 = pd.DataFrame.from_dict(atom_data)
                df1=df1.assign(protein_id=lambda x : all_data['_pdbx_database_status.entry_id'])
                print(df1)
                df_a = df_a.append(df1, ignore_index=True)
            else:
    else:
                #skip this crysllographic information file
case ("n")
    directory = input("Enter the path of your crystallographic information files: ")
    df = pd.DataFrame()

    for crystal_file in Path(directory).glob('*.cif.gz'):

    if str(crystal_file).endswith('.cif.gz'):

        with gzip.open(crystal_file, 'rb') as ip:
            cf = CifFile.ReadCif(ip)
            all_data = cf.first_block()
            atom_data = all_data.GetLoop("_atom_site.group_PDB")
            df1 = pd.DataFrame.from_dict(atom_data)
            df1=df1.assign(protein_id=lambda x : all_data['_pdbx_database_status.entry_id'])
            print(df1)
            df = df.append(df1, ignore_index=True)

    print(df)
    if df.empty
        print("Dataframe is empty")
        print("this means that either:")
        print("1: you misspelled in the command prompt")
        print("2: the directory does not exist")
        print("3: the files are not crystallographic information files")
        print("4: your crystallographic information files are empty")
        df.to_csv("df.csv")
    else
        df.to_csv("df.csv")
    break;

    default
    "please enter a yes or no response"
}
