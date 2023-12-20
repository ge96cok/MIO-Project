# MIO-Project

Project objective:
determine best alpha
determine best size of Elite Set

To implement:
loop over all instances
write a loop to test different alphas
write Path Relinking function

Ideas to improve solution:
apply LS during PR
determine Elite Set not from one random seed but several?

Ask Rafa about use of random seed == 1 for fairness between groups?

#########################################################################

Report:

    -Implementing a modified version of Grasp to calculate elite set:
    -Reactive algorithm / learning alpha

    -Implementing Path-Relinking algorithm
    -Local Search adaptation

    -Results


Graspmod:
Our first idea is to modify the given GRASP-algorithm in order to obtain a set of solutions, 
so that we can apply the Path-Relinking (PR) method on them.
The modiefied algorithm consists in two parts: Calculating more solutions with the given GRASP-algorithm 
and then apply the GRASP method again on this set of solutions.
That way we can obtain a set of solutions that are in some kind distant from each other.
We hope to get better results this way, since there are more PR-steps between the obtained solutions.

-1. Calculating various Solutions:

    Our first idea was to calculate some Solutions with the given GRASP-algorithm and a pre-calculated alpha and to safe the solutions in an array.
    But the results we obtained did not vary too much from the solution obtained with the original GRASP with random alpha.
    So we wanted to implement a "learning alpha parameter".
    After some investigation we found some papers explaining Reactive GRASP. We decided to try the Reactive GRASP on our instanses.
    So we started with a discrete set of values for alpha [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1].
    Firstly each alpha is picked by the algorithm with the same probability.
    Reactive GRASP adaptively changes the probabilities to which each alpha is picked, to favor values that produce good solutions.
    To start the learning-process with some solutions for every alpha, we calculate a pre-determined amount of solutions for each of them.
    Then, during the learning-process we need to define our value of the incumbent (i.e. best so far) solution and
    the average value of the solutions obtained with each of the alphas. With this we can calculate new probabilities for the alphas.
    The problem we see with this method is the limited amount of alpha parameters used. For the whole range from 0 to 1
    there is just a fixed set of alphas. And also the were just minor differences in the probabilities for the alphas,
    which mean, the solutions did not differ a lot.
    We belive that maybe we should use more alphas and more iterations, but since we want a fast algorithm, we thought of another idea. 
    
    We start again with a discrete set of values for alpha, but this time the number of values in this set is given as an argument in 
    the function. Also we don't use evenly distributed values, but instead we use random numbers. 
    We also found out by experimenting with alpha, that there are even important differances between an alpha and an alpha+0.05 so
    it would only be logical to inspect a small area around a good alpha, to see if we can improve it.
    That's why we do the same thing again: in a given intervall around our so far best alpha we calculate some random numbers and compare
    the values of their solutions. 
    Every in this process calculated solution can be safed in our array of solutions, since they are calculated anyway.
    
-2. Calculating a initial set for PR:

    Now that we have a lot of solutions for our instance, we can use the given GRASP-method on them to obtain a set of sufficiently different solutions.
    Therefore we need to create an instance out of them. Obviously our new nodes are the solutions, but we need to calculate the distance 
    between solutions in an efficient way. We decided to define the distance between two solutions as the sum of the distances between unequal
    nodes of that solutions.
    So now that we have a new instance with nodes and the distances between every node, we can use GRASP on this instance to obtain 
    a set of solutions, that are different enough from each other.

-Adjustments:

    (Keeping so far best solution.)
    Since GRASP doesn't doesn't consider the values of the solutions, but just the distances between the solutions, we want to
    modify the resulting set. Although we want solutions to differ from each other, we also want to keep our so far best solution.
    So if GRASP chooses a set of solutions, that doesn't contain the best so far, we will remove the worst solutions from the set 
    and add our best. So we can guarantee, that this aplication of GRASP will not make us lose value in the result.

-Changeable Parameter:
    
    We want to point out, that there are plenty of parameters that can be changed.
    For every random number we use as alpha, we calculate 20 solutions. Obviously we could calculate more or less than that. 
    
    --------- (Explain a little more here) ------------------
    
    And for the incumbent alpha, we calculate 10 more alphas in an intervall of size 0.6 around it. Why? Well, because! 
    
    Another parameter is the size of the initial set. We chose it to be 5% of the size of the instance. 
    And we are not determining an alpha for the GRASP on our new instance of solutions. (Should we change that? Can we change that?) 
    
    Gives space for a parameteranalysis.

Next we want to use PR to improve our solutions.
















