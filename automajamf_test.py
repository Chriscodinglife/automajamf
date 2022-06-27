#!/usr/bin/env python3

'''

 ________  _________  ________  _____ ______   ________        ___  ________  _____ ______   ________ 
|\   __  \|\___   ___\\   __  \|\   _ \  _   \|\   __  \      |\  \|\   __  \|\   _ \  _   \|\  _____\
\ \  \|\  \|___ \  \_\ \  \|\  \ \  \\\__\ \  \ \  \|\  \     \ \  \ \  \|\  \ \  \\\__\ \  \ \  \__/ 
 \ \   __  \   \ \  \ \ \  \\\  \ \  \\|__| \  \ \   __  \  __ \ \  \ \   __  \ \  \\|__| \  \ \   __\
  \ \  \ \  \   \ \  \ \ \  \\\  \ \  \    \ \  \ \  \ \  \|\  \\_\  \ \  \ \  \ \  \    \ \  \ \  \_|
   \ \__\ \__\   \ \__\ \ \_______\ \__\    \ \__\ \__\ \__\ \________\ \__\ \__\ \__\    \ \__\ \__\ 
    \|__|\|__|    \|__|  \|_______|\|__|     \|__|\|__|\|__|\|________|\|__|\|__|\|__|     \|__|\|__| 
                                                                                                      
                                                                                                      
This script is for unit testing the automajamf.py script.

'''

## IMPORT

import unittest
import automajamf

class test_automajamf(unittest.TestCase):
    
    '''Run several tests to ensure quality of automajamf'''
    def test_check_parallel_exists(self):
        actual = automajamf.check_parallel_exists()
        self.assertTrue(actual)
        