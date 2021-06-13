class State:
    boundDown = 6
    boundUp = 2

    def getNeigbors(self, initialState):
        self.children = []
        board = initialState.split(',')
        idx = board.index('0')
        self.__moveLeft(board, idx)
        self.__moveRight(board, idx)
        self.__moveUp(board, idx)
        self.__moveDown(board, idx)
        return self.children


    def __moveLeft(self, board, idx):
        newBoard = board.copy()
        if ((idx % 3) != 0):
            newBoard[idx] = newBoard[idx - 1]
            newBoard[idx - 1] = '0'
            self.children.append(','.join(newBoard))

    def __moveRight(self, board, idx):
        newBoard = board.copy()
        if (((idx + 1) % 3) != 0):
            newBoard[idx] = newBoard[idx + 1]
            newBoard[idx + 1] = '0'
            self.children.append(','.join(newBoard))

    def __moveUp(self, board, idx):
        newBoard = board.copy()
        if (idx > self.boundUp):
            newBoard[idx] = newBoard[idx - 3]
            newBoard[idx - 3] = '0'
            self.children.append(','.join(newBoard))

    def __moveDown(self, board, idx):
        newBoard = board.copy()
        if (idx < self.boundDown):
            newBoard[idx] = newBoard[idx + 3]
            newBoard[idx + 3] = '0'
            self.children.append(','.join(newBoard))

    def getX(self, state):
        x = []
        stArr = state.split(',')
        for i in ['0','1','2','3','4','5','6','7','8']:
            idx = stArr.index(i)
            x.append(idx % 3)
        return x

    def getY(self, state):
        y = []
        stArr = state.split(',')
        for i in ['0','1','2','3','4','5','6','7','8']:
            idy = stArr.index(i)
            y.append(int(idy / 3))
        return y

if __name__ == '__main__':
    bfs = State()
    #path = bfs.getNeigbors("0,2,3,1,5,6,4,7,8")
    #for i in path:
      # print(i)
    x = bfs.getX("0,2,3,1,5,6,4,7,8")
    y = bfs.getY("0,2,3,1,5,6,4,7,8")
    for c in y:
        print(c)
