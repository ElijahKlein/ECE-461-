""" Name: Matthew Nale
    Date of Last Edit: 2/5/2023
    
    Purpose: Calculate Licensing Sub Metric of a given GitHub Repository

    Details: Scans the README file of the given repository and returns a binary value for if the Repository has compatible licensing with the ACME Corporation. If not in README, will also
    check for existance of a LICENSE file for compatable licensing
    
"""
#Using GitPython for 'import git'
import git
import os
from Submodules.readme import checkLicensing

def calculateLicenseScore(repo):
    return checkLicensing(repo)                                        #Uses the readme.py functions to check for licensing, then returns either 1 or 0 depending on compatibility