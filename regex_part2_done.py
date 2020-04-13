# -*- coding: utf-8 -*-
"""
If you have looked through the hackers.log file,
you may have noticed a few types of data in the rows.

One type of row is that which indicates when the log
was opened or when the date changes. We found these
rows last week.

Today we will search for rows where chat participants
post messages. 

@author: lee
"""

#%% imports


#%% define function
def find_message(row):
    return True

#%% define test

def test_find_message():
    assert find_message('a') == True
    assert find_message('b') == False
    
#%% call test function
test_find_message()

#%% load data
raw_log = ""
with open('data/hackers.log', 'r+', errors='ignore') as f:
    raw_log = f.readlines()
    
    
