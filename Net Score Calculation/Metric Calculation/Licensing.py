""" Name:
    Date of Last Edit: 2/4/2023
    
    Purpose: Calculate Licensing Sub Metric of a given GitHub Repository

    Details: Scans the README file of the given repository and returns a binary value for if the Repository has compatible licensing with the ACME Corporation 
    
"""
import git
import sys
import os

#Checks if the README exists, and evaluates it if it does
def evaluate_readme(repo):
    scoring = 0
    try:
        #Clones the repo into temp. Can be quite slow so potential optimizations may be necessary
        clonedRepo = git.Repo.clone_from(repo, 'C:/temp/' + os.path.basename(repo))
        targetFile = clonedRepo.working_tree_dir
        with open(os.path.join(targetFile, 'README.md'), 'r') as f:
            if(f.read().find('MIT License')):
                scoring = 1
            else:
                try:
                    with open(os.path.join(targetFile, 'LICENSE')) as f:
                        if(f.read().find('MIT License')):
                            scoring = 1
                except:
                    scoring = 0
        f.close()
    except:
        #If the clone_from fails, the scoring automatically is a 0, as there is not README to check the liscensing
        scoring = 0
        
    return scoring
        

#For testing of the function, use the below code. It takes one arguement, which is the url of the github repository to check for the correct 
repo = sys.argv[1]
scoring = evaluate_readme(repo)
print(scoring)