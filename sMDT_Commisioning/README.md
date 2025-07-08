Steps for running certification analysis:

1. In terminal, run: <br/>
`setupATLAS` <br/>
`lsetup "root recommended"`<br/>

2. Run `run_all.sh` to create pdf of individual spectra, histograms, heatmaps, and stats output: <br/>
`bash run_all.sh Mod[]_BIS[]_CosmicRay_Thr[]`

Note:<br/> `analysis_functions.ipynb` has filtering functions and workshopping material for .py files<br/>
`all_mods_functions.ipynb` has functions for creating summary histos of parameters for all modules <br/>

Reminder for commiting changes: <br/>
`git add <file(s)>` <br/>
`git commit -m "commit message"` <br/>
`git push origin main` <br/>
