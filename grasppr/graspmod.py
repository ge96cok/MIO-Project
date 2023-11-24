#To get initial solutions for PR

from structure import instance, solution
from algorithms import grasp
from constructives import cgrasp
from localsearch import lsbestimp
import random

def execute(inst, alpha):
    #create Matrix for initial solutions
    initsol = []
    #calculate number of iterations = 10% of n
    n = inst['n']
    iter = int(n*0.1)
    for i in range(iter):
        sol = cgrasp.construct(inst, alpha)
        lsbestimp.improve(sol)
        initsol.append(sol)
        initalSet = calcInitSet(sol, iter)
    return initalSet


def calcInitSet(set, size):
    #Create new instance of solutions with distances as dictionary
    initSet = {}
    initSet['n'] = size
    initSet['p'] = size/2
    initSet['d'] = []
    for i in range(size):
        instance['d'].append([0] * size)
    for i in range(size):
        for j in range(i + 1, size):
            #Get pairwise distances as sum of distances between non-equal nodes
            d = set[i]['sol']#......

            instance['d'][i][j] = d
            instance['d'][j][i] = d
    #use grasp on new instance
    return initSet
