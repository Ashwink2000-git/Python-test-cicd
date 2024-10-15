# tests/test_hello.py
import io
import sys
from src.module1.hello import print_hello

def test_print_hello(capfd):
    print_hello()
    captured = capfd.readouterr()
    assert captured.out == "Hello, World!\n"
