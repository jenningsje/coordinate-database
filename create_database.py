import CifFile
import pandas as pd
import io
from pathlib import Path
import gzip

directory = '/home/james/Desktop/Move_to_Linux/all_mmcifs'
df = pd.DataFrame()

for crystal_file in Path(directory).glob('*.cif.gz'):

    if str(crystal_file) != "posix.DirEntry":

        with gzip.open(crystal_file, 'rb') as ip:
            cf = CifFile.ReadCif(ip)
            all_data = cf.first_block()
            atom_data = all_data.GetLoop("_atom_site.group_PDB")
            df1 = pd.DataFrame.from_dict(atom_data)
            print(df1)
            df1.assign(protein_id=[])
            df = df.append(df1, ignore_index=True)

print(df)
df.to_csv("df.csv")
print(df.csv)
