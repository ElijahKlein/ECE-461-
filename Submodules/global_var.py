""" 
Name: Eric Chen 
    Date of Last Edit: 2/8/2023
    
    Purpose: Holds all global variables and functions

    Details: Current vars are Github token and cloned repo location

"""

from github import Github                                                       #Using PyGitHub for interaction with REST API
import os.path as path

token = Github('PUT TOKEN HERE')                                                #! MY ACCESS TOKEN, DO NOT SHARE. PUT YOUR OWN TOKEN HERE FOR NOW
file_loc = path.dirname(__file__) + '/../clone_dir/temp'

#set_file_loc will be used to keep a global variable of the working file directory for cloning
def set_file_loc(url):
    global file_loc
    file_loc = path.dirname(__file__) + '/../clone_dir/' + path.basename(url)
