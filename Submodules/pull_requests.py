""" 
Name: Matthew Nale
    Date of Last Edit: 2/8/2023
    
    Purpose: Performs all operations related to pull requests, which can be called from any other function

    Details: Lists and controls all operations for analyzing pull requests, such as the most number of pull requests, along with dates

"""

import os
import sys
from Submodules.token_file import *
from datetime import datetime                                                       #Used for time calculations

#getMostRecentPull will return the date of the most recent pull request of the provided URL, sorted by type (closed, open, all)
def getMostRecentPull(url, type):
    try:
        repo = token.get_repo(url.split("github.com/", 1)[1])
        issuesAndPull = repo.get_issues(state=type)                                 #Get the issues and pull requests depending on the provided state
        index = 0
        mostRecent = issuesAndPull[index]
        while not mostRecent.pull_request and index < issuesAndPull.totalCount:     #Iterates through all Issues and Pull Request to find the most recent Pull Request of the specified type
            index += 1
        return datetime.now() - mostRecent.closed_at                                #Returns a datetime object, which details the most recent Pull Request
    except:
        print("Error in getMostRecentPull")                                         #Except case for potential invalid github links

#getAllPullDates will return a list of datetimes of all Pull Requests of the provided type
def getAllPullDates(url, type):
    try:
        repo = token.get_repo(url.split("github.com/", 1)[1])
        issuesAndPull = repo.get_issues(state=type)
        datesList = []
        for pulls in issuesAndPull:
            if(pulls.pull_request):
                datesList.append(pulls.closed_at)
        return datesList
    except:
        print("Error in getAllPullDates")
        
"""This below can be used for testing. Comment when not being used, or delete when finishing project
url = sys.argv[1]
date = getMostRecentPull(url, 'closed')
print(datetime.now() - date)

datesList = getAllPullDates(url, 'closed')
print(datesList)
"""

