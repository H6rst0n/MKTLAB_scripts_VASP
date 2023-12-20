#!/usr/bin/env python3
import sys
import modules.mathBetweenAtoms as mathbetweenatoms

# read file
file_name=sys.argv[1:]

## for first file
with open(file_name[0],"r") as f:
    file=[x.split() for x in f]

# Make sure the system is not direct
selection=file[7][0]
if selection[0]=="S" or selection[0]=="s":
    coor=file[8][0]
    start_num=9
    if coor[0]=="D" or coor[0]=="d":
        file=mathbetweenatoms.D2C(file)
        file[8][0]="Cartesian"
else:
    coor=file[7][0]
    start_num=8
    if coor[0]=="D" or coor[0]=="d":
        file=mathbetweenatoms.D2C(file)
        file[7][0]="Cartesian"

atoms_num=sum([int(x) for x in file[6]])        
atom2num={}
# print("\nThe system have "+str(atoms_num)+' atoms.')                #!!!!!!!!!!!!!!!!number of total atoms
for i in range(len(file[5])):
    atom2num[str(file[5][i])]=int(file[6][i])
# print(atom2num)                                                     #!!!!!!!!!!!!!!atom spice and number

# Which atoms to consider
# atomtoconsider=input("Which atoms to consider (65 70):").split()     #!!!!!!!!!!!!!!!!interactive range of consider atoms
atomtoconsider=[65,70]                                                #!!!!!!!!!!!!!!!!for Cu111 ads HOCCOH molecular

i = int(atomtoconsider[0])
massOfAllAtom_x=float(0)
massOfAllAtom_y=float(0)
massOfAllAtom_z=float(0)
allmass=float(0)

while i <= int(atomtoconsider[1]):
    # getting mass of atom
    column=0
    aaa=int(file[6][column])
    while i > aaa:
        column+=1
        aaa+=int(file[6][column])
    atomspice=file[5][column]
    i+=1
    atomicmass=float(mathbetweenatoms.massDataOfatom(atomspice))

    atomnumber=int(start_num + i - 2)
    massOfAtom_x, massOfAtom_y, massOfAtom_z = mathbetweenatoms.massXposition(atomicmass, float(file[atomnumber][0]), float(file[atomnumber][1]), float(file[atomnumber][2]))
    massOfAllAtom_x += massOfAtom_x
    massOfAllAtom_y += massOfAtom_y
    massOfAllAtom_z += massOfAtom_z
    allmass += atomicmass

masscenter_x_1=massOfAllAtom_x/allmass
masscenter_y_1=massOfAllAtom_y/allmass
masscenter_z_1=massOfAllAtom_z/allmass

## for second file
with open(file_name[1],"r") as f:
    file=[x.split() for x in f]

# Make sure the system is not direct
selection=file[7][0]
if selection[0]=="S" or selection[0]=="s":
    coor=file[8][0]
    start_num=9
    if coor[0]=="D" or coor[0]=="d":
        file=mathbetweenatoms.D2C(file)
        file[8][0]="Cartesian"
else:
    coor=file[7][0]
    start_num=8
    if coor[0]=="D" or coor[0]=="d":
        file=mathbetweenatoms.D2C(file)
        file[7][0]="Cartesian"

atoms_num=sum([int(x) for x in file[6]])        
atom2num={}

for i in range(len(file[5])):
    atom2num[str(file[5][i])]=int(file[6][i])

i = int(atomtoconsider[0])
massOfAllAtom_x=float(0)
massOfAllAtom_y=float(0)
massOfAllAtom_z=float(0)
allmass=float(0)

while i <= int(atomtoconsider[1]):
    # getting mass of atom
    column=0
    aaa=int(file[6][column])
    while i > aaa:
        column+=1
        aaa+=int(file[6][column])
    atomspice=file[5][column]
    i+=1
    atomicmass=float(mathbetweenatoms.massDataOfatom(atomspice))

    atomnumber=int(start_num + i - 2)
    massOfAtom_x, massOfAtom_y, massOfAtom_z = mathbetweenatoms.massXposition(atomicmass, float(file[atomnumber][0]), float(file[atomnumber][1]), float(file[atomnumber][2]))
    massOfAllAtom_x += massOfAtom_x
    massOfAllAtom_y += massOfAtom_y
    massOfAllAtom_z += massOfAtom_z
    allmass += atomicmass

masscenter_x_2=massOfAllAtom_x/allmass
masscenter_y_2=massOfAllAtom_y/allmass
masscenter_z_2=massOfAllAtom_z/allmass


## Gravity center Diff of two system
diff=mathbetweenatoms.distance(masscenter_x_1, masscenter_y_1, masscenter_z_1, masscenter_x_2, masscenter_y_2, masscenter_z_2)
print("The difference between the centroid molecules =",diff,"A.")
