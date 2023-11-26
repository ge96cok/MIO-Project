#To get initial solutions for PR
import numpy as np
from structure import instance, solution
from algorithms import grasp
from constructives import cgrasp
from localsearch import lsbestimp
import random

def execute(inst, alpha):
    #create Vector for initial solutions
    initsol = []
    #calculate number of iterations = 10% of n
    n = inst['n']
    #iter = int(n*0.1)
    iter = 10
    best = None
    best_of = -1
    for i in range(iter):
        sol = cgrasp.construct(inst, alpha)
        lsbestimp.improve(sol)
        initsol.append(sol)
        if sol['of'] > best_of:
            best_of = sol['of']
            best = sol

    return calcInitSet(initsol, iter, inst, alpha, best)


def calcInitSet(initsol, size, inst, alpha, best_sol):
    #Create new instance of solutions with distances as dictionary in order to use GRASP on it
    initSet = {'n': size, 'p': size / 2, 'd': []}
    for i in range(size):
        initSet['d'].append([0] * size)

    #i and j are the nodes (numer i and j of vector initsol)
    for i in range(size):
        for j in range(i + 1, size):
        #Get pairwise distances as sum of distances between non-equal nodes
            #check what nodes are different:
            compare1 = list(initsol[i]['sol'].difference(initsol[j]['sol']))
            compare2 = list(initsol[j]['sol'].difference(initsol[i]['sol']))
            d = 0
            index1 = 0
            index2 = 0
            finalIndex = len(compare1)
            while index1 < finalIndex:
                #sum of the distances between every node in compare1&2
                d += inst['d'][compare1[index1]][compare2[index2]]
                if index2 == len(compare1)-1:
                    index1 += 1
                    index2 = 0
                else:
                    index2 += 1

            initSet['d'][i][j] = d
            initSet['d'][j][i] = d


    #########use grasp on new instance##########

    graspsol = grasp.execute(initSet, size, alpha)
    worst = None
    worst_of = 0x3f3f3f
    best_sol_included = False
    best_of = best_sol['of']
    if graspsol is None:
        return None
    else:
        #in result we will collect the solutions of initsol that GRASP says we keep
        result = []
        for i in graspsol['sol']:
            result.append(initsol[i])
            if(initsol[i]['of'] >= best_of):
                best_sol_included = True
            if(initsol[i]['of'] < worst_of):
                worst = initsol[i]
                worst_of = initsol[i]['of']

    if (not best_sol_included):
        result.remove(worst)
        result.append(best_sol)

    return result