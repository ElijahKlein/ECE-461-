""" 
Name: Eric Chen
    Date of Last Edit: 2/8/2023
    
    Purpose: Established connection with GitHub REST API

    Details: Using a private access token, establishes a connection with the REST API in order to obtain relevant information

"""

from github import Github                                       #Using PyGitHub for interaction with REST API
token = Github('PRIVATE ACCESS TOKEN')                          #! MY ACCESS TOKEN, DO NOT SHARE. PUT YOUR OWN TOKEN HERE FOR NOW
