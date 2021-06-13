import timeit

from BFS import BFS
from DFS import DFS
from AStar import AStar


from State import State
import math

def manhattanDistance(cstate, end, state):
   currX = state.getX(cstate)
   goalX = state.getX(end)
   currY = state.getY(cstate)
   goalY = state.getY(end)
   h = []
   for x1, x2, y1, y2 in zip(currX, goalX, currY, goalY):
      h.append(abs(x1 - x2) + abs(y1 - y2))
   return sum(h)

def euclideanDistance(cstate, end, state):
   currX = state.getX(cstate)
   goalX = state.getX(end)
   currY = state.getY(cstate)
   goalY = state.getY(end)
   h = []
   for x1, x2, y1, y2 in zip(currX, goalX, currY, goalY):
      h.append(math.sqrt((x1 - x2)**2 + (y1 - y2)**2))
   return sum(h)

def printBoard(s):
   print("")
   x = 0
   while x < 9:
        c = s[x]
        if c == "0":
           c = " "
        if x % 3 == 0:
            print('.---' * 3 + ".")
            print("| " + c + " |", end="")
        elif x % 3 == 1:
            print(" " + c + " |", end="")
        else:
            print(" " + c + " |")
        if x == 8:
            print('.---' * 3 + ".")
        x = x + 1

def BFSAlg(state, iniState):
    cost_path = 0
    bfs = BFS()
    bfs.init()
    start = timeit.default_timer()
    BFSAlg = bfs.doBFS(state, iniState)
    path = BFSAlg[0][0]
    depth = BFSAlg[0][1]
    explored = BFSAlg[1]
    stop = timeit.default_timer()
    print('============= Time =============')
    print(stop - start)
    print('============= Depth =============')
    print(depth)
    print('============= Explored =============')
    print(explored)
    print('============= Path =============')
    for i in path:
        printBoard(i.split(','))
        cost_path += 1
    print('============= Cost =============')
    print(cost_path)

def DFSAlg(state, iniState):
    cost_path = 0
    dfs = DFS()
    dfs.init()
    start = timeit.default_timer()
    DFSAlg = dfs.doDFS(state, iniState)
    path = DFSAlg[0][0]
    depth = DFSAlg[0][1]
    explored = DFSAlg[1]
    stop = timeit.default_timer()
    print('============= Time =============')
    print(stop - start)
    print('============= Depth =============')
    print(depth)
    print('============= Explored =============')
    print(explored)
    print('============= Path =============')
    for i in path:
        printBoard(i.split(','))
        cost_path += 1
    print('============= Cost =============')
    print(cost_path)

def AStarAlg(state, heuristic, iniState):
    cost_path = 0
    a = AStar()
    a.init()
    start = timeit.default_timer()
    aAlgo = a.doAStar(state, iniState, heuristic)
    path = aAlgo[0][0]
    depth = aAlgo[0][1]
    explored = aAlgo[1]
    stop = timeit.default_timer()
    print('============= Time =============')
    print(stop - start)
    print('============= Depth =============')
    print(depth)
    print('============= Explored =============')
    print(explored)
    print('============= Path =============')
    for i in path:
        printBoard(i.split(','))
        cost_path += 1
    print('============= Cost =============')
    print(cost_path)

if __name__ == '__main__':
    state = State()
    print('1 : BFS ,   2: DFS ,   3 : A* manhattanDistance ,   4 : A* euclideanDistance')
    n = int(input('choose number of algorithm: '))
    iniState = input('Enter the initial state eg: 1,2,5,3,4,0,6,7,8 : ')
    if n == 1:
        BFSAlg(state,iniState)
    elif n == 2:
        DFSAlg(state,iniState)
    elif n == 3:
        AStarAlg(state, manhattanDistance,iniState)
    elif n == 4:
        AStarAlg(state, euclideanDistance,iniState)




