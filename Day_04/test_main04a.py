import pytest
from src04a import num_adj_rolls_at_loc, scan_map_adj_rolls

simple_map = [
    "..@",
    "...",
    "..."
]

def test_simple_map():
    assert 0==num_adj_rolls_at_loc(simple_map, (0,0))
    assert 0==num_adj_rolls_at_loc(simple_map, (0,1))
    assert 0==num_adj_rolls_at_loc(simple_map, (0,2))

    assert 1==num_adj_rolls_at_loc(simple_map, (1,0))
    assert 1==num_adj_rolls_at_loc(simple_map, (1,1))
    assert 0==num_adj_rolls_at_loc(simple_map, (1,2))

    assert 0==num_adj_rolls_at_loc(simple_map, (2,0))
    assert 1==num_adj_rolls_at_loc(simple_map, (2,1))
    assert 0==num_adj_rolls_at_loc(simple_map, (2,2))

def test_simple_map_scan():
    assert 1 == scan_map_adj_rolls(simple_map)