""" Name: Matthew Nale
    Date of Last Edit: 2/5/2023
    
    Purpose: Cloning the given repository from the provided URL. 

    Details: When provided a valid URL, a local clone of the repository is made in the local 'temp' folder, and the Repo object is returned
    
"""

import git
import os

def clone_repo(url):
    try:
        return git.Repo.clone_from(url, 'C:/temp/' + os.path.basename(url))             #Clones the repo from the provided URL into 'temp' and returns the Repo (GitPython) structure
    except:
        if(os.path.exists('C:/temp/' + os.path.basename(url))):
            try:
                return git.Repo('C:/temp/' + os.path.basename(url))
            except: 
                print("Error, provide new valid repository URL")                        #Cloning failed, provides an error code