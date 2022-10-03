import unittest
from unittest.mock import patch
import tic_tac_toe


class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.tic_tac_toe_game = tic_tac_toe.TicTacToe()

    @patch('tic_tac_toe.get_input', return_value='1 1')
    def test_input(self, input):
        self.assertEqual(tic_tac_toe.validate_input(), (1, 1))

    def test_player_swapping(self):
        self.assertEqual(tic_tac_toe.swap_player_turn('X'), 'O')
        self.assertEqual(tic_tac_toe.swap_player_turn('O'), 'X')

    def test_get_random(self):
        self.assertGreaterEqual(tic_tac_toe.get_random_first_player(), 0)
        self.assertLessEqual(tic_tac_toe.get_random_first_player(), 1)

    def test_board_creating(self):
        self.assertEqual(self.tic_tac_toe_game.create_board(), None)

    def test_putting(self):
        self.tic_tac_toe_game.create_board()
        self.assertEqual(self.tic_tac_toe_game.fix_spot(1, 1, 'X'), True)
        self.assertEqual(self.tic_tac_toe_game.fix_spot(1, 2, 'X'), True)
        self.assertEqual(self.tic_tac_toe_game.fix_spot(1, 1, 'X'), False)

    def test_winning_main_diag(self):
        self.tic_tac_toe_game.create_board()
        self.tic_tac_toe_game.board[0][0] = 'X'
        self.tic_tac_toe_game.board[1][1] = 'X'
        self.tic_tac_toe_game.board[2][2] = 'X'
        self.assertEqual(self.tic_tac_toe_game.check_main_diag('X'), True)
        self.assertEqual(self.tic_tac_toe_game.check_main_diag('O'), False)
        self.assertEqual(self.tic_tac_toe_game.is_player_win('X'), True)
        self.assertEqual(self.tic_tac_toe_game.is_player_win('O'), False)

    def test_winning_another_diag(self):
        self.tic_tac_toe_game.create_board()
        self.tic_tac_toe_game.board[0][2] = 'O'
        self.tic_tac_toe_game.board[1][1] = 'O'
        self.tic_tac_toe_game.board[2][0] = 'O'
        self.assertEqual(self.tic_tac_toe_game.check_another_diag('O'), True)
        self.assertEqual(self.tic_tac_toe_game.check_another_diag('X'), False)
        self.assertEqual(self.tic_tac_toe_game.is_player_win('O'), True)
        self.assertEqual(self.tic_tac_toe_game.is_player_win('X'), False)

    def test_winning_row(self):
        self.tic_tac_toe_game.create_board()
        self.tic_tac_toe_game.board[1][0] = 'O'
        self.tic_tac_toe_game.board[1][1] = 'O'
        self.tic_tac_toe_game.board[1][2] = 'O'
        self.assertEqual(self.tic_tac_toe_game.check_rows('O'), True)
        self.assertEqual(self.tic_tac_toe_game.check_rows('X'), False)
        self.assertEqual(self.tic_tac_toe_game.is_player_win('O'), True)
        self.assertEqual(self.tic_tac_toe_game.is_player_win('X'), False)

    def test_winning_col(self):
        self.tic_tac_toe_game.create_board()
        self.tic_tac_toe_game.board[0][1] = 'X'
        self.tic_tac_toe_game.board[1][1] = 'X'
        self.tic_tac_toe_game.board[2][1] = 'X'
        self.assertEqual(self.tic_tac_toe_game.check_columns('X'), True)
        self.assertEqual(self.tic_tac_toe_game.check_columns('O'), False)
        self.assertEqual(self.tic_tac_toe_game.is_player_win('X'), True)
        self.assertEqual(self.tic_tac_toe_game.is_player_win('O'), False)

    def test_not_winning(self):
        self.tic_tac_toe_game.create_board()
        self.tic_tac_toe_game.board[0][1] = 'X'
        self.assertEqual(self.tic_tac_toe_game.is_player_win('X'), False)
        self.assertEqual(self.tic_tac_toe_game.is_player_win('O'), False)

    def test_fullness(self):
        self.tic_tac_toe_game.create_board()
        self.tic_tac_toe_game.board[0][1] = 'X'
        self.assertEqual(self.tic_tac_toe_game.is_board_filled(), False)
        self.tic_tac_toe_game.board[1][1] = 'X'
        self.tic_tac_toe_game.board[2][1] = 'O'
        self.tic_tac_toe_game.board[2][2] = 'X'
        self.tic_tac_toe_game.board[2][0] = 'O'
        self.tic_tac_toe_game.board[0][2] = 'X'
        self.tic_tac_toe_game.board[0][0] = 'O'
        self.tic_tac_toe_game.board[1][0] = 'O'
        self.tic_tac_toe_game.board[1][2] = 'X'
        self.assertEqual(self.tic_tac_toe_game.is_board_filled(), True)


if __name__ == '__main__':
    unittest.main()
