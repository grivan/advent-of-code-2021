INPUT = "day4/day4.in"

class Board():
    
    marked = None
    board = None
    
    def __init__(self, board_lines):
        self.marked = [[0 for i in range(5)] for j in range(5)]
        self.board = []
        
        for line in board_lines:
            self.board.append([int(num) for num in line.rstrip().split()])
    
    def update(self, number):
        # updates the marked items on the board
        # returns True (bingo!) if the board is now winning!
        for row, line in enumerate(self.board):
            try:
                col = line.index(number)
                self.marked[row][col] = 1
                return self.check(row, col)
            except ValueError:
                continue
    
    def check(self, row, col):
        # check the row 'row'
        if all(self.marked[row]): 
            return True
        
        # check column 'col'
        if all([mark[col] for mark in self.marked]): 
            return True
        
        return False
        
    def printb(self):
        for line in self.board:
            print(line)
        for line in self.marked:
            print(line)
            
    def win_sum(self):
        total = 0
        for row, line in enumerate(self.board):
            for col, num in enumerate(line):
                if not self.marked[row][col]:
                    total += num
        return total
        

with open(INPUT) as input_file:
    numbers = [int(x) for x in input_file.readline().rstrip().split(',')]
    
    boards = []
    
    while(True):
        
        # read empty line
        iline = input_file.readline()
        if len(iline) == 0:
            break
        
        board_lines = []
        for i in range(5):
            line = input_file.readline().rstrip()
            board_lines.append(line)
        boards.append(Board(board_lines))
        
    # PART 1
    winning_board = None
    win_num = None
    for num in numbers:
        for board in boards:
            if board.update(num):
                winning_board = board
                win_num = num
                break
        if winning_board:
            break
    
    print(winning_board.win_sum() * win_num)
    
    # PART 2
    board_wins = [(board, False) for board in boards]
    last_win = None
    win_num = None
    for num in numbers:
        for index, (board, won) in enumerate(board_wins):
            if not won and board.update(num):
                last_win = board
                win_num = num
                board_wins[index] = (board, True)
    
    print(last_win.win_sum() * win_num)