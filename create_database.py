import prettytable
import CifFile

#obtain the protein data
cf = CifFile.ReadCif("20gs.cif")
all_data = cf.first_block()
atom_data = all_data.GetLoop("_atom_site.group_PDB")

#create a text file for the atom coordinates
file = open("atom_coordinates.txt", "w")
xyz_table = prettytable.PrettyTable(["atom", "amino", "X", "Y", "Z"])

#add rows to xyz_table
for a in atom_data:
    print(a[11], a[12], a[13])

#add rows to xyz_table
for a in atom_data:
    xyz_table.add_row([a[2], a[5], a[10], a[11], a[12]])

#print the xyz_table
print(xyz_table)

#output pretty table to textfile
with open('atom_coordinates', 'w') as w:
    w.write(str(xyz_table))
