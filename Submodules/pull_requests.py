""" 
Name: Matthew Nale
    Date of Last Edit: 2/12/2023
    
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
        try:
            pulls = repo.get_pulls(state=type, sort="updated", direction="asc")     #Get the issues and pull requests depending on the provided state
            return (datetime.now() - pulls[0].updated_at).days                      #Returns a datetime object, which details the most recent Pull Request
        except:
            return (datetime.now() - repo.created_at).days;                         #No pull request, so return the creation date of the repo
    except:
        print("Error in getMostRecentPull")                                         #Except case for potential invalid github links

#getAllPulls will obtain the number of pull requests of  the specific type
def getAllPulls(url, type):
    try:
        repo = gv.token.get_repo(url.split("github.com/", 1)[1])                    #Obtain the appropriate repo from REST API
        try:
            pulls = repo.get_pulls(state=type)                                      #Grabs the list of pull requests
            return pulls.totalCount
        except:
            return (datetime.now() - repo.created_at).days;                         #No pull request, so return the creation date of the repo
    except:
        print("Error in getAllPullDates")

#getCreationDate will return the datetime of when the repository was created
def getCreationDate(url):
    try:
        repo = gv.token.get_repo(url.split("github.com/", 1)[1])
        return (datetime.now() - repo.created_at).days                              #Returns days since creation
    except:
        print("Error in getCreationDate")