Steps for running certification analysis:

1. Open up `sMDTcertification/setup.sh` and check that the paths to your results and analysis directory are correct. `Results_Dir` points to the location of txt files generated from the cosmic analysis coding package, and `Analysis_Dir` points to the folder in `sMDTCertification` that has all of the python scripts required to process this txt file (should be `sMDTCertification/online`)<br/>
2. In terminal, write the command `source setup.sh` <br/>
This will set the results directory, the analysis directory, setup python and root, and cd to the analysis director.

2. Run `run_all.sh` from the analysis directory to create pdf of individual spectra, histograms, heatmaps, and stats output using the following command for a specfic module: <br/>
`bash run_all.sh Mod[]_BIS[]_CosmicRay_Thr[]` <br/>
Results will be saved in `sMDTcertification/output/<module_of_interest>`

3. In `sMDTcertification/summary_functions`, there are functions used for creating summary plots and statistics across multiple modules. To run, navigate to the folder and write: <br/>
`python summarize.py` <br/>
*Note that `summarize.py` calls other scripts in this folder. The other individual scripts cannot be run by themselves.

Reminder for commiting changes: <br/>
`git add <file(s)>` <br/>
`git commit -m "commit message"` <br/>
`git push origin main` <br/>
