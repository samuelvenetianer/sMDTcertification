# import required modules
import numpy as np

def calc_rms(data, parameter:str):
    """
    Function calculates root mean square of provided array
    
    Parameters:
        data: values of interest
        parameter: label of interest for printing result
 
    """
    squared=np.square(data)
    rms=np.sqrt(np.sum(squared)/len(data))
    print("Root Mean Squared of", parameter, "is: ", rms)
    
    return rms

def calc_stddev(data, parameter:str):

    """
    Function calculates standard deviation of provided array
    
    Parameters:
        data: values of interest
        parameter: label of interest for printing result

    """
    std_dev=np.std(data)
    print("Standard Deviation of", parameter, "is: ", std_dev)

    return std_dev


