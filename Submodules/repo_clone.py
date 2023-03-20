""" Name: Matthew Nale, Eric Chen 
    Date of Last Edit: 2/8/2023
    
    Purpose: Cloning the given repository from the provided URL. 

    Details: When provided a valid URL, a local clone of the repository is made in the local 'clone_dir' folder, and the Repo object is returned
    
"""

import git #GitPython'

import Submodules.global_var as gv
import os.path as path

def clone_repo(url):
    try:
        gv.set_file_loc(url)
        return git.Repo.clone_from(url, gv.file_loc)                                                #Clones the repo from the provided URL into 'clone_dir' and returns the Repo (GitPython) structure
    except:
        if(path.exists(path.dirname(__file__) + '/../clone_dir/' + path.basename(url))):
            try:
                return git.Repo(path.dirname(__file__) + '/../clone_dir/' + path.basename(url))     #If the path already exists (Already cloned locally), return the Repo object of the instance
            except: 
                print("Error, provide new valid repository URL")                                    #Cloning failed, provides an error code