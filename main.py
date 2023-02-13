""" Name: Matthew Nale, Eric Chen 
    Date of Last Edit: 2/12/2023
    
    Purpose: Used for testing individual functions and function calls, without having to setup Rust-Python integration

    Details: Individual calls can be made below, such as for Licensing.py and repo_clone.py, in order to ensure compatability with all files
"""

import sys
import subprocess                                                               #Used for calling executables (Compiled Rust files) with arguements
import os
import json

from NetScoreCalculation.MetricCalculation.licensing import calculateLicenseScore
from Submodules.repo_clone import clone_repo
import Submodules.readme as rm
import Submodules.issues as issues
import Submodules.pull_requests as pulls
from Submodules.npm_handler import npm2git
import Submodules.contributors as contributors

file = sys.argv[1]
netScores = {}
with open(os.path.normpath(file), 'r') as f:
    for url_in in f:
        url_in = url_in.rstrip()
        
        #Convert npm link to GitHub if needed
        if "npmjs.com/" in url_in: 
            url = npm2git(url_in)  
        else: 
            url = url_in

        #Clones the repository locally from the provided URL, and returns a Repo object of the URL                                            
        repo = clone_repo(url)

        #Calculates the Licensing score, by using the repo object obtained
        license_score = calculateLicenseScore(repo)

        #Obtain information from the readme.py function
        readmeLength = rm.checkRMLength(repo)

        #Obtain information from the contributors.py function
        repoSize = contributors.getNumFiles(url)
        numContributors = contributors.getNumContributors(url)
        numCommits = 0
        allCommits = contributors.getStatsContributors(url)
        for contributor in allCommits:
            numCommits += contributor.total

        #Obtain information from the issues.py function
        issueData = issues.getIssueData(url.split("github.com/", 1)[1])
        numIssues = issueData['data']['repository']['open']['totalCount']
        numDownloads = issues.getUsers(url)

        #Obtain information from the pull_requests.py function
        recentPull = pulls.getMostRecentPull(url, 'all')                         
        pullTotal = pulls.getAllPulls(url, 'all')
        creationDate = pulls.getCreationDate(url)

        #Calculates the pull request frequency since the creation of the repo
        pullFrequency = creationDate / pullTotal

        #Sets the rust executable path
        executable = os.path.dirname(__file__) + "/NetScoreCalculation/net_score.exe "

        #Arguements for NetScore file using gathered data
        args = f"{license_score} {numIssues} {numDownloads} {readmeLength} {recentPull} {pullFrequency} {repoSize} {numContributors} {numCommits}"

        #Runs the net_score.rs file to obtain information about the scoring. Catches the output on dataString
        dataString = subprocess.run(executable + args, cwd=None, shell=False, stdout=subprocess.PIPE)
        
        #Splits the output string by delimiters
        dataString = (dataString.stdout.decode('utf-8')).split(" ")
        
        #Converts ouput string into list of floats
        netScores[url_in] = list(map(float, dataString))

#Sort the directory by net score values
netScores = dict(sorted(netScores.items(), key=lambda x: x[1][0], reverse=True))

#Prints the net score in JSON format
formatString = ''
for key in netScores:
    formatString += f"{{\"URL\":\"{key}\", \"NET_SCORE\":{netScores[key][0]}, \"RAMP_UP_SCORE\":{netScores[key][2]}, \"CORRECTNESS_SCORE\":{netScores[key][1]}, \"BUS_FACTOR_SCORE\":{netScores[key][4]}, \"RESPONSIVENESS_SCORE\":{netScores[key][3]}, \"LICENSE_SCORE\":{netScores[key][5]}}} \n"
print(formatString)