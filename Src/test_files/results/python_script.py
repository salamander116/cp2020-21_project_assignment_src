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


def get_results(filename1, filename2):
    numThreads = []
    timeLocal = []
    file = open(filename1)
    next(file)
    for line in file:
        lineArray = line.split(",")
        lineArray[2] = lineArray[2].replace(" \n","")#removes the \n
        numThreads.append(lineArray[1])
        timeLocal.append(lineArray[2])
        
    speedUpLocal = []
    efficiencyLocal = []
    for x in range(len(timeLocal) - 1):
        su = float(timeLocal[0])/float(timeLocal[x+1])
        speedUpLocal.append(su)  
        ef = su/float(numThreads[x+1])
        efficiencyLocal.append(ef)
    
    timeCluster = []
    file = open(filename2)
    next(file)
    for line in file:
        lineArray = line.split(",")
        lineArray[2] = lineArray[2].replace(" \n","")#removes the \n
        
        timeCluster.append(lineArray[2])
        
    speedUpCluster = []
    efficiencyCluster = []
    for x in range(len(timeCluster) - 1):
        su = float(timeCluster[0])/float(timeCluster[x+1])
        speedUpCluster.append(su)  
        ef = su/float(numThreads[x+1])
        efficiencyCluster.append(ef)
    
    
    print("speedup cluster ",speedUpCluster)
    print("speedup local ", speedUpLocal)
    fname = filename2.split(".")[0]
    plt.plot(numThreads[1:], speedUpLocal)
    plt.plot(numThreads[1:],speedUpCluster)
    plt.legend(["Local", "Cluster"])
    plt.title("Speedup " + fname+ " local")
    plt.show()
    plt.plot(numThreads[1:], efficiencyLocal)
    plt.plot(numThreads[1:], efficiencyCluster)
    plt.legend(["Local", "Cluster"])
    plt.title("Efficiency " + fname + " local")
    plt.show()
   

def get_layerSizes(filename, layer_size):
    file = open(filename)
    for line in file:
        value = line.split(" ")
        layer_size.append(value[0])
    del layer_size[-1]
    

    

layer_size = []
file_names = ["local1.txt","1.txt","local2.txt","2.txt","local03.txt","03.txt","local04.txt","04.txt","local05.txt","05.txt","local06.txt","06.txt","local7.txt","7.txt","local8.txt","8.txt"]
file_results = ["results1Local.txt", "results1Cluster.txt","results2Local.txt", "results2Cluster.txt","results3Local.txt", "results3Cluster.txt","results4Local.txt", "results4Cluster.txt","results5Local.txt", "results5Cluster.txt","results6Local.txt", "results6Cluster.txt","results7Local.txt", "results7Cluster.txt","results8Local.txt", "results8Cluster.txt"]
get_layerSizes("index.txt", layer_size)
print(layer_size)
for x in range (len(layer_size)):
    print("x: ", x)
    endResultLocal ={}
    endResultCluster ={}
    parse(file_names[x*2], endResultLocal,layer_size[x])
    get_final(file_results[x*2], endResultLocal)
    parse(file_names[x*2 +1], endResultCluster,layer_size[x])
    get_final(file_results[x*2 +1], endResultCluster)
    print(file_results[x*2])
    print(file_results[x*2 +1])
    get_results(file_results[x*2], file_results[x*2 +1])


    