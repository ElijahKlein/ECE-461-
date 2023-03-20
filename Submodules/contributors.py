# -*- coding: utf-8 -*-
"""
Name: Jack Kwan
Date: 2/12/2023
File: contributors.py
Description: Defines functionality to return contributor and file information about an inputted Github Repo 
Input: url = The url for the Github repo
"""

import Submodules.globar_var as gv
#Retrieves the number of contributors for a given repo
def getNumContributors(url):
    try:
        repo = gv.token.get_repo(url.split("github.com/", 1)[1])    #Obtain the repo from rest API
        numContributors = repo.get_contributors(anon="true")        #Get the list of contributors using PyGithub
        return numContributors.totalCount                           #Return the total count of contributors
    except:
        print("Error retrieving the number of contributors")        #Error trap
        
#Retrieves the number of files in a given repo          
def getNumFiles(url, token):
    try:
        repo = gv.token.get_repo(url.split("github.com/", 1)[1])    #Obtain the repo from rest API 
        contents = repo.get_contents("")                            #Get all files contained in the repo
        numFiles = []                                               #List that will contain all file objects
        #Parse through all file objects created by PyGithub
        while contents:                             
            files_content = contents.pop(0)                         #Pop out the top file
            if(files_content.type == "dir"):                            #If the file is a directory, recursively get the subdirectory file objects
                contents.extend(repo.get_contents(files_content.path))
            else:
                numFiles.append(files_content)                      #Add the specific file object to the list
        return len(numFiles)                                        #Return the length of the list
    except:
        print("Error retrieving the number of files")               #Error trap
#Retrives commit counts from each individual contributor. 
def getStatsContributors(url):
    try:
        repo = gv.token.get_repo(url.split("github.com/", 1)[1]) 
        statsContributors = repo.get_stats_contributors()
        return statsContributors
    except:
        print("Error retrieving the stats of contributors")

#Unused functionality: 
#Retrieves the commits activity over the last year for a given repo
'''
def getStatsCommitActivity(url):
    try:
        repo = gv.token.get_repo(url.split("github.com/", 1)[1])    #Obtain the repo from rest API 
        statsCommitActivity = repo.get_stats_commit_activity()      #Get the repo's commit activity from the last year
        return statsCommitActivity                                  #Return this activity
    except:
        print("Error retrieving the stats of commits")
'''

