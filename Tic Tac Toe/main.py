import math


class Game:
    """A class representing a Tic-Tac-Toe game with AI using the Minimax algorithm."""

    def __init__(self):
        """Initializes the game board as a 3x3 matrix and prints it."""
        self.matrix = [["   " for _ in range(3)] for _ in range(3)]
        self.print()

    def print(self):
        """Prints the current state of the game board."""
        for i in self.matrix:
            print("|".join(i))
            print("-" * 11)

    def check_winner(self, player):
        """Checks if the given player has won the game.

        Args:
            player (str): The player symbol (' X ' or ' O ').

        Returns:
            bool: True if the player has won, False otherwise.
        """
        matrix = len(self.matrix)

        # Check rows and columns
        for i in range(matrix):
            if (all(self.matrix[i][j].strip() == player.strip() for j in range(len(self.matrix[i]))) or
                    all(self.matrix[j][i].strip() == player.strip() for j in range(len(self.matrix[i])))):
                return True

        # Check diagonals
        if (all(self.matrix[i][i].strip() == player.strip() for i in range(matrix)) or
                all(self.matrix[i][matrix - 1 - i].strip() == player.strip() for i in range(matrix))):
            return True

        return False

    def is_full(self):
        """Checks if the game board is full (no empty spaces left)."""
        return all(self.matrix[i][j] != "   " for i in range(len(self.matrix)) for j in range(len(self.matrix)))

    def minimax(self, depth, maximizing):
        """Implements the Minimax algorithm to determine the best move for the AI.

        Args:
            depth (int): The current depth of the recursive tree.
            maximizing (bool): True if maximizing for AI (O), False if minimizing for player (X).

        Returns:
            int: The best score for the given game state.
        """
        if self.check_winner("X"):
            return depth - 10

        if self.check_winner("O"):
            return 10 - depth

        if self.is_full():
            return 0

        if maximizing:
            best_score = -math.inf

            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    if self.matrix[i][j] == "   ":
                        self.matrix[i][j] = " O "
                        score = self.minimax(depth=depth + 1, maximizing=False)
                        self.matrix[i][j] = "   "
                        best_score = max(score, best_score)

            return best_score
        else:
            best_score = math.inf

            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    if self.matrix[i][j] == "   ":
                        self.matrix[i][j] = " X "
                        score = self.minimax(depth=depth + 1, maximizing=True)
                        self.matrix[i][j] = "   "
                        best_score = min(score, best_score)

            return best_score

    def get_best_move(self):
        """Finds the best possible move for the AI using the Minimax algorithm.

        Returns:
            tuple: The row and column indices of the best move.
        """
        best_score = -math.inf
        best_move = None

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == "   ":
                    self.matrix[i][j] = " O "
                    score = self.minimax(0, False)
                    self.matrix[i][j] = "   "
                    
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)

        return best_move

    def get_player_move(self):
        """Prompts the player to input their move and validates the input.

        Returns:
            tuple: The row and column indices of the player's move.
        """
        while True:
            try:
                row, col = map(int, input("Enter row and column (0-2, separated by space): ").split())

                if self.matrix[row][col] == "   ":
                    return row, col
                else:
                    print("Cell is already occupied! Try again.")
            except (ValueError, IndexError):
                print("Invalid input! Enter row and column between 0 and 2.")


def play_game():
    """Runs the Tic-Tac-Toe game loop where the player and AI take turns playing.

    Returns:
        str: A message indicating the result of the game.
    """
    user = " X "
    computer = " O "
    board = Game()

    while True:
        # Player's move
        x, y = board.get_player_move()
        board.matrix[x][y] = user
        board.print()

        if board.check_winner(user):
            return "Congratulations! You win!"

        if board.is_full():
            return "It's a tie!"

        # AI's move
        print("Computer's turn...")
        x, y = board.get_best_move()
        board.matrix[x][y] = computer
        board.print()

        if board.check_winner(computer):
            return "Computer wins! Better luck next time."

        if board.is_full():
            return "It's a tie!"


if __name__ == "__main__":
    print(play_game())
