Steps for running certification analysis:

1. In terminal, run: <br/>
`setupATLAS` <br/>
`lsetup "root recommended"`<br/>

2. In `online`, run `run_all.sh` to create pdf of individual spectra, histograms, heatmaps, and stats output: <br/>
`bash run_all.sh Mod[]_BIS[]_CosmicRay_Thr[]`

3. In `offline`, there are work in progress functions used for offline analysis including filtering and summarizing results across multiple modules.

Reminder for commiting changes: <br/>
`git add <file(s)>` <br/>
`git commit -m "commit message"` <br/>
`git push origin main` <br/>
