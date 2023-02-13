""" Name: Elijah Klein
    Date of Last Edit: 2/12/2023
    
    Purpose: Used for testing individual functions and function calls, without having to setup Rust-Python integration

    Details: Individual calls can be made below, such as for Licensing.py and repo_clone.py, in order to ensure compatability with all files
"""
import git
import sys
from datetime import datetime
import Submodules.global_var as gv
from Submodules.repo_clone import clone_repo
from Submodules.file_information import getDirectorySize
from Submodules.npm_handler import npm2git 
import Submodules.pull_requests as pulls
import Submodules.readme as readme
import Submodules.contributors as contrib

from NetScoreCalculation.MetricCalculation.Licensing import calculateLicenseScore
import Submodules.issues as issues



url = 'https://github.com/ElijahKlein/461-Test-Case-1'
url2 = 'https://github.com/ElijahKlein/461-Test-Case-2'
repo = clone_repo(url)                                                          #Clones the repository from the given URL, and a GitPython Repo object is stored in repo

failCount = 0
numContrib = contrib.getNumContributors(url).totalCount
sumCount = 0
for i in contrib.getStatsContributors(url):
	sumCount += i.total
numFiles = contrib.getNumFiles(url)

functions = [npm2git("https://www.npmjs.com/package/express"), getDirectorySize(url), issues.getIssuesByType(url, 'open'), issues.getIssuesByType(url, 'closed'), issues.getUsers(url), pulls.getMostRecentPull(url, 'closed'), pulls.getMostRecentPull(url, 'open'), pulls.getAllPulls(url, 'closed'), pulls.getAllPulls(url, 'open'), pulls.getAllPulls(url2, 'closed'), pulls.getAllPulls(url2, 'open'), pulls.getCreationDate(url), readme.checkLicensing(repo), readme.checkRMLength(repo), contrib.getNumContributors(url).totalCount, contrib.getNumFiles(url), sumCount, sumCount, contrib.calcContributorsPerFile(numContrib, numFiles)]
answers = ["https://github.com/expressjs/express", 19, 6, 4, 1, (datetime.now() - datetime(2023, 2, 12, 1, 42)).days, None, 2, 0, 0, 1, (datetime.now() - datetime(2023, 2, 12, 9, 14)).days, 1, 707, 2, 5, 9, 9, 0.4]
total = len(functions)
for i in range(0, total):
	try:
		assert(functions[i]) == answers[i]
	except AssertionError as msg:
		failCount += 1
		print(f"{i}\n")
total += 1
try:
	assert(repo) != (None)
except AssertionError as msg:
	failCount += 1



print(f'{total - failCount}/{total} test cases passed. Z% line coverage achieved.')
