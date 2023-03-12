# -*- coding: utf-8 -*-
"""
Name: Jack Kwan
Date: 2/12/2023
File: contributors.py
Description: Defines functionality to return contributor and file information about an inputted Github Repo 
Input: url = The url for the Github repo
"""

<<<<<<< HEAD
import Submodules.globar_var as gv
#Retrieves the number of contributors for a given repo
=======
import Submodules.global_var as gv

#getNumContributors retrieves the number of contributors for a given repo
>>>>>>> fbe5fda0fc06c593210631a37854a592c164ee64
def getNumContributors(url):
    try:
        repo = gv.token.get_repo(url.split("github.com/", 1)[1])    #Obtain the repo from rest API
        numContributors = repo.get_contributors(anon="true")        #Get the list of contributors using PyGithub
        return numContributors.totalCount                           #Return the total count of contributors
    except:
        print("Error retrieving the number of contributors")        #Error trap
        
<<<<<<< HEAD
#Retrieves the number of files in a given repo          
def getNumFiles(url, token):
=======
#getNumFikes retrieves the number of files in a given repo          
def getNumFiles(url):
>>>>>>> fbe5fda0fc06c593210631a37854a592c164ee64
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
<<<<<<< HEAD
#Retrives commit counts from each individual contributor. 
=======
        
#getStatsContributors retrives commit counts from each individual contributor. 
>>>>>>> fbe5fda0fc06c593210631a37854a592c164ee64
def getStatsContributors(url):
    try:
        repo = gv.token.get_repo(url.split("github.com/", 1)[1]) 
        statsContributors = repo.get_stats_contributors()
        return statsContributors
    except:
<<<<<<< HEAD
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

=======
        print("Error retrieving the stats of contributors")
>>>>>>> fbe5fda0fc06c593210631a37854a592c164ee64
