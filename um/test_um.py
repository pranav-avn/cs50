import pytest
from um import count

def main():
    test_1()



def test_1():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, hello, um, world") == 2
    assert count("Hello, um, world") == 1
    assert count("yummy") == 0
