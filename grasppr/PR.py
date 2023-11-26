#from structure.solution import evaluate#, removeFromSolution
import structure.solution as solution

def path_relinking(initial_sol, guiding_sol, inst, probLocalSearch=0):

    sol = solution.createEmptySolution(inst)

    initial_set = initial_sol['sol']
    guiding_set = guiding_sol['sol']

    # save best from initial and guiding solution
    initial_of = initial_sol['of']
    guiding_of = guiding_sol['of']
    best_of = max(initial_of, guiding_of)
    if best_of == initial_of:
        best_set = initial_set
    else:
        best_set = guiding_set

    # nodes to enter the initial set
    nodes_enter = guiding_set.difference(initial_set)
    # nodes from guiding set already present in the inital set
    nodes_keep = initial_set.intersection(guiding_set)
    # nodes in intermediate set to exchange with a entering node
    nodes_exchange = initial_set.difference(nodes_keep)

    best_pr_of = -1
    
    # enter all nodes
    while len(nodes_enter) > 0:
        # force at least one new node to enter with -1
        current_of = -1
        test1= True
        for i in nodes_enter:
            # build intermediate_set
            intermediate_set = nodes_keep.union(nodes_exchange)
            intermediate_set.add(i)
            # candidates to exchange with entering node
            for j in nodes_exchange:          
                # check for best node to leave
                intermediate_set.remove(j)
                intermediate_of = evaluate(intermediate_set, sol)
                #if test1: print(intermediate_of)
                if  intermediate_of > current_of:
                    best_enter = i
                    best_leave = j
                    current_of = intermediate_of
                    #current_set = intermediate_set 
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
        if best_pr_of > best_of:
            best_of = best_pr_of
            best_set = best_pr_set
     
        #print("Step Solution: ", end="")
        #for s in best_pr_set:
        #    print(s, end=" ")
        #print()
        #print("Objective Value: "+str(round(best_pr_of, 2)))      
        
    # add local search here, just with a probability or a counter?
    # if probLocalSearch > 0

    printSolution(best_set, best_of)
    return best_set, best_of

def evaluate(set, sol):
    of = 0
    for s1 in set:
        for s2 in set:
            if s1 < s2:
                of += sol['instance']['d'][s1][s2]
    return of

def printSolution(set, of):
    print("Best PR solution: ", end="")
    for s in set:
        print(s, end=" ")
    print()
    print("Objective Value: "+str(round(of, 2)))
