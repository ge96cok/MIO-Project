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

def executeInstance(path):
    inst = instance.readInstance(path)
    sol = grasp.execute(inst, 110, -1)
    print("\nBEST SOLUTION:")
    solution.printSolution(sol)

def trygraspmod(path):
    inst = instance.readInstance(path)
    #sol = graspmod.execute(inst, -1)
    sol = graspmod.execute_without_alpha(inst, 5)
    #sol = graspmod.execute_with_learning_alpha(inst, 10, 20)
    best = -1
#    print("\nINITIAL SOLUTIONS:")
    for i in range(np.size(sol)):
#        print(sol[i]['sol'])
#        print(sol[i]['of'])
        if(best < sol[i]['of']):
            best = sol[i]['of']
    print("\nBEST SOLUTION = "+ str(best))

"""
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
                best_set, best_of = grasppr.PR.path_relinking(sol[i], sol[j], inst)
                if(best_of > best):
                    best = best_of
                    best_solution = best_set
    print("\nBEST SOLUTION = "+str(best))
"""

def trypr(path):
    inst = instance.readInstance(path)
    sol = graspmod.execute(inst, -1)
    best = -1
    best_solution = None
    freq = [0,0.05,0.1,0.2,0.3]
    with open("pr_test500.csv", "w") as results:
        for f in freq:
            for i in range(len(sol)):
                for j in range(len(sol)):
                    if i != j:
                        results.write("freq" + "," + "i" + "," + "j" + "," + "of" + "," + "type" + "," + "runtime" + "\n")
                        results.write(str(f) + "," + str(i) + "," + str(j) + ",")
                        print("INIT_SOL: "+str(sol[i]['of']))
                        print("GUIDING_SOL: "+str(sol[j]['of']))
                        start = datetime.datetime.now()
                        best_set, best_of, type = grasppr.PR.path_relinking(sol[i], sol[j], inst, freqLS=f)
                        runtime = datetime.datetime.now() - start
                        runtime = round(runtime.total_seconds(), 2)
                        results.write(str(round(best_of,2)) + "," + str(type) + "," + str(runtime)+"\n")
                        if(best_of > best):
                            best = best_of
                            best_solution = best_set
            print("\nBEST SOLUTION = "+str(best))



if __name__ == '__testpr__':
    trypr("instances/MDG-a_2_n500_m50.txt")
