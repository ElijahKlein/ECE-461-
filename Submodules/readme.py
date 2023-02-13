""" 
Name: Matthew Nale
    Date of Last Edit: 2/12/2023
    
    Purpose: Performs all README operations, which can be called from any other function

    Details: Lists and controls all README operations, such as checking for licensing

"""

import git                                                                      #Using GitPython for 'import git'
import os

def checkLicensing(repo):
    for ext in [".md", ".markdown"]:            #Checking for multiple file extensions
        try:                                                                    
            targetFile = repo.working_tree_dir
            with open(os.path.join(targetFile, 'README' + ext), 'r') as f:
                if(f.read().find('MIT License') or f.read().find('LGPLv2.1 License')):
                    return 1
                else:                                                                               
                    try:
                        with open(os.path.join(targetFile, 'LICENSE')) as f:
                            if(f.read().find('MIT License') or f.read().find('LGPLv2.1 License')):
                                return 1
                            else:
                                return 0;
                    except:
                        pass
            f.close()
        except:                  #If the clone_from fails, the scoring automatically is a 0, as there is not README to check for compatability
            pass
    print("Error in checkLicensing")
    return -1;

def checkRMLength(repo):
    for ext in [".md", ".markdown"]:
        try:
            targetFile = os.path.join(repo.working_tree_dir, 'README' + ext)                                    
            numLines = sum(1 for line in open(targetFile, 'r'))
            return numLines
        except:
            pass