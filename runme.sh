mkdir -p $HOME/scripts
cd ../
mv ./MKTLAB_scripts_VASP $HOME/scripts
cd $HOME/scripts/MKTLAB_scripts_VASP
chmod +x *py *sh
chmod -x runme.sh
echo 'export PATH=$HOME/scripts/MKTLAB_scripts_VASP:$PATH' >> ~/.bashrc
echo 'module load anaconda3/5.1.10' >> ~/.bashrc
source ~/.bashrc
