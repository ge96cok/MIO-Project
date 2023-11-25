from structure.solution import evaluate

def path_relinking(initial_sol, guiding_sol, probLocalSearch=0):

    # remove if initial_sol, guiding_sol are sets already
    initial_set = initial_sol['sol']
    guiding_set = guiding_sol['sol']

    # save best from initial and guiding solution
    initial_of = evaluate(initial_set)
    guiding_of = evaluate(guiding_set)
    best_of = min(initial_of, guiding_of)
    if best_of == initial_of:
        best_set = initial_set
    else:
        best_set = guiding_set

    intermediate_set = initial_set.copy() # copy needed?

    # nodes to enter the initial set
    nodes_enter = guiding_set.difference(initial_set)
    # nodes from guiding set already present in the inital set
    nodes_keep = initial_set.intersection(guiding_set)
    # nodes in intermediate set to exchange with a entering node
    nodes_exchange = intermediate_set.difference(nodes_keep)

    # enter all nodes
    while len(nodes_enter) > 0:
        # force at least one new node to enter 
        current_of = -1
        for i in nodes_enter:
            # build intermediate_set
            intermediate_set = nodes_keep.union(nodes_exchange)
            intermediate_set.add(i)
            # candidates to exchange with entering node
            for j in nodes_exchange:          
                # check for best node to leave
                intermediate_set.remove(j)
                intermediate_of = evaluate(intermediate_set)
                if  intermediate_of < current_of or current_of < 0:
                    best_enter = i
                    best_leave = j
                    current_of = intermediate_of
                    current_set = intermediate_set 
                # rebuild nodes to exchange for next iter
                intermediate_set.add(j)
            intermediate_set.remove(i)
        # remove leaving and entering nodes 
        nodes_exchange.remove(best_leave)
        nodes_enter.remove(best_enter)
        
        # check for best pr set vs best set from initial and global
        best_pr_set = current_set
        best_pr_of =  evaluate(best_pr_set)
        if  best_pr_of < best_of:
            best_of = best_pr_of
            best_set = best_pr_set
        
    # add local search here, just with a probability or a counter?
    # if probLocalSearch > 0

    return best_set