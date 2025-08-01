# Create shortcut for important paths
echo 'Setting results directory...'
Results_Dir=/net/ustc_01/users/lich/muon/results/
echo $Results_Dir

echo 'Setting analysis directory...'
Analysis_Dir=/home/svenetia/sMDTcertification/online
echo $Analysis_Dir

setupATLAS
lsetup "root recommended"

cd $Analysis_Dir