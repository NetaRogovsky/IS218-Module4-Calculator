from unittest.mock import patch
from app.calculator import Calculator


def test_get_number_valid():
    with patch("builtins.input", return_value="42"):
        assert Calculator().get_number("Enter: ") == 42.0


def test_get_number_invalid_then_valid():
    with patch("builtins.input", side_effect=["abc", "5"]):
        with patch("builtins.print"):
            assert Calculator().get_number("Enter: ") == 5.0


def test_run_exit():
    with patch("builtins.input", side_effect=["exit"]):
        with patch("builtins.print"):
            Calculator().run()


def test_run_help_then_exit():
    with patch("builtins.input", side_effect=["help", "exit"]):
        with patch("builtins.print"):
            Calculator().run()


def test_run_history_empty_then_exit():
    with patch("builtins.input", side_effect=["history", "exit"]):
        with patch("builtins.print"):
            Calculator().run()


def test_run_unknown_command_then_exit():
    with patch("builtins.input", side_effect=["banana", "exit"]):
        with patch("builtins.print"):
            Calculator().run()


def test_run_calculation_then_history_then_exit():
    inputs = ["add", "3", "4", "history", "exit"]
    with patch("builtins.input", side_effect=inputs):
        with patch("builtins.print"):
            Calculator().run()


def test_run_divide_by_zero_then_exit():
    with patch("builtins.input", side_effect=["divide", "5", "0", "exit"]):
        with patch("builtins.print"):
            Calculator().run()