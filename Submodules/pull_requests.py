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

#getMostRecentPull will return the date of the most recent pull request of the provided URL, sorted by type (closed, open, all)
def getMostRecentPull(url, type):
    try:
        repo = gv.token.get_repo(url.split("github.com/", 1)[1])                    #Obtain the appropriate repo from REST API
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
        repo = gv.token.get_repo(url.split("github.com/", 1)[1])                    #Obtain the appropriate repo from REST API
        issuesAndPull = repo.get_issues(state=type)                                 #Grabs the issues depending on provided type
        datesList = []
        for pulls in issuesAndPull:                                                 
            if(pulls.pull_request):                                                 #If there is a pull request, add the closed date to the datesList
                datesList.append(pulls.closed_at)
    except:
        print("Error in getAllPullDates")
    return datesList
        
"""This below can be used for testing. Comment when not being used, or delete when finishing project
url = sys.argv[1]
date = getMostRecentPull(url, 'closed')
print(datetime.now() - date)

datesList = getAllPullDates(url, 'closed')
print(datesList)
"""

