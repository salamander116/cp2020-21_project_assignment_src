# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import csv

def parse(filename, endResult):
    results = open(filename, "r")
    info = results.readlines
    
    thread_num = ''
    layer_size = ''
    time = ''
    
    os.system("echo Parsing file {}" )
    for line in info:
        
        if line.startswith('Size',0):
            layer_size = line.split(':')[1].replace("\n", "")
            
        elif line.startswith('Threads',0):
            thread_num = line.split(':')[1].replace("\n", "")
        
        elif line.startswith('Time',0):
            time = line.split(':')[1].replace("\n", "")
        
            if layer_size not in endResult.keys():
                endResult[layer_size] = {}
        
            if thread_num not in endResult[layer_size].keys():
                endResult[layer_size][thread_num] = {}
        
        endResult[layer_size][thread_num] = time
        
def get_final(new_file, results):
    if (os.path.isfile(new_file) == False):
        os.system("echo No such file, creating new file.")
        file = open(new_file, "w")
    else:
        os.system("echo File found.")
        file = open(new_file, 'w')
        file.truncate()            
    
    first_line = "Size:Threads:Time\n"
    file.write(first_line)
    
    for size in results.keys():
        for threads in results[size].keys():
            file.write(size + "," + threads + "," + results[size][threads]+ " " )
            file.write("\n")


def get_results(filename):
    file = open(filename)
    resultRead = csv.DictReader(file)
    
def plot(filename):
    
    