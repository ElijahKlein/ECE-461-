""" Name: Matthew Nale
    Date of Last Edit: 2/5/2023
    
    Purpose: Used for testing individual functions and function calls, without having to setup Rust-Python integration

    Details: Individual calls can be made below, such as for Licensing.py and repo_clone.py, in order to ensure compatability with all files
"""

import sys
from NetScoreCalculation.MetricCalculation.Licensing import evaluate_readme
from Submodules.repo_clone import clone_repo

url = sys.argv[1]
repo = clone_repo(url)
scoring = evaluate_readme(repo)
print(scoring)

