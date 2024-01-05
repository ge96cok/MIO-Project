#from structure.solution import evaluate#, removeFromSolution
import structure.solution as solution
import localsearch.lsbestimp as lsbestimp

def createPRSol(set, of, inst):
    sol = {}
    sol['instance'] = inst
    sol['sol'] = set
    sol['of'] = of
    return sol

def evaluate(set, sol):
    of = 0
    for s1 in set:
        for s2 in set:
            if s1 < s2:
                of += sol['instance']['d'][s1][s2]
    return of

def printSolution(set, of, type):
    print("Best PR Solution: ", end="")
    for s in set:
        print(s, end=" ")
    print()
    print("Objective Value: "+str(round(of, 2)))
    print("Type:", type)

# simple: select a random element to enter the intermediate set and find the best to leave 
# freqLS: if 0 no local search is performed, otherwise local search is performed every freqLS*len(nodes_enter) steps
# advLS: if True, use local search solution as new initial sol for next round

"""
To check: 
simple=False, freqLS=0, advLS=False
simple=True, freqLS=0, advLS=False
simple=False, freqLS=0.1, advLS=False
simple=False, freqLS=0.1, advLS=True

"""

def path_relinking(initial_sol, guiding_sol, inst, simple=False, freqLS=0, advLS=False):

    # catch errors
    if advLS==True and freqLS==0:
        print("LS could not be performed as freqLS is not specified. Normal PR is performed.")

    sol = solution.createEmptySolution(inst)

    initial_set = initial_sol['sol']
    guiding_set = guiding_sol['sol']

    # save best from initial and guiding solution
    best_of = max(initial_sol['of'], guiding_sol['of'])
    if best_of == initial_sol['of']:
        best_set = initial_set
        type = "initial solution"
    else:
        best_set = guiding_set
        type = "guiding solution"

    # nodes to enter the initial set
    nodes_enter = guiding_set.difference(initial_set)
    # nodes from guiding set already present in the inital set
    nodes_keep = initial_set.intersection(guiding_set)
    # nodes in intermediate set to exchange with a entering node
    nodes_exchange = initial_set.difference(nodes_keep)

    best_pr_of = -1
    # set a counter for LS and calculate steps for LS from freqLS
    counter = 1
    nodes_check = set()
    stepsLS = int(freqLS*len(nodes_enter))
    # counter to stop LS in case of edge cases
    if freqLS>0:
        maxLS = int(1/freqLS)
    counterLS = 0
    
    while len(nodes_enter) > 0:
        # force at least one new node to enter with -1
        current_of = -1
        if simple==True:
            i = nodes_enter.pop()
            nodes_enter = [i]
        for i in nodes_enter:
            # build intermediate_set
            intermediate_set = nodes_keep.union(nodes_exchange)
            intermediate_set.add(i)
            # candidates to exchange with entering node
            for j in nodes_exchange:          
                # check for best node to leave
                intermediate_set.remove(j)
                intermediate_of = evaluate(intermediate_set, sol)
                if  intermediate_of > current_of:
                    best_enter = i
                    best_leave = j
                    current_of = intermediate_of
                # rebuild nodes to exchange for next iter
                intermediate_set.add(j)
            intermediate_set.remove(i)
        # remove leaving and entering nodes      
        nodes_exchange.remove(best_leave)
        nodes_enter.remove(best_enter)
        nodes_keep.add(best_enter)

        # check for best pr set vs best set from initial and global
        best_pr_set = nodes_keep.union(nodes_exchange)
        best_pr_of = evaluate(best_pr_set, sol)
        if best_pr_of > round(best_of,2):
            best_of = best_pr_of
            best_set = best_pr_set
            type = "path relinking"

        # check if perform LS
        if freqLS > 0:
            # construct sol from set
            best_ls_sol = createPRSol(best_pr_set, best_pr_of, inst)
            if counter == stepsLS:
                # perform LS
                lsbestimp.improve(best_ls_sol)
                #print("LS -> "+str(round(best_ls_sol['of'], 2)))
                counter = 1
                if advLS==True and freqLS > 0:
                    # break if we run into edge cases
                    if counterLS >= maxLS:
                        break
                    else:
                        counterLS += 1
                    # use LS set as inital set for next PR iteration
                    initial_set = best_ls_sol['sol']
                    nodes_enter = guiding_set.difference(initial_set)
                    nodes_keep = initial_set.intersection(guiding_set)
                    # break if initial set stays the same over two loops as LS moved too far from guiding solution
                    # we can do this since we know that after the first iteration of the while loop 
                    # there is at least one node to keep
                    # of course we could also check other sets than nodes_keep
                    if nodes_keep == nodes_check:
                        break
                    nodes_check = nodes_keep.copy()
                    nodes_exchange = initial_set.difference(nodes_keep)
            else:
                counter += 1
            if round(best_ls_sol['of'], 2) > round(best_of,2):
                best_of = round(best_ls_sol['of'], 2)
                best_set = best_ls_sol['sol']
                type = "local search"            

    printSolution(best_set, best_of, type)
    return best_set, best_of, type  



