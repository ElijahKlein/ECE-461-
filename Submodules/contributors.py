# -*- coding: utf-8 -*-
"""
Name: Jack Kwan
Date: 2/12/2023
File: contributors.py
Description: Defines functionality to return contributor and file information about an inputted Github Repo 
Input: url = The url for the Github repo
"""

#import Submodules.global_var as gv
from github import Github
import Submodules.globar_var as gv

#Retrieves the number of contributors for a given repo
def getNumContributors(url):
    try:
        repo = gv.token.get_repo(url.split("github.com/", 1)[1]) 
        numContributors = repo.get_contributors(anon="true")
        return numContributors
    except:
        print("Error retrieving the number of contributors")
#Retrieves the number of files in a given repo        
def getNumFiles(url):
    try:
        repo = gv.token.get_repo(url.split("github.com/", 1)[1]) 
        contents = repo.get_contents("")
        numFiles = []
        while contents:
            files_content = contents.pop(0)
            if(files_content.type == "dir"):
                contents.extend(repo.get_contents(files_content.path))
            else:
                if(files_content.name != ".gitignore" or files_content.name != "readme.md"):                 #Within this if statement, add any names of files you wish to ignore when collecting the number of files
                    numFiles.append(files_content)
        return len(numFiles)
    except:
        print("Error retrieving the number of files")

#Retrieves the commits activity over the last year for a given repo
def getStatsCommitActivity(url):
    try:
        repo = gv.token.get_repo(url.split("github.com/", 1)[1]) 
        statsCommitActivity = repo.get_stats_commit_activity()
        return statsCommitActivity
    except:
        print("Error retrieving the stats of commits")

#Calculation function used to determine the commits per contributor per file for a given repo
def calcCommitsPerContributorsPerFile(numCommits, numContributors, numFiles):
    try:
        commitsPerContributorsPerFile = (numCommits / numContributors) / numFiles
        return commitsPerContributorsPerFile
    except TypeError:
        print("Type Error: Check the variable type for inputs")

#Unused functionality: Retrives commit counts from each individual contributor. 
'''
def getStatsContributors(url):
    try:
        repo = gv.token.get_repo(url.split("github.com/", 1)[1]) 
        statsContributors = repo.get_stats_contributors()
        return statsContributors
    except:
        print("Error retrieving the stats of contributors")
'''
