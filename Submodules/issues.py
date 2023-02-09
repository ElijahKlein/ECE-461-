""" 
Name: Matthew Nale
    Date of Last Edit: 2/8/2023
    
    Purpose: Performs all operations related to issues, which can be called from any other function

    Details: Lists and controls all operations for analyzing issues, such as the amount of open/closed issues and total issues

"""

import os
import sys
import Submodules.global_var as gv

#getIssuesByType can be slow depending on the amount of issues. Look into another way of doing this. Type can be either 'closed', 'open', or 'all'
def getIssuesByType(url, type):
    count = 0                                                       #Count used to count the type of issues being found
    try:
        repo = gv.token.get_repo(url.split("github.com/", 1)[1])    #Obtains the name identifier from the provided url, and obtains that repo from the REST API
        issuesAndPull = repo.get_issues(state=type)                 #Get the issues and pull requests depending on the provided state
        for issue in issuesAndPull:
            if not issue.pull_request:                              #Sort out the Pull Requests from the issues. For some reason PyGitHub combines the two
                count = count + 1
    except:
        print("Error in getIssuesByType")                           #Except case for potential invalid GitHub links
        count = -1
    return count
 
#getUsers will obtain and return the amount of stars of a repository, hinting at number of users of a repo
def getUsers(url):
    try:
        repo = gv.token.get_repo(url.split("github.com/", 1)[1])    #Obtains the repo from REST API
        return repo.stargazers_count                                #Returns the amount of stars of the project, which gives an estimate at the number of users
        
    except:
        print("Error in getUsers")                                  #Except case for potential invalid GitHub links



"""This below can be used for testing. Comment when not being used, or delete when finishing project
url = sys.argv[1]
count = getIssuesByType(url, 'closed')
print(count)
"""