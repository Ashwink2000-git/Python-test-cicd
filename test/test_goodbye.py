# tests/test_goodbye.py
from src.module2.goodbye import print_goodbye

def test_print_goodbye(capfd):
    print_goodbye()
    captured = capfd.readouterr()
    assert captured.out == "Goodbye, World!\n"
