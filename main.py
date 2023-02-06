""" Name: Matthew Nale
    Date of Last Edit: 2/5/2023
    
    Purpose: Used for testing individual functions and function calls, without having to setup Rust-Python integration

    Details: Individual calls can be made below, such as for Licensing.py and repo_clone.py, in order to ensure compatability with all files
"""

import sys
from NetScoreCalculation.MetricCalculation.Licensing import calculateLicenseScore
from Submodules.repo_clone import clone_repo

url = sys.argv[1]                                                               #Obtains the URL link from argv[1]. Will later be modified to take a .txt file instead
repo = clone_repo(url)                                                          #Clones the repository from the given URL, and a GitPython Repo object is stored in repo
license_score = calculateLicenseScore(repo)                                     #license_score is determined by the evaluate_readme function in Licensing.py
print(license_score)

