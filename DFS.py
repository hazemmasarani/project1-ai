class DFS:
    def init(self):
        self.frontier = []
        self.explored = set()    # explored bodes set
        self.end = "0,1,2,3,4,5,6,7,8" # target state

    def doDFS(self, state,root):
        parent = {}
        self.frontier.append(root)
        while self.frontier:
            cstate = self.frontier.pop()
            self.explored.add(cstate)
            if cstate == self.end: # check if the goal was reached
                return self.backtrace( parent, root), self.explored
            for adj in state.getNeigbors(cstate): # add the adj node to the frontier list
                if adj not in self.explored and adj not in self.frontier:
                    parent[adj] = cstate
                    self.frontier.append(adj)

    # returns the right path from the source to the goal
    def backtrace(self, parent, root):
        path = [self.end]
        while path[-1] != root:
            path.append(parent[path[-1]])
        path.reverse()
        return path, len(path)