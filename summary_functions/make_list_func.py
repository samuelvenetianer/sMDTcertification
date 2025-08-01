# This file contains the function needed to create a list of all files in a folder with a specified extension

# import required packages
import os                                       

# function definition
def makelist(folder:str, extension:str):

    """
    Function creates a list of all files in a folder with the specified extension
    
    Parameters:
        folder: Folder path to where files of interest are stored
        extension: Extension of files of interest (i.e. .txt)
 
    """

    selected_files=[]                           # Define empty list that will store files of interest
    all_files=os.listdir(folder)                # Make list of all files in folder

    for i in all_files:                         # Loop through all files in folder
        if extension in i:
            selected_files.append(i)            # Append files with specified extension to master list

    return selected_files
