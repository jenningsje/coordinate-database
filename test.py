import CifFile
import pandas as pd
import io
from pathlib import Path
from CifFile import CifBlock
import gzip

cf = CifFile.ReadCif("1a0j.cif")
all_data = cf.first_block()
print(all_data['_database_2.database_id'])
