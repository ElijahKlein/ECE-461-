""" Name: Elijah Klein
    Date of Last Edit: 2/12/2023
    
    Purpose: Used for testing individual functions and function calls, without having to setup Rust-Python integration

    Details: Individual calls can be made below, such as for Licensing.py and repo_clone.py, in order to ensure compatability with all files
"""

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
repo = clone_repo(url)                                                          #Clones the repository from the given URL, and a GitPython Repo object is stored in repo

total = 0
failCount = 0

repo = clone_repo(url)


total += 1	
try:
	assert(repo) != None
except AssertionError as msg:
	failCount += 1
	print(total)

total += 1	
try:
	assert(npm2git("https://www.npmjs.com/package/express")) == "https://github.com/expressjs/express"
except AssertionError as msg:
	failCount += 1
	print(total)

total += 1	
try:
	assert(getDirectorySize(url)) == 19 #TODO - Verify
except AssertionError as msg:
	failCount += 1
	print(total)

total += 1	
try:
	assert(issues.getIssuesByType(url, 'open')) == 6
except AssertionError as msg:
	failCount += 1
	print(total)

total += 1	
try:
	assert(issues.getIssuesByType(url, 'closed')) == 4
except AssertionError as msg:
	failCount += 1
	print(total)

total += 1	
try:
	assert(issues.getUsers(url)) == 1
except AssertionError as msg:
	failCount += 1
	print(total)

total += 1	
try:
	assert(pulls.getMostRecentPull(url, 'closed')) == (datetime.now() - datetime(2023, 2, 11, 20, 42)).days
except AssertionError as msg:
	failCount += 1
	print(total)

total += 1	
try:
	assert(pulls.getMostRecentPull(url, 'open')) == None #TODO - verify
except AssertionError as msg:
	failCount += 1
	print(total)

total += 1	
try:
	assert(pulls.getAllPulls(url, 'closed')) == 2
except AssertionError as msg:
	failCount += 1
	print(total)

total += 1	
try:
	assert(pulls.getAllPulls(url, 'open')) == 0
except AssertionError as msg:
	failCount += 1
	print(total)
total += 1	
try:
	assert(pulls.getCreationDate(url)) == (datetime.now() - datetime(2023, 2, 11, 19, 4)).days
except AssertionError as msg:
	failCount += 1
	print(total)
total += 1	
try:
	assert(readme.checkLicensing(repo)) == 1 #TODO - verify
except AssertionError as msg:
	failCount += 1
	print(total)
total += 1	
try:
	assert(readme.checkRMLength(repo)) == 707
except AssertionError as msg:
	failCount += 1
	print(total)





total += 1	
numContrib = contrib.getNumContributors(url).totalCount
try:
	#print(f'NumContrib: {contrib.getNumContributors(url)}')
	assert(contrib.getNumContributors(url).totalCount) == 2
except AssertionError as msg:
	failCount += 1
	print("fail 1")
total += 1	
numFiles = contrib.getNumFiles(url)
try:
	assert(contrib.getNumFiles(url)) == 5 #TODO - verify
except AssertionError as msg:
	failCount += 1
	print("fail 2")
	
	
#TODO - This Fails
total += 1	
try:
	#print(f'ContribStats: {contrib.getStatsContributors(url)}')
	assert(contrib.getStatsContributors(url)) == 5 #TODO - verify
except AssertionError as msg:
	failCount += 1
	print("fail 3")
	
#TODO - This Fails
total += 1	
try:
	#print(f'commitactivity: {contrib.getStatsCommitActivity(url)}')
	assert(contrib.getStatsCommitActivity(url)) == 5 #TODO - verify
except AssertionError as msg:
	failCount += 1
	print("fail 4")
total += 1	
try:
	assert(contrib.calcContributorsPerFile(numContrib, numFiles)) == 0.4 #TODO - verify
except AssertionError as msg:
	failCount += 1
	print("fail 5")





print(f'{total - failCount}/{total} test cases passed. Z% line coverage achieved.')





