# This file contains the function needed to create a summary across all tubes of a chosen parameter

# import required packages
import pandas as pd

# import other functions
from make_list_func import *

def all_tube_data(folder:str, extension:str, parameter:str):
    
    """
    Function creates a list containing all data points for chosen variable across many dataframes
    
    Parameters:
        folder: Folder path to where data files are stored
        extension: Extension of data files (i.e. .txt)
        parameter: Variable of interest as named in the data files (i.e. "Resolution[um]")

    """
    data=[]                                                                 # Create master list where values of variable will be stored for all chambers
    file_names=makelist(folder, extension)                                  # Create list of data files
    
    for i in file_names:                                                    # Loop through list of data files                                                 
        df = pd.read_csv(folder+"\\"+i, delimiter=",")                      # Create dataframe for selected chamber from data file
        df=df.loc[(df['Resolution[um]']>0) & (df['Efficiency']>0)]          # Select alive tubes only
        values=df[parameter].tolist()                                       # Create list of all values in dataframe of the variable of interest
        data+=values                                                        # Add values in list for this chamber to master list 
        
    return data