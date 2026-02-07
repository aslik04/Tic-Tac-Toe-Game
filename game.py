import random

class Game:
    def __init__(self, difficulty, current):
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.current = current
        self.game_over = False
        self.winner = None
        self.moves = 0
        if difficulty == "human":
            self.bot = None
        else:
            self.bot = Bot(difficulty, 1)
    
    def move(self, row, col):
        if row < 0 or row > 2 or col < 0 or col > 2 or self.board[row][col] != None:
            return False
        
        self.board[row][col] = self.current
        self.moves += 1

        if all(x == self.current for x in self.board[row]):
            self.winner = self.current
            self.game_over = True
        elif all(r[col] == self.current for r in self.board):
            self.winner = self.current
            self.game_over = True
        elif all(self.board[i][i] == self.current for i in range(3)):
            self.winner = self.current
            self.game_over = True
        elif all(self.board[2 - i][i] == self.current for i in range(3)):
            self.winner = self.current
            self.game_over = True
        elif self.moves == 9:
            self.game_over = True
        else:
            self.current = 1 if self.current == 0 else 0

        return True

    def play(self):

        while not self.game_over:
            if self.bot and self.current == self.bot.player:
                r, c = self.bot.move(self.board)
                self.move(r, c)
                continue

            print("Player ", self.current, " Please make your move")
            self.display_board()
            try:
                row = int(input("Enter Row: "))
                col = int(input("Enter Col: "))
                if not self.move(row, col):
                    print("Invalid move, please try again")
                    continue
            except ValueError:
                print("Please enter integers only")
                continue
        
        if self.winner == None:
            print("No moves remaining, game is a draw!")
        elif self.winner == 0:
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")

    def display_board(self):
        sym = {None: ".", 0: "X", 1: "O"}
        for i, row in enumerate(self.board):
            print(" | ".join(sym[cell] for cell in row))
            if i < 2:
                print("--+---+--")

class Bot:
    def __init__(self, difficulty, player):
        self.difficulty = difficulty
        self.player = player

    def move(self, board):
        valid_states = [(r, c) for r in range(3) for c in range(3) if board[r][c] is None]

        if self.difficulty == 1:
            state = valid_states[random.randint(0, len(valid_states) - 1)]
            return state
        elif self.difficulty == 2:
            if self.can_win(valid_states, board, self.player) is not None:

                return self.can_win(valid_states, board, self.player)
            elif self.can_win(valid_states, board, 1 - self.player) is not None:

                return self.can_win(valid_states, board, 1 - self.player)
            elif (1, 1) in valid_states:
                return (1, 1)
            
            corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
            sides = [(0, 1), (1, 0), (1, 2), (2, 1)]

            print(valid_states)

            valid_corners = [x for x in valid_states if x in corners]

            if valid_corners:
                state = valid_corners[random.randint(0, len(valid_corners) - 1)]
                return state
            else:
                state = valid_states[random.randint(0, len(valid_states) - 1)]
                return state
        else:
            bot = Minimax()
            return bot.best_move(board)
            
    def can_win(self, valid_states, board, player):
        
        for r, c in valid_states:
            board[r][c] = player

            won = (
                all(board[r][j] == player for j in range(3)) or
                all(board[i][c] == player for i in range(3)) or 
                all(board[i][i] == player for i in range(3)) or
                all(board[i][2 - i] == player for i in range(3))
            )

            board[r][c] = None

            if won:
                return (r, c)

        return None
    
class Minimax:
    def __init__(self):
        self.bot = 1
        self.human = 0
        self.win_score = 1
        self.draw_score = 0
        self.lose_score = -1

    def best_move(self, board):
        valid_states = [(r, c) for r in range(3) for c in range(3) if board[r][c] is None]
        max_score = float("-inf")
        best_r, best_c = -1, -1

        for r, c in valid_states:
            board[r][c] = 1
            score = self.minimax(board, 0)
            board[r][c] = None
            
            if score == 1:
                max_score = score
                best_r, best_c = r, c
                break 
            elif score > max_score:
                max_score = score
                best_r, best_c = r, c
        
        return (best_r, best_c)


    def minimax(self, board, current_player):
        valid_states = [(r, c) for r in range(3) for c in range(3) if board[r][c] is None]
        
        if self.has_win(board, 0):
            return -1
        elif self.has_win(board, 1):
            return 1
        elif not valid_states:
            return 0
        elif current_player == 1:
            max_score = float("-inf")

            for r, c in valid_states:
                board[r][c] = current_player
                score = self.minimax(board, 1 - current_player)
                board[r][c] = None
                
                if score == 1:
                    max_score = score
                    break 
                elif score > max_score:
                    max_score = score
            
            return max_score
        else:
            min_score = float("inf")

            for r, c in valid_states:
                board[r][c] = current_player
                score = self.minimax(board, 1 - current_player)
                board[r][c] = None
                
                if score == -1:
                    min_score = score
                    break 
                elif score < min_score:
                    min_score = score
            
            return min_score
        
    def has_win(self, board, player):
        # rows
        for r in range(3):
            if all(board[r][c] == player for c in range(3)):
                return True

        # cols
        for c in range(3):
            if all(board[r][c] == player for r in range(3)):
                return True

        # diagonals
        if all(board[i][i] == player for i in range(3)):
            return True
        if all(board[i][2 - i] == player for i in range(3)):
            return True

        return False


if __name__ == "__main__":
    inp = "Y"
    start = 1
    score = {"Player" : 0, "Bot": 0, "Draw": 0}

    while inp == "Y":
        if input("Would you like to play a bot: ") == "Y":
            difficulty = input("What level bot would you like to play: ")
            start = 1 - start
            game = Game(int(difficulty), start)
        else:
            start = 1 - start
            game = Game("human", start)

        game.play()
        if game.winner is None:
            score["Draw"] += 1
        elif game.winner == 0:
            score["Player"] += 1
        else:
            score["Bot"] += 1
        
        inp = input("Would you like to play again: type Y ")
    print(score)