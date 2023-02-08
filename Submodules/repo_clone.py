""" Name: Matthew Nale
    Date of Last Edit: 2/5/2023
    
    Purpose: Cloning the given repository from the provided URL. 

    Details: When provided a valid URL, a local clone of the repository is made in the local 'temp' folder, and the Repo object is returned
    
"""

import git
import os.path as path 

def clone_repo(url):
    try:
        file_loc = path.dirname(__file__) + '/../clone_dir/' + path.basename(url)
        clonedRepo = git.Repo.clone_from(url, file_loc)       #Clones the repo from the provided URL into 'clone_dir' and returns the Repo (GitPython) structure
        return clonedRepo
    except:
        print("Error, provide new valid repository URL")                                #Cloning failed, provides an error code