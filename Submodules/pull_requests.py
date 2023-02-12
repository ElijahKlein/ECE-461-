""" 
Name: Matthew Nale
    Date of Last Edit: 2/8/2023
    
    Purpose: Performs all operations related to pull requests, which can be called from any other function

    Details: Lists and controls all operations for analyzing pull requests, such as the most number of pull requests, along with dates

"""

import os
import sys
import Submodules.global_var as gv
from datetime import datetime                                                       #Used for time calculations

#getMostRecentPull will return the days since the most recent pull request of the provided URL, sorted by type (closed, open, all)
def getMostRecentPull(url, type):
    try:
        repo = gv.token.get_repo(url.split("github.com/", 1)[1])                    #Obtain the appropriate repo from REST API
        issuesAndPull = repo.get_issues(state=type)                                 #Get the issues and pull requests depending on the provided state
        index = 0
        mostRecent = issuesAndPull[index]
        while not mostRecent.pull_request and index < issuesAndPull.totalCount:     #Iterates through all Issues and Pull Request to find the most recent Pull Request of the specified type
            index += 1
        return (datetime.now() - mostRecent.closed_at).days                         #Returns a datetime object, which details the most recent Pull Request
    except:
        print("Error in getMostRecentPull")                                         #Except case for potential invalid github links

#getAllPulls will obtain the number of pull requests of  the specific type
def getAllPulls(url, type):
    try:
        repo = gv.token.get_repo(url.split("github.com/", 1)[1])                    #Obtain the appropriate repo from REST API
        pulls = repo.get_pulls(state=type)                                          #Grabs the list of pull requests
        return pulls.totalCount
    except:
        print("Error in getAllPullDates")

#getCreationDate will return the datetime of when the repository was created
def getCreationDate(url):
    try:
        repo = gv.token.get_repo(url.split("github.com/", 1)[1])
        return (datetime.now() - repo.created_at).days
    except:
        print("Error in getCreationDate")
        
"""This below can be used for testing. Comment when not being used, or delete when finishing project
url = sys.argv[1]
date = getMostRecentPull(url, 'closed')
print(datetime.now() - date)

datesList = getAllPullDates(url, 'closed')
print(datesList)
"""

