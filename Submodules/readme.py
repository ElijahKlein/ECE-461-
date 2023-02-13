""" 
Name: Matthew Nale
    Date of Last Edit: 2/12/2023
    
    Purpose: Performs all README operations, which can be called from any other function

    Details: Lists and controls all README operations, such as checking for licensing

"""

import git                                                                                  #Using GitPython for 'import git'
import os

def checkLicensing(repo):
    for ext in [".md", ".markdown"]:                                                        #Checking for multiple file extensions
        try:                                                                    
            targetFile = repo.working_tree_dir
            with open(os.path.join(targetFile, 'README' + ext), 'r') as f:
                if(f.read().find('MIT License') or f.read().find('LGPLv2.1 License')):      #Check the README for mention of compatable licenses
                    return 1
                else:                                                                       #Attempt to look in the LICENSE file for information
                    try:
                        with open(os.path.join(targetFile, 'LICENSE')) as f:
                            if(f.read().find('MIT License') or f.read().find('LGPLv2.1 License')):
                                return 1
                            else:
                                return 0                                                    #If license information not in README/LICENSE, return value 0
                    except:
                        pass                                                                #No LICENSE file and not in README
            f.close()
        except:                  #If the clone_from fails, the scoring automatically is a 0, as there is not README to check for compatability
            pass
    print("Error in checkLicensing")
    return -1;

def checkRMLength(repo):
    for ext in [".md", ".markdown"]:
        try:
            targetFile = os.path.join(repo.working_tree_dir, 'README' + ext)                                          
            numLines = sum(1 for line in open(targetFile, 'r'))                             #Calculates number of lines in the readme with sum() function
            return numLines
        except:
            return 0                                                                        #No README detected