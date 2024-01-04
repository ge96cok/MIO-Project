import grasppr.PR
from structure import instance, solution
from algorithms import grasp
import random
from grasppr import graspmod
import numpy as np
import pandas as pd
import datetime
import os
import csv
import time

def executeInstance(path):
    inst = instance.readInstance(path)
    sol = grasp.execute(inst, 110, -1)
    print("\nBEST SOLUTION:")
    solution.printSolution(sol)

def trygraspmod(path):
    inst = instance.readInstance(path)
    #sol = graspmod.execute(inst, -1)
    sol = graspmod.execute_without_alpha(inst)
    #sol = graspmod.execute_with_learning_alpha(inst, 10, 20)
    best = -1
#    print("\nINITIAL SOLUTIONS:")
    for i in range(np.size(sol)):
#        print(sol[i]['sol'])
#        print(sol[i]['of'])
        if(best < sol[i]['of']):
            best = sol[i]['of']
    print("\nBEST SOLUTION = "+ str(best))

def trypr(path):
    inst = instance.readInstance(path)
    sol = graspmod.execute(inst, -1)
    best = -1
    best_solution = None
    for i in range(len(sol)):
        for j in range(len(sol)):
            if i != j:
                print("INIT_SOL: "+str(sol[i]['of']))
                print("GUIDING_SOL: "+str(sol[j]['of']))
                best_set, best_of = grasppr.PR.path_relinking(sol[i], sol[j], inst, 0.2)
                if(best_of > best):
                    best = best_of
                    best_solution = best_set
    print("\nBEST SOLUTION = "+str(best))

"""
if __name__ == '__main__':
    random.seed(1)
    instancesss = ["instances/MDG-a_1_100_m10.txt",
                   "instances/MDG-a_2_n500_m50.txt",
                   "instances/MDG-a_4_100_m10.txt",
                   "instances/MDG-a_5_n500_m50.txt",
                   "instances/MDG-a_6_n500_m50.txt",
                   "instances/MDG-a_9_n500_m50.txt",
                   "instances/MDG-a_10_100_m10.txt",
                   "instances/MDG-a_12_100_m10.txt",
                   "instances/MDG-a_13_n500_m50.txt",
                   "instances/MDG-a_14_100_m10.txt",
                   "instances/MDG-a_16_n500_m50.txt",
                   "instances/MDG-a_17_n500_m50.txt",
                   "instances/MDG-a_19_n500_m50.txt",
                   "instances/MDG-a_20_100_m10.txt",
                   "instances/MDG-a_20_n500_m50.txt",
                   ]
    path = instancesss[1]
    start_time = time.time()
    #executeInstance(path)
    trygraspmod(path)
    #trypr(path)
    end_time = time.time()
    print("Time taken to run the code:", end_time - start_time, "seconds")
"""

# try basic first
# then run for all versions

def executeDir():
    dir = "instances"
    with os.scandir(dir) as files:
        filesnames = [file.name for file in files]
    with open("results.csv", "w") as results:
        results.write("file" + "," + "of" + "," + "runtime (s)" + "\n")
        for f in filesnames:
            path = dir+"/"+f
            print("Solving "+f)
            inst = instance.readInstance(path)
            results.write(f + ",")
            start = datetime.datetime.now()

            #sol = graspmod.execute_without_alpha(inst, 5)
            sol = graspmod.execute_with_learning_alpha(inst, 20, 20)
            best = -1
            best_solution = None
            for i in range(len(sol)):
                for j in range(len(sol)):
                    if i != j:
                        print("INIT_SOL: " + str(sol[i]['of']))
                        print("GUIDING_SOL: " + str(sol[j]['of']))
                        best_set, best_of = grasppr.PR.path_relinking(sol[i], sol[j], inst, 0.2)
                        if (best_of > best):
                            best = best_of
                            best_solution = best_set
            print("\nBEST SOLUTION = " + str(best))
            #sol = grasp.execute(inst, 10, -1)

            runtime = datetime.datetime.now() - start
            runtime = round(runtime.total_seconds(), 2)
            #solution.printSolution(sol)
            #results.write(str(round(sol['of'], 2))+","+str(runtime)+"\n")
            results.write(str(round(best, 2)) + "," + str(runtime) + "\n")
            print("Runtime:" + str(runtime))
        print("Finished")

if __name__ == '__main__':
    random.seed(1)
    executeDir()





    #res = pd.read_csv("results.csv")
    #print(res)