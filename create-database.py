# import libraries
import CifFile
import pandas as pd
import io
from pathlib import Path
import gzip
import sys
import os
import shutil


#Step 1 (yes response): move files to a directory of users choice
for file in files:

    file_name = os.path.join(source, file)
    shutil.move(file_name, destination)

    print("your files have just been moved")
    print("to the following directory:" + str(destination))
