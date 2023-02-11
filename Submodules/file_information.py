""" 
Name: Matthew Nale
    Date of Last Edit: 2/11/2023
    
    Purpose: Used for performing analysis on cloned local files from the given repository

    Details: Has multiple functions that can be called to obtain information about all files/specific files

"""

import os
import sys
import Submodules.global_var as gv

def getDirectorySize(url):
    try:
        repo = gv.token.get_repo(url.split("github.com/", 1)[1])
        return repo.size
    except:
        print("Error in file_information.py")