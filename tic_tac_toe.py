"""
This module is representing a simple TicTacToe game
"""
import random


def get_input(text):
    """
    function for tests patching
    :param text: user's input
    :return: a string
    """
    return input(text)


def validate_input() -> (int, int):
    """
    function for checking input
    :return: user input
    """
    user_input = get_input("Enter row and column numbers to fix spot: ")
    print()
    while True:
        try:
            if len(user_input.split()) != 2:
                print("Please give two coordinates")
                user_input = get_input("Try again: ")
                continue

            nums_range = True

            for coordinate in user_input.split():

                if int(coordinate) < 1 or int(coordinate) > 3:
                    nums_range = False
                    print("Coordinates should be in range from 1 to 3")
                    break

            if nums_range:
                return int(user_input.split()[0]), int(user_input.split()[1])

        except ValueError:
            print('You need to type numbers from 1 to 3')

        user_input = get_input("Try again: ")


def get_random_first_player():
    """
    function for choosing starting player
    :return: 0 or 1
    """
    return random.randint(0, 1)


def swap_player_turn(player):
    """
    function for changing turn
    :param player: current player
    :return: another player
    """
    return 'X' if player == 'O' else 'O'


class TicTacToe:
    """
    This class is using for TicTacToe game
    """

    def __init__(self):
        self.board = []
        self.is_win = False

    def create_board(self) -> None:
        """
        function for creating a board
        :return: terminal image of a board
        """
        for _ in range(3):
            row = []
            for _ in range(3):
                row.append('-')
            self.board.append(row)

    def fix_spot(self, row, col, player) -> bool:
        """
        checking place for emptiness
        :param row: player's row
        :param col: player's column
        :param player: current player
        :return: bool that means emptiness of a place
        """
        if self.board[row][col] == '-':
            self.board[row][col] = player
            return True
        print("This place is already marked, choose another coordinates")
        return False

    def check_rows(self, player: str) -> bool:
        """
        function for checking 3 in a row
        :param player: X or O
        :return: win or not
        """
        for i in range(len(self.board)):
            self.is_win = True
            for j in range(len(self.board)):
                if self.board[i][j] != player:
                    self.is_win = False
                    break
            if self.is_win:
                return self.is_win
        return False

    def check_columns(self, player: str) -> bool:
        """
        function for checking 3 in a column
        :param player: X or O
        :return: win or not
        """
        for i in range(len(self.board)):
            self.is_win = True
            for j in range(len(self.board)):
                if self.board[j][i] != player:
                    self.is_win = False
                    break
            if self.is_win:
                return self.is_win
        return False

    def check_main_diag(self, player: str) -> bool:
        """
        function for checking 3 in a main diagonal
        :param player: X or O
        :return: win or not
        """
        self.is_win = True
        for i in range(len(self.board)):
            if self.board[i][i] != player:
                self.is_win = False
                break
        return self.is_win

    def check_another_diag(self, player: str) -> bool:
        """
        function for checking 3 in a another diagonal
        :param player: X or O
        :return: win or not
         """
        self.is_win = True
        for i in range(len(self.board)):
            if self.board[i][len(self.board) - 1 - i] != player:
                self.is_win = False
                break
        return self.is_win

    def is_player_win(self, player: str) -> bool:
        """
        function for checking if someone won
        :param player: which of the two player's turn
        :return: bool
        """
        return self.check_rows(player) or self.check_columns(player) or \
                self.check_main_diag(player) or self.check_another_diag(player)

    def is_board_filled(self) -> bool:
        """
        function for checking is board filled
        :return: bool
        """
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def show_board(self) -> None:
        """
        function for printing a board
        :return:
        """
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def start(self) -> None:
        """
        function for starting a Tic-Tac-Toe game
        :return: None
        """
        self.create_board()

        player = 'X' if get_random_first_player() == 1 else 'O'
        while True:
            print(f"Player {player} turn")

            self.show_board()
            spot_marked = False
            while not spot_marked:
                row, col = validate_input()
                spot_marked = self.fix_spot(row - 1, col - 1, player)

            if self.is_player_win(player):
                print(f"Player {player} has won!")
                break

            if self.is_board_filled():
                print("Match Draw!")
                break

            player = swap_player_turn(player)

        print()
        self.show_board()


if __name__ == '__main__':
    TIC_TAC = TicTacToe()
    TIC_TAC.start()
