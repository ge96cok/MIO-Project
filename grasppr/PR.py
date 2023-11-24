def path_relinking(initial_sol, guiding_sol, approach="greedy"):
    
    # get candidate values that are in guiding solution but not in initial solution
    candidate_nodes = guiding_sol['sol'].difference(initial_sol['sol'])
    # candidate_values = initial_sol.symmetric_difference(guiding_sol)

    if approach=="greedy":

        while len(candidate_nodes) > 0:

            # loop over all spots in initial solution
            for i in len(initial_sol['sol']):
                # set baseline intermediate sol as initial sol with 1st candidate node at first position
                pr_init_sol = 
                # loop over all candidate values
                for j in candidate_nodes:
                    # exchange node i in initial_sol with node j in candidate nodes
                    intermediate_sol = initial_sol['sol'][j]

            # pop chosen node from candiate nodes



        return intermediate_sol = best_sol


def path_relinking(self, initial_solution, final_solution):

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