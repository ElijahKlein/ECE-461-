""" Name: Elijah Klein
    Date of Last Edit: 2/12/2023
    
    Purpose: Used for testing individual functions and function calls, without having to setup Rust-Python integration

    Details: Individual calls can be made below, such as for Licensing.py and repo_clone.py, in order to ensure compatability with all files
"""

import sys
import Submodules.global_var as gv
from NetScoreCalculation.MetricCalculation.Licensing import calculateLicenseScore
from Submodules.repo_clone import clone_repo
import Submodules.issues as issues
import Submodules.pull_requests as pulls
import pytest




url = 'https://github.com/ElijahKlein/461-Test-Case-1'
repo = clone_repo(url)                                                          #Clones the repository from the given URL, and a GitPython Repo object is stored in repo
license_score = calculateLicenseScore(repo)                                     #license_score is determined by the evaluate_readme function in Licensing.py
print(f'License scoring: {license_score}')

numIssues = issues.getIssuesByType(url, 'open')                                 #Example usage of the getIssuesByTypes function, which obtains the number of open issues
print(f'Number of open issues: {numIssues}')
numIssues = issues.getIssuesByType(url, 'closed')                                 #Example usage of the getIssuesByTypes function, which obtains the number of open issues
print(f'Number of closed issues: {numIssues}')
numDownloads = issues.getUsers(url)                                             #Example usage of the getUsers function, which obtains the number of downloads of the repo
print(numDownloads)

recentPull = pulls.getMostRecentPull(url, 'closed')                             #Example usage of the getMostRecentPull function, which obtaines the most recent closed pull request
print(f'The most recent pull request was: {recentPull} time ago')
#pullDates = pulls.getAllPullDates(url, 'closed')                               #Example usage of the getAllPullDates function, which obtains a list of all Pull Request dates
#print(pullDates)
