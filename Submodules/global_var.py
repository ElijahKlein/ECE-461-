""" 
Name: Eric Chen 
    Date of Last Edit: 2/8/2023
    
    Purpose: Holds all globl variables and funct5ions

    Details: 

"""

from github import Github                                                       #Using PyGitHub for interaction with REST API
import os.path as path
import os

token = Github(os.getenv('GITHUB_TOKEN'))                                                #! MY ACCESS TOKEN, DO NOT SHARE. PUT YOUR OWN TOKEN HERE FOR NOW
file_loc = path.dirname(__file__) + '/../clone_dir/temp'

#set_file_loc will be used to keep a global variable of the working file directory for cloning
def set_file_loc(url):
    global file_loc
    file_loc = path.dirname(__file__) + '/../clone_dir/' + path.basename(url)
