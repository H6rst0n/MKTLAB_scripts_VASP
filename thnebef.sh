echo 'step of NEB ??'
read step
echo "" >> note.txt
echo "=====> $step <=====" >> note.txt
nebef.pl >> note.txt

tail -15 ./note.txt
