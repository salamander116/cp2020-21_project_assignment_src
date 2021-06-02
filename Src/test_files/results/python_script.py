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

def parse(filename, endResult, layer_size):
    results = open(filename, "r")
    
    info = [line.rstrip() for line in results]
    
    thread_num = '1'
    time = ''
    os.system("echo Parsing file {}" )
    
    for line in info:
        if line.startswith('Size',0):
            layer_size = line.split(':')[1].replace("\n", "").replace(" ", "")
            
        elif line.startswith('Threads',0):
            thread_num = line.split(':')[1].replace("\n", "").replace(" ", "")
        
        elif line.startswith('Time',0):
            time = line.split(':')[1].replace("\n", "").replace(" ", "")
        
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
    numThreads = []
    time = []
    file = open(filename)
    next(file)
    for line in file:
        lineArray = line.split(",")
        lineArray[2] = lineArray[2].replace(" \n","")#removes the \n
        numThreads.append(lineArray[1])
        time.append(lineArray[2])
        
    speedUp = []
    efficiency = []
    for x in range(len(time) - 1):
        su = float(time[0])/float(time[x+1])
        speedUp.append(su)  
        ef = su/float(numThreads[x+1])
        efficiency.append(ef)

    print(speedUp)
    print(efficiency)
    plt.plot(numThreads[1:], speedUp)
    plt.title("Speedup " + filename)
    plt.show()
    plt.plot(numThreads[1:], efficiency)
    plt.title("Efficiency " + filename)
    plt.show()

def get_layerSizes(filename, layer_size):
    file = open(filename)
    for line in file:
        value = line.split(" ")
        layer_size.append(value[0])
    del layer_size[-1]
    

    

layer_size = []
file_names = ["1.txt", "2.txt", "03.txt", "04.txt", "05.txt", "06.txt", "7.txt", "8.txt"]
file_results = ["organized1.txt", "organized2.txt", "organized03.txt", "organized04.txt", "organized05.txt", "organized06.txt", "organized7.txt", "organized8.txt"]
get_layerSizes("index.txt", layer_size)
print(layer_size)
for x in range (len(layer_size)):
    endResult ={}
    parse(file_names[x], endResult,layer_size[x])
    get_final(file_results[x], endResult)
    get_results(file_results[x])


    