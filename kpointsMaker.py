#!/usr/bin/env python3
#this is for linux system
import os

print("\nThis scrip is for making KPOINTS of VASP!!\n")
sysname=input("system name: ")
point=input("\nGamma centered or Monkhorst-Pack (G/M): ")
if point!="G" and point!="g" and point!="M" and point!="m":
    print("\nGrid is not allow!!\n")
    quit()
if point=="G" or point=="g":
    point=["Gamma"]
else:
    point=["Monkhorst"]
A=input("\n(a, b, c) plz input a b c:").split()
kpoints=[[sysname],[" 0"],point,A,["0", "0", "0"]]

pwd=os.getcwd()+"/KPOINTS"
with open(pwd, mode="w") as file:
    for i in range(len(kpoints)):
        for j  in range(len(kpoints[i])):
            file.write(str(kpoints[i][j])+'  ')
        file.write("\n")
