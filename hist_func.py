# import required packages
import matplotlib.pyplot as plt

def make_hist(data, parameter:str, binning: int):
    
    """
    Function creates a histogram using the data for a chosen parameter
    
    Parameters:
        data: array of all data points to be plotted on histogram
        parameter: variable of interest as named in the data files (i.e. "Resolution[um]")
        binning: integer number of bins desired for histogram

    """

    # once hist_func is made, have this all just be calling a function
    plt.hist(data, bins=binning, histtype="step", facecolor="none", edgecolor="blue")
    plt.title(parameter+ " of All Tubes in UM Chambers")
    plt.xlabel(parameter)
    plt.ylabel("Number of tubes")
    plt.show()


