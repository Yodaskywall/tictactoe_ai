class Board:
    def __init__(self):
        self.player = 1
        self.board = [[0,0,0],[0,0,0],[0,0,0]]
        self.winner = None

    def move(self, pos):
        print("moving")
        self.board[pos[0]][pos[1]] = self.player
        self.player *= -1
        self.check_winner()

    def check_winner(self):
        for row in range(3):
            if self.board[row][0] != 0 and self.board[row][0] == self.board[row][1] == self.board[row][2]:
                self.winner = self.board[row][0]
                return True

            if self.board[0][row] != 0 and self.board[0][row] == self.board[1][row] == self.board[2][row]:
                self.winner = self.board[0][row]
                return True

        if self.board[1][1] != 0 and self.board[1][1] == self.board[0][0] == self.board[2][2]:
            self.winner = self.board[0][0]
            return True

        if self.board[0][2] != 0 and self.board[0][2] == self.board[1][1] == self.board[2][0]:
            self.winner = self.board[0][2]
            return True

        complete = True
        for r in range(3):
            for c in range(3):
                if self.board[r][c] == 0:
                    complete = False


        if complete:
            self.winner = 0
            return True

        print("didn't win hahahh")
        return False

