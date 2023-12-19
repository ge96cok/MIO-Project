#To get initial solutions for PR
import numpy as np
from structure import instance, solution
from algorithms import grasp
from constructives import cgrasp
from localsearch import lsbestimp
import random

def execute_without_alpha(inst, num_rand):
    #TODO: write graspmod-execute-method without alpha-parameter
    initsol = []
    best = None
    best_of = -1
    best_average_alpha = -1
    best_alpha = -1
    alphas = []
    Ais = []
    if num_rand < 1:
        num_rand = 1
    for j in range(num_rand):
        Ais.append(set())
        alphas.append(random.random())
        for i in range(20):
            sol = cgrasp.construct(inst, alphas[j])
            lsbestimp.improve(sol)
            initsol.append(sol)
            Ais[j].add(sol['of'])
            if sol['of'] > best_of:
                best_of = sol['of']
                best = sol
                best_alpha = alphas[j]
    #calculate the best average alpha:
    for i in range(len(Ais)):
        Ais[i] = np.average(list(Ais[i]))
        if best_average_alpha < 0 or Ais[best_average_alpha] < Ais[i]:
            best_average_alpha = i
    #iterate over alphas near best_average_alpha:
    for j in range(10):
        a = alphas[best_average_alpha]-0.03+0.6*random.random()
        #a = best_alpha-0.03+0.6*random.random()
        if a <= 1 and a >= 0:
            sol = cgrasp.construct(inst, a)
            lsbestimp.improve(sol)
            initsol.append(sol)
            if sol['of'] > best_of:
                best_of = sol['of']
                best = sol
    print("\n BEST ALPHA = "+str(best_alpha))
    print("\n BEST AVERAGE ALPHA = "+str(alphas[best_average_alpha]))
    return calcInitSet(initsol, len(initsol), inst, -1, best)

def execute_with_learning_alpha(inst, iniciate_alpha, learning_alpha):
    initsol = []
    best = None
    best_of = -1
    alphas = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    Ais = []
    Qis = []
    Pis = []
    for i in range(11):
        Ais.append(set())
        Qis.append(0)
        Pis.append(0)
    for j in range(iniciate_alpha):
        for i in range(11):             #11 = size of alphas
            sol = cgrasp.construct(inst, alphas[i])
            lsbestimp.improve(sol)
            initsol.append(sol)
            Ais[i].add(sol['of'])
            if sol['of'] > best_of:
                best_of = sol['of']
                best = sol
    for j in range(learning_alpha):
        for i in range(len(Qis)):
            Qis[i] = best_of/sum(Ais[i])/len(Ais[i])
        for i in range(len(Pis)):
            Pis[i] = Qis[i]/sum(Qis)
        alpha = random.choices(alphas, Pis)[0]
        sol = cgrasp.construct(inst, alpha)
        lsbestimp.improve(sol)
        initsol.append(sol)
        if sol['of'] > best_of:
            best_of = sol['of']
            best = sol
    print("\nALPHA PROPS = "+str(Pis))

    return calcInitSet(initsol, len(initsol), inst, -1, best)

def execute(inst, alpha):
    #create Array for initial solutions
    initsol = []
    #calculate number of iterations = 10% of n
    n = inst['n']
    #iter = int(n*0.1)
    iter = 75
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
    p = inst['p']
    n = inst['n']
    initSet = {'n': size, 'p': int(n*0.05), 'd': []}
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