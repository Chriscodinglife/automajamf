#!/usr/bin/env python3

'''

 ________  _________  ________  _____ ______   ________        ___  ________  _____ ______   ________ 
|\   __  \|\___   ___\\   __  \|\   _ \  _   \|\   __  \      |\  \|\   __  \|\   _ \  _   \|\  _____\
\ \  \|\  \|___ \  \_\ \  \|\  \ \  \\\__\ \  \ \  \|\  \     \ \  \ \  \|\  \ \  \\\__\ \  \ \  \__/ 
 \ \   __  \   \ \  \ \ \  \\\  \ \  \\|__| \  \ \   __  \  __ \ \  \ \   __  \ \  \\|__| \  \ \   __\
  \ \  \ \  \   \ \  \ \ \  \\\  \ \  \    \ \  \ \  \ \  \|\  \\_\  \ \  \ \  \ \  \    \ \  \ \  \_|
   \ \__\ \__\   \ \__\ \ \_______\ \__\    \ \__\ \__\ \__\ \________\ \__\ \__\ \__\    \ \__\ \__\ 
    \|__|\|__|    \|__|  \|_______|\|__|     \|__|\|__|\|__|\|________|\|__|\|__|\|__|     \|__|\|__| 
                                                                                                      
                                                                                                      
                                                                                                      
This script is used to automate the process of testing and deploying a policy on a Jamf Pro server to a local machine or a VM.

'''

## IMPORT
import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()


## VARIABLES
jss_user = os.getenv('JSS_USER')
jss_pass = os.getenv('JSS_PASS')


## FUNCTIONS
def check_parallel_exists():
    
    '''Check if a file exists.'''
    if os.path.isfile('/usr/local/bin/prlctl'):
        return True
    
    return False


def check_jamf_install():
    
    '''Check if the jamf binary is installed locally.'''
    if os.path.isfile('/usr/local/bin/jamf'):
        return True
    
    return False


def check_policy_exists():
    
    '''Check if the policy exists.'''
    pass