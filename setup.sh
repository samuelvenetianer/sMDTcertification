# Create shortcut for important paths
setupATLAS
lsetup "root recommended"

echo 'Setting results directory...'
Results_Dir=/net/ustc_01/users/lich/muon/results/
echo $Results_Dir

echo 'Setting analysis directory...'
Analysis_Dir=/home/svenetia/sMDTcertification/online
echo $Analysis_Dir

cd $Analysis_Dir