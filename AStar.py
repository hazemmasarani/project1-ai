import heapq

class AStar:
    def init(self):
        self.frontier = []
        self.explored = set()    # explored bodes set
        self.end = "0,1,2,3,4,5,6,7,8" # target state
        self.g = {}
        self.f = {}

    def doAStar(self, state, root, heuristic):
        parent = {}
        heapq.heappush(self.frontier, (heuristic(root, self.end, state), root))
        self.g[root] = 0

        while self.frontier:
            cstate = heapq.heappop(self.frontier)[1]
            self.explored.add(cstate)
            # check if a goal was reached
            if cstate == self.end:
                return self.backtrace( parent, root), self.explored

            for adj in state.getNeigbors(cstate):
                self.g[adj] = self.g[cstate] + 1
                h = heuristic(adj,self.end, state)
                if adj in self.f:
                    old_cost = self.f[adj]
                else:
                    old_cost = -1
                if adj not in self.explored and (old_cost, adj) not in self.frontier:
                    heapq.heappush(self.frontier, (h + self.g[adj], adj))
                    self.f[adj] = h + self.g[adj]
                    parent[adj] = cstate
                elif (old_cost, adj) in self.frontier and (h + self.g[adj]) < old_cost:
                    self.frontier.remove((old_cost, adj))
                    heapq.heappush(self.frontier, (h + self.g[adj], adj)) # decrease key
                    self.f[adj] = h + self.g[adj]
                    parent[adj] = cstate

    # returns the right path from the source to the goal
    def backtrace(self, parent, root):
        path = [self.end]
        while path[-1] != root:
            path.append(parent[path[-1]])
        path.reverse()
        return path, len(path)