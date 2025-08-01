# import required packages
import matplotlib.pyplot as plt
from summary_func import *

def make_hist(data, parameter:str, binning: int, rootmeansq:float, standarddev:float, output_path:str):
    
        """
        Function creates a histogram using the data for a chosen parameter

        Parameters:
                data: array of all data points to be plotted on histogram
                parameter: variable of interest as named in the data files (i.e. "Resolution[um]")
                binning: integer number of bins desired for histogram
                rootmeansq: value of RMS from summary_stats_func
                standarddev: value of std dev from summary_stats_func

        """
        rms_string="RMS: "+str(round(rootmeansq, 2))
        std_string="STD Dev: "+str(round(standarddev,2))

        if parameter=="T0[ns]":
                title="T0"
        elif parameter=="TMax[ns]":
                title="TMax"
        elif parameter=="ADC_peak[ns]":
                title="ADCpeak"
        elif parameter=="ADC_width[ns]":
                title="ADCwidth"
        elif parameter=="Resolution[um]":
                title="Resolution"
        elif parameter=="Efficiency":
                title="Efficiency"
        fig,ax = plt.subplots()
        ax.hist(data, bins=binning, histtype="step", facecolor="none", edgecolor="blue")
        plt.title(parameter+ " of All Tubes in UM Chambers")
        plt.xlabel(parameter)
        plt.ylabel("Number of tubes")
        plt.text(.7, .85, rms_string, transform = ax.transAxes,
                bbox = dict(facecolor = 'blue', alpha = .2))
        plt.text(.7, .75, std_string, transform = ax.transAxes,
                bbox = dict(facecolor = 'blue', alpha = .2))
        plt.savefig(output_path+"/"+ title+".png", bbox_inches="tight")
        plt.close()



