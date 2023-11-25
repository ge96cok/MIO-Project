from structure import instance, solution
from algorithms import grasp
import random
from grasppr import graspmod, PR
import numpy as np

path = "instances/MDG-a_2_n500_m50.txt"
inst = instance.readInstance(path)
random.seed(1)
sol1 = grasp.execute(inst, 1, -1)
random.seed(2)
sol2 = grasp.execute(inst, 1, -1)
print("\nBEST SOLUTION 1:")
solution.printSolution(sol1)
print("\nBEST SOLUTION 2:")
solution.printSolution(sol2)

pr_test, of = PR.path_relinking(sol1, sol2, inst)
PR.printSolution(pr_test, of)

