""" 
Name: Matthew Nale
    Date of Last Edit: 2/12/2023
    
    Purpose: Performs all operations related to issues, which can be called from any other function

    Details: Lists and controls all operations for analyzing issues, such as the amount of open/closed issues and total issues

"""

import os
import requests
import Submodules.global_var as gv

#getIssueData uses GraphQL to obtain all issues of the repository
def getIssueData(url):
    header = {"Authorization": f"Bearer {os.getenv('GITHUB_TOKEN')}"}    #Header for request
    names = url.split('/')                                               #Split to seperate name
    #Request sent to GraphQL API 
    request = requests.post('https://api.github.com/graphql', json={'query':f'{{repository(owner: "{names[0]}", name: "{names[1]}") {{issues {{totalCount}}open: issues(states:OPEN) {{totalCount}}closed: issues(states:CLOSED) {{totalCount}}}}}}'}, headers=header)
    if(request.status_code == 200):                                      #Return JSON response if completed
        return request.json()
    else:                                                                #Raise exception otherwise
        raise Exception("Query failes to run by returning code of {}.".format(request.status_code))
    
#getUsers will obtain and return the amount of stars of a repository, hinting at number of users of a repo
def getUsers(url):
    try:
        repo = gv.token.get_repo(url.split("github.com/", 1)[1])    #Obtains the repo from REST API
        return repo.stargazers_count                                #Returns the amount of stars of the project, which gives an estimate at the number of users
        
    except:
        print("Error in getUsers")                                  #Except case for potential invalid GitHub links