from structure.solution import evaluate

def path_relinking(initial_sol, guiding_sol, approach="greedy"):
    
    # get candidate values that are in guiding solution but not in initial solution
    candidate_set = guiding_sol['sol'].difference(initial_sol['sol'])
    # convert all to a list
    candidate_nodes = sorted(candidate_set)
    guiding_list = sorted(guiding_sol['sol'])
    initial_list = sorted(initial_sol['sol'])
    # candidate_values = initial_sol.symmetric_difference(guiding_sol)

    """
    Todo 
    rename intermediate list as inital_list for less operations
    rewrite as sets???
    """

    #if approach=="greedy":
    # loop over all candidate nodes
    while len(candidate_nodes) > 1:
        i = candidate_nodes[0]
        # add local search here
        best_list = initial_list
        """
        this only works for first time, we do not want to replace already replaced elements
        compute set difference new?
        """
        best_list[0] = i
        best_sol = evaluate(set(best_list))
        # loop over all positions/nodes to replace in set
        for j in len(initial_list):
            intermediate_list = initial_list
            intermediate_list[j] = i
            intermediate_sol = evaluate(set(intermediate_list))
            if intermediate_sol > best_sol:
                best_list = intermediate_list
        # set new inital list 
        # add local search here later
        initial_list = best_list
        candidate_nodes.remove(i)
    
    # if only 1 candidate left define set
    # difference best list and guiding list
    best_set = set(best_list)

    # exchange element with last candidate


    return set(best_list)

def path_relinking_google(self, initial_solution, final_solution):

        # values that differ between initial and guiding solution
        sym_dif = initial_solution.symmetric_difference(final_solution)

        cost_init_sol = self.evaluate_solution(initial_solution)
        cost_final_sol = self.evaluate_solution(final_solution)

        best_cost = min(cost_init_sol, cost_final_sol)

        if cost_init_sol < cost_final_sol:
            best_sol = initial_solution

        else:
            best_sol = final_solution

        current_sol = initial_solution.copy()

        best_dif_cost = 0
        best_change_cost = best_cost

        while len(sym_dif) > 0:

            new_it = True

            for i in sym_dif:

                if i in current_sol:
                    dif_cost = -self.subsets_cost[i]

                else:
                    dif_cost = self.subsets_cost[i]

                current_sol.symmetric_difference_update({i})

                if (dif_cost < best_dif_cost or new_it) and self.is_complete(current_sol):
                    new_it = False

                    best_i = i
                    best_dif_cost = dif_cost

                current_sol.symmetric_difference_update({i})

            current_sol.symmetric_difference_update({best_i})

            best_change_cost += best_dif_cost

            if best_change_cost < best_cost:
                best_cost = best_change_cost
                best_sol = current_sol.copy()

            sym_dif.remove(best_i)

        return best_sol