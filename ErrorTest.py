""" Name: Elijah Klein
    Date of Last Edit: 2/12/2023
    Purpose: Generate a testing suite that covers the code base
"""
from datetime import datetime
from Submodules.repo_clone import clone_repo
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
numContrib = contrib.getNumContributors(url)
sumCount = 0
for i in contrib.getStatsContributors(url):
	sumCount += i.total
numFiles = contrib.getNumFiles(url)
#print(type(issues.getIssueData(url.split("github.com/", 1)[1])))

#functions = [npm2git("https://www.npmjs.com/package/express"), type(issues.getIssueData(url)), issues.getUsers(url), pulls.getMostRecentPull(url, 'closed'), pulls.getMostRecentPull(url, 'open'), pulls.getAllPulls(url, 'closed'), pulls.getAllPulls(url, 'open'), pulls.getAllPulls(url2, 'closed'), pulls.getAllPulls(url2, 'open'), pulls.getCreationDate(url), readme.checkLicensing(repo), readme.checkRMLength(repo), contrib.getNumContributors(url).totalCount, contrib.getNumFiles(url), sumCount, sumCount, contrib.calcContributorsPerFile(numContrib, numFiles)]
#answers = ["https://github.com/expressjs/express", '.json', 1, (datetime.now() - datetime(2023, 2, 12, 1, 42)).days, None, 2, 0, 0, 1, (datetime.now() - datetime(2023, 2, 12, 9, 14)).days, 1, 707, 2, 5, 9, 9, 0.4]

functions = [npm2git("https://www.npmjs.com/package/express"), issues.getUsers(url), pulls.getMostRecentPull(url, 'closed'), pulls.getMostRecentPull(url, 'open'), pulls.getAllPulls(url, 'closed'), pulls.getAllPulls(url, 'open'), pulls.getAllPulls(url2, 'closed'), pulls.getAllPulls(url2, 'open'), pulls.getCreationDate(url), readme.checkLicensing(repo), readme.checkRMLength(repo), contrib.getNumContributors(url), contrib.getNumFiles(url), sumCount, sumCount]
answers = ["https://github.com/expressjs/express", 1, (datetime.now() - datetime(2023, 2, 12, 1, 42)).days, None, 2, 0, 0, 1, (datetime.now() - datetime(2023, 2, 12, 9, 14)).days, 1, 707, 2, 5, 9, 9]
print(f'len: {len(functions)}')
print(f'len: {len(answers)}')
total = len(functions)
for i in range(0, total):
	try:
		assert(functions[i]) == answers[i]
	except AssertionError as msg:
		failCount += 1
		print(total)
total += 1
try:
	assert(repo) != (None)
except AssertionError as msg:
	failCount += 1
print(f'{total - failCount}/{total} test cases passed. 83% line coverage achieved.') #83% coverage taken from using coverage.py and pytest in conjunction to generate a full coverage report shown in documentation