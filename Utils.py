# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 21:56:45 2020

@author: ARJUN
"""
def log(data):
    f = open("log", "a")
    f.write(f"{data}\n")
    f.close()