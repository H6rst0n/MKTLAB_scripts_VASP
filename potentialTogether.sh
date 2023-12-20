for i in `ls -d s*|sort -V`;do 
cd $i
echo -e "426\n3\n"|vaspkit
sleep 5
cd ..
done

awk 'NR>1{printf "%8s\n", $1}' s1/PLANAR_AVERAGE.dat > total.dat
for i in `ls -d s*|sort -V`;do 
awk 'NR>1{printf "%8s\n", $2}' $i/PLANAR_AVERAGE.dat > tmp
paste total.dat tmp > totmp
mv totmp total.dat
done
rm tmp -f
