# import required packages
import matplotlib.pyplot as plt
import os
import os.path

# import other functions
from hist_func import *
from make_list_func import *
from summary_func import *
from summary_stats_func import *

# define inputs
path_to_files = "/net/ustc_01/users/lich/muon/results"
extension_of_files = ".txt"
output_path= "/home/svenetia/sMDTcertification/output/summary"
hist_bins=100

# check if stats file exists
exists=os.path.exists(output_path+"/"+"stats.txt")
if exists==True:
    os.remove(output_path+"/"+"stats.txt")

# specify parameters of interest

all_param=[
    'T0[ns]', 
    'TMax[ns]',
    'ADC_peak[ns]', 
    'ADC_width[ns]', 
    'Resolution[um]', 
    'Efficiency'
    ]

for i in all_param:
    all_data = all_tube_data(path_to_files, extension_of_files, i)
    rms=calc_rms(all_data, i, output_path)
    stddev=calc_stddev(all_data, i, output_path)
    histogram = make_hist(all_data, i, hist_bins, rms, stddev, output_path)
