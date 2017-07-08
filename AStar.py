# Astar.py, April 2017
# Based on ItrDFS.py, Ver 0.3, April 11, 2017.

# A* Search of a problem space.
# The Problem should be given in a separate Python
# file using the "QUIET" file format.
# See the TowerOfHanoi.py example file for details.
# Examples of Usage:

# python3 AStar.py EightPuzzleWithHeuristics h_manhattan

'''
Derek Wang
CSE 415 Spring 2017
Tanimoto
April 19

HW 3
'''

import sys
from queue import PriorityQueue

# DO NOT CHANGE THIS SECTION
if sys.argv==[''] or len(sys.argv)<2:
    import EightPuzzleWithHeuristics as Problem
    heuristics = lambda s: Problem.HEURISTICS['h_manhattan'](s)

else:
    import importlib
    Problem = importlib.import_module(sys.argv[1])
    heuristics = lambda s: Problem.HEURISTICS[sys.argv[2]](s)


print("\nWelcome to AStar")
COUNT = None
BACKLINKS = {}

# DO NOT CHANGE THIS SECTION
def runAStar():
    #initial_state = Problem.CREATE_INITIAL_STATE(keyVal)
    initial_state = Problem.CREATE_INITIAL_STATE()
    print("Initial State:")
    print(initial_state)
    global COUNT, BACKLINKS
    COUNT = 0
    BACKLINKS = {}
    path, name = AStar(initial_state)
    print(str(COUNT)+" states examined.")
    return path, name

# A star search algorithm
# TODO: finish A star implementation
def AStar(initial_state):
    global COUNT, BACKLINKS
    # TODO: initialze and put first state into
    # priority queue with respective priority
    # add any auxiliary data structures as needed
    OPEN = PriorityQueue()
    OPEN.put((0,initial_state))
    SEEN = []
    CLOSED = []
    G_SCORE = {}
    G_SCORE[initial_state] = 0
    BACKLINKS[initial_state] = -1
    MAX_GSCORE = 0

    while not OPEN.empty():
        S = OPEN.get()[1]
        while S in CLOSED:
            S = OPEN.get()[1]
        CLOSED.append(S)

        # DO NOT CHANGE THIS SECTION: begining
        if Problem.GOAL_TEST(S):
            print(Problem.GOAL_MESSAGE_FUNCTION(S))
            # path = backtrace(S)
            print(len(BACKLINKS))
            return path, Problem.PROBLEM_NAME
        # DO NOT CHANGE THIS SECTION: end

        COUNT += 1
        # TODO: finish A* implementation
        for op in Problem.OPERATORS:
            if op.precond(S):
                next_state = op.state_transf(S)
                # This is a valid move so you need to calculate F(n) = G(n) + H(n)
                if next_state not in SEEN and next_state not in CLOSED:
                    if S in G_SCORE:
                        next_G_SCORE = 1 + G_SCORE[S]
                    else:
                        next_G_SCORE = MAX_GSCORE
                    G_SCORE[next_state] = next_G_SCORE
                    if next_G_SCORE > MAX_GSCORE:
                        MAX_GSCORE = next_G_SCORE
                    next_F_SCORE = next_G_SCORE + heuristics(next_state)
                    OPEN.put((next_F_SCORE, next_state))
                    SEEN.append(next_state)
                    BACKLINKS[next_state] = S
                    print(S)


# DO NOT CHANGE
def backtrace(S):
    global BACKLINKS
    path = []
    while not S == -1:
        path.append(S)
        S = BACKLINKS[S]
    path.reverse()
    print("Solution path: ")
    for s in path:
        print(s)
    print("\nPath length = "+str(len(path)-1))
    return path

if __name__=='__main__':
    path, name = runAStar()
