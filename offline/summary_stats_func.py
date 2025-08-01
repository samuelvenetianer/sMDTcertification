# import required modules
import numpy as np

def calc_rms(data, parameter:str, output_folder:str):
    """
    Function calculates root mean square of provided array
    
    Parameters:
        data: values of interest
        parameter: label of interest for printing result
 
    """
    squared=np.square(data)
    rms=np.sqrt(np.sum(squared)/len(data))
    # print("Root Mean Squared of", parameter, "is: ", rms)
    
    with open(output_folder+"/"+"stats.txt", 'a') as f:
        f.write("Root Mean Squared of "+ parameter+ " is: "+ str(rms)+"\n")

    return rms

def calc_stddev(data, parameter:str, output_folder:str):

    """
    Function calculates standard deviation of provided array
    
    Parameters:
        data: values of interest
        parameter: label of interest for printing result

    """
    std_dev=np.std(data)
    #print("Standard Deviation of", parameter, "is: ", std_dev)
    
    with open(output_folder+"/"+"stats.txt", 'a') as f:
        f.write("Standard Deviation of "+ parameter+ " is: "+ str(std_dev)+ "\n")

    return std_dev


