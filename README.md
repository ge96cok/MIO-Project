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

    -1. Calculating various Solutions
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
    ...

Adjustments:
(Keeping so far best solution.)
















