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
                content = f.read()
                if('mit license' in content.lower() or 'lgplv2.1 license' in content.lower()):      #Check the README for mention of compatable licenses
                    return 1
                else:                                                                       #Attempt to look in the LICENSE file for information
                    try:
                        if open(os.path.join(targetFile, 'LICENSE')):
                            return 1                                                        
                    except:
                        pass                                                                #No LICENSE file and not in README
            f.close()
        except:
            pass
    return 0;

def checkRMLength(repo):
    for ext in [".md", ".markdown"]:
        try:
            targetFile = os.path.join(repo.working_tree_dir, 'README' + ext)                                          
            numLines = sum(1 for line in open(targetFile, 'r'))                             #Calculates number of lines in the readme with sum() function
            return numLines
        except:
            return 0                                                                        #No README detected
