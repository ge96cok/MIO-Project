import grasppr.PR
import structure2.instance2
from structure import instance, solution
from algorithms import grasp
import random
from grasppr import graspmod
import datetime
import os

def executeInstance(path):
    inst = instance.readInstance(path)
    sol = grasp.execute(inst, 110, -1)
    print("\nBEST SOLUTION:")
    solution.printSolution(sol)


def executeDir():
    dir = "instances"
    with os.scandir(dir) as files:
        filesnames = [file.name for file in files]
    with open("results50itersAGAIN_AGAIN.csv", "w") as results:
        results.write("file" + "," + "GRASPMOD_of" + "," + "GRASPMOD_runtime (s)" + "," + "PR1_of" + "," + "PR1_runtime (s)" + "," + "PR2_of" + "," + "PR2_runtime (s)" + "," + "PR3_of" + "," + "PR3_runtime (s)" + "," + "PR4_of" + "," + "PR4_runtime (s)" + "," + "PR5_of" + "," + "PR5_runtime (s)" + "\n")
        for f in filesnames:
            path = dir+"/"+f
            print("Solving "+f)
            inst = instance.readInstance(path)
            results.write(f + ",")

            start = datetime.datetime.now()
            sol, best_of = graspmod.execute_with_learning_alpha(inst, 3, 17)
            runtime = datetime.datetime.now() - start
            runtime = round(runtime.total_seconds(), 2)
            results.write(str(round(best_of, 2)) + "," + str(runtime) + ",")
            print("FINISHED GRASPMOD IN " + str(runtime) + " s")

            start = datetime.datetime.now()
            best = -1
            for i in range(len(sol)):
                for j in range(len(sol)):
                    if i != j:
                        best_set, best_of, type = grasppr.PR.path_relinking(sol[i], sol[j], inst, False, 0, False)
                        if (best_of > best):
                            best = best_of
            runtime = datetime.datetime.now() - start
            runtime = round(runtime.total_seconds(), 2)
            results.write(str(round(best, 2)) + "," + str(runtime) + ",")
            print("FINISHED PR1 IN " + str(runtime) + " s")

            start = datetime.datetime.now()
            best = -1
            for i in range(len(sol)):
                for j in range(len(sol)):
                    if i != j:
                        best_set, best_of, type = grasppr.PR.path_relinking(sol[i], sol[j], inst, True, 0, False)
                        if (best_of > best):
                            best = best_of
            runtime = datetime.datetime.now() - start
            runtime = round(runtime.total_seconds(), 2)
            results.write(str(round(best, 2)) + "," + str(runtime) + ",")
            print("FINISHED PR2 IN " + str(runtime) + " s")

            start = datetime.datetime.now()
            best = -1
            for i in range(len(sol)):
                for j in range(len(sol)):
                    if i != j:
                        best_set, best_of, type = grasppr.PR.path_relinking(sol[i], sol[j], inst, False, 0.1, False)
                        if (best_of > best):
                            best = best_of
            runtime = datetime.datetime.now() - start
            runtime = round(runtime.total_seconds(), 2)
            results.write(str(round(best, 2)) + "," + str(runtime) + ",")
            print("FINISHED PR3 IN " + str(runtime) + " s")

            start = datetime.datetime.now()
            best = -1
            for i in range(len(sol)):
                for j in range(len(sol)):
                    if i != j:
                        best_set, best_of, type = grasppr.PR.path_relinking(sol[i], sol[j], inst, False, 0.1, True)
                        if (best_of > best):
                            best = best_of
            runtime = datetime.datetime.now() - start
            runtime = round(runtime.total_seconds(), 2)
            results.write(str(round(best, 2)) + "," + str(runtime) + ",")
            print("FINISHED PR4 IN " + str(runtime) + " s")

            start = datetime.datetime.now()
            best = -1
            for i in range(len(sol)):
                for j in range(len(sol)):
                    if i != j:
                        best_set, best_of, type = grasppr.PR.path_relinking(sol[i], sol[j], inst, True, 0.1, False)
                        if (best_of > best):
                            best = best_of
            runtime = datetime.datetime.now() - start
            runtime = round(runtime.total_seconds(), 2)
            results.write(str(round(best, 2)) + "," + str(runtime) + ",")
            print("FINISHED PR5 IN " + str(runtime) + " s")

            start = datetime.datetime.now()
            sol = grasp.execute(inst, 50, -1)
            runtime = datetime.datetime.now() - start
            runtime = round(runtime.total_seconds(), 2)
            results.write(str(round(sol['of'], 2)) + "," + str(runtime) + "\n")
            print("FINISHED GRASP IN " + str(runtime) + " s")

        print("Finished")



def executeDir2():
    dir = "instances_1b"
    with os.scandir(dir) as files:
        filesnames = [file.name for file in files]
    with open("results100itersBIG.csv", "w") as results:
        results.write("file" + "," + "GRASPMOD_of" + "," + "GRASPMOD_runtime (s)" + "," + "GRASP_of" + "," + "GRASP_runtime (s)" + "\n")
        for f in filesnames:
            path = dir+"/"+f
            print("Solving "+f)
            inst = structure2.instance2.readInstance2(path)
            results.write(f + ",")

            start = datetime.datetime.now()
            best_of = graspmod.execute_with_learning_alpha(inst, 3, 40)
            runtime = datetime.datetime.now() - start
            runtime = round(runtime.total_seconds(), 2)
            results.write(str(round(best_of, 2)) + "," + str(runtime) + ",")
            print("FINISHED GRASPMOD IN " + str(runtime) + " s")

            start = datetime.datetime.now()
            sol = grasp.execute(inst, 100, -1)
            runtime = datetime.datetime.now() - start
            runtime = round(runtime.total_seconds(), 2)
            results.write(str(round(sol['of'], 2)) + "," + str(runtime) + "\n")
            print("FINISHED GRASP IN " + str(runtime) + " s")


        print("Finished")


if __name__ == '__main__':
    random.seed(1)
    executeDir()