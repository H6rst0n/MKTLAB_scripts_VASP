#!/usr/bin/env python3
import sys
import modules.mathBetweenAtoms as mathbetweenatoms

file_name=sys.argv[1:]
with open(file_name[0],"r") as f1:
    file1=[x.split() for x in f1]
with open(file_name[1],"r") as f2:
    file2=[x.split() for x in f2]

# Make sure the system is the same
atomSpecies1=file1[5]
atomSpecies2=file2[5]
if atomSpecies1!=atomSpecies2:
    print("""
    Atoms of system is error!!!
    """)

# Make sure the system is not direct
    # system 1
selection1=file1[7][0]
if selection1[0]=="S" or selection1[0]=="s":
    coor1=file1[8][0]
    start_num1=9
    if coor1[0]=="D" or coor1[0]=="d":
        file1=mathbetweenatoms.D2C(file1)
        file1[8][0]="Cartesian"
else:
    coor1=file1[7][0]
    start_num1=8
    if coor1[0]=="D" or coor1[0]=="d":
        file1=mathbetweenatoms.D2C(file1)
        file1[7][0]="Cartesian"

    # system 2
selection2=file2[7][0]
if selection2[0]=="S" or selection2[0]=="s":
    coor2=file2[8][0]
    start_num2=9
    if coor2[0]=="D" or coor2[0]=="d":
        file2=mathbetweenatoms.D2C(file2)
        file2[8][0]="Cartesian"
else:
    coor2=file2[7][0]
    start_num2=8
    if coor2[0]=="D" or coor2[0]=="d":
        file2=mathbetweenatoms.D2C(file2)
        file2[7][0]="Cartesian"


atoms_num=sum([int(x) for x in file1[6]])        
atom2num={}
print("\nThe system have "+str(atoms_num)+' atoms.')
for i in range(len(file1[5])):
    atom2num[str(file1[5][i])]=int(file1[6][i])
print(atom2num)

atom=input("\nWhitch atom you wanna see ? (e.x. C 2) :\n").split()
while atom[0] not in file1[5]:
    print("Atom not in the system !!")
    atom=input("\nWhitch atom you wanna see ? (e.x. C 2) :\n").split()

column=0
row=0
while atom[0] != file1[5][column]:
    row+=int(file1[6][column])
    column+=1
else:
    row+=int(atom[1])
numberofatom1 = start_num1 + row - 1

column=0
row=0
while atom[0] != file2[5][column]:
    row+=int(file2[6][column])
    column+=1
else:
    row+=int(atom[1])
numberofatom2 = start_num2 + row - 1

dis=mathbetweenatoms.distance(file1[numberofatom1][0],file1[numberofatom1][1],file1[numberofatom1][2],file2[numberofatom2][0],file2[numberofatom2][1],file2[numberofatom2][2])
print("The distance between atom "+atom[0]+atom[1]+" = "+str(dis)+" A")
