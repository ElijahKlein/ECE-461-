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
import Submodules.global_var as gv
def getNumContributors(url):
    try:
        repo = gv.token.get_repo(url.split("github.com/", 1)[1]) 
        numContributors = repo.get_contributors(anon="true")
        return numContributors.totalCount
    except:
        print("Error retrieving the number of contributors")
        
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
                numFiles.append(files_content)
        return len(numFiles)
    except:
        print("Error retrieving the number of files")

def getStatsContributors(url):
    try:
        repo = gv.token.get_repo(url.split("github.com/", 1)[1]) 
        statsContributors = repo.get_stats_contributors()
        return statsContributors
    except:
        print("Error retrieving the stats of contributors")

def getStatsCommitActivity(url):
    try:
        repo = gv.token.get_repo(url.split("github.com/", 1)[1]) 
        statsCommitActivity = repo.get_stats_commit_activity()
        return statsCommitActivity
    except:
        print("Error retrieving the stats of commits")

def calcContributorsPerFile(numContributors, numFiles):
    try:
        contributorsPerFile = numContributors / numFiles
    except TypeError:
        print("Type Error: Check the variable type for inputs")
    return contributorsPerFile

