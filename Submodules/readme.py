""" 
Name: Matthew Nale
    Date of Last Edit: 2/5/2023
    
    Purpose: Performs all README operations, which can be called from any other function

    Details: Lists and controls all README operations, such as checking for licensing

"""

import git                                                                  #Using GitPython for 'import git'
import os

def checkLicensing(repo):
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

def checkLength(repo):
    numLines = 0
    try:
        targetFile = os.path.join(repo.working_tree_dir, 'README.md')       
        with open(targetFile, 'r') as f:                                    
            for line in f:                                                  #Line by line, checks if lines is non-blank (i.e. actual content), and adds one to counter if true
                if(line.strip()):
                    numLines += 1
    except:
        print("No possible README to analyze")                              #If cannot open README (doesn't exist), numLines stays 0, which will cause a weight of zero
    return numLines