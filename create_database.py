# 1. import libraries
import prettytable
import CifFile
import glob
import io
import gzip
from pathlib import Path
import zipfile


cf = CifFile.ReadCif("20gs.cif")
all_data = cf.first_block()
atom_data = all_data.GetLoop("_atom_site.group_PDB")
