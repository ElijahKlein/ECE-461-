""" 
Name: Eric Chen 
    Date of Last Edit: 2/8/2023
    
    Purpose: Holds all global variables and functions

    Details: Current vars are Github token and cloned repo location

"""

from github import Github                                                       #Using PyGitHub for interaction with REST API
import os.path as path
import os

token = Github(os.getenv('GITHUB_TOKEN'))                                       #Access token for REST API
file_loc = path.dirname(__file__) + '/../clone_dir/temp'

#set_file_loc will be used to keep a global variable of the working file directory for cloning
def set_file_loc(url):
    global file_loc
    file_loc = path.dirname(__file__) + '/../clone_dir/' + path.basename(url)