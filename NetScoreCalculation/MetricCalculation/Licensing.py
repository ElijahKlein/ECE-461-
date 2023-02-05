""" Name: Matthew Nale
    Date of Last Edit: 2/5/2023
    
    Purpose: Calculate Licensing Sub Metric of a given GitHub Repository

    Details: Scans the README file of the given repository and returns a binary value for if the Repository has compatible licensing with the ACME Corporation. If not in README, will also
    check for existance of a LICENSE file for compatable licensing
    
"""
#Using GitPython for 'import git'
import git
import os
                                                                            #Checks if the README exists, and evaluates it if it does
def evaluate_readme(repo):
    scoring = 0
    try:                                                                    #Open the targetFile (README) for compatability checking
        targetFile = repo.working_tree_dir
        with open(os.path.join(targetFile, 'README.md'), 'r') as f:
            if(f.read().find('MIT License')):
                scoring = 1
            else:                                                           #If not located in the README, check the LICENSE file for compatability
                try:
                    with open(os.path.join(targetFile, 'LICENSE')) as f:
                        if(f.read().find('MIT License')):
                            scoring = 1
                except:
                    scoring = 0
        f.close()
    except:                                                                 #If the clone_from fails, the scoring automatically is a 0, as there is not README to check for compatability
        scoring = 0
        
    return scoring