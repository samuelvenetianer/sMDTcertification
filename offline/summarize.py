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
path_to_files = r"C:\Users\svene\OneDrive\Documents\Tufts\Research\qual\eye_scanning\Cosmic_Data"
extension_of_files = ".txt"
output_path= r"C:\Users\svene\OneDrive\Documents\Tufts\Research\qual\functions\summary_plots"
hist_bins=100

# check if stats file exists
exists=os.path.exists(output_path+"\\"+"stats.txt")
if exists==True:
    os.remove(output_path+"\\"+"stats.txt")

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
    histogram = make_hist(all_data, i, hist_bins, rms, stddev)
