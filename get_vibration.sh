#!/bin/sh
#edge by lipai@mail.ustc.edu.cn
pos2xyz.pl POSCAR
n=`grep PiTHz OUTCAR |wc -l`
awk '/PiTHz/,/POTIM/{print $4" "$5" "$6}' OUTCAR> tmp
awk 'BEGIN{RS="\n  \n"}{a++}{print >"tmp_"a}' tmp
for i in `seq 1 $n`
do
sed -i "1,2s/.*/ /" tmp_$i
paste -d " " POSCAR.xyz tmp_$i >vib_$i.xyz
done
rm tmp*
mkdir vib
mv vib_* vib
