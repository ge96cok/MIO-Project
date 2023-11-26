import grasppr.PR
from structure import instance, solution
from algorithms import grasp
import random
from grasppr import graspmod
import numpy as np

def executeInstance(path):
    inst = instance.readInstance(path)
    sol = grasp.execute(inst, 10, -1)
    print("\nBEST SOLUTION:")
    solution.printSolution(sol)

def trygraspmod(path):
    inst = instance.readInstance(path)
    sol = graspmod.execute_with_learning_alpha(inst, 10, 20)
    #sol = graspmod.execute(inst, -1)
    best = -1
    print("\nINITIAL SOLUTIONS:")
    for i in range(np.size(sol)):
        print(sol[i]['sol'])
        print(sol[i]['of'])
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
            print("INIT_SOL: "+str(sol[i]['of']))
            print("GUIDING_SOL: "+str(sol[j]['of']))
            best_set, best_of = grasppr.PR.path_relinking(sol[i], sol[j], inst, 0.2)
            if(best_of > best):
                best = best_of
                best_solution = best_set
    print("\nBEST SOLUTION = "+str(best))


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

    #executeInstance(path)
    trygraspmod(path)
    #trypr(path)