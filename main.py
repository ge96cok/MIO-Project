from structure import instance, solution
from algorithms import grasp
import random
from grasppr import graspmod
import numpy as np

def executeInstance():
    path = "instances/MDG-a_2_n500_m50.txt"
    inst = instance.readInstance(path)
    sol = grasp.execute(inst, 10, -1)
    print("\nBEST SOLUTION:")
    solution.printSolution(sol)

def trying():
    path = "instances/MDG-a_2_n500_m50.txt"
    inst = instance.readInstance(path)
    sol = graspmod.execute(inst, -1)
    print("\nINITIAL SOLUTIONS:")
    for i in range(np.size(sol)):
        print(sol[i]['sol'])
        print(sol[i]['of'])



if __name__ == '__main__':
    random.seed(1)
    #executeInstance()
    trying()

