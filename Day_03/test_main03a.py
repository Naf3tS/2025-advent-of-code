import pytest
from src03a import max_joltage

def test_max_joltage():
    assert max_joltage("123") == 23
    assert max_joltage("999") == 99

def test_max_joltage_edge_cast():
    assert max_joltage("989") == 99