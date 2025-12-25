import pytest
from src04b import num_adj_rolls_at_loc, scan_map_adj_rolls, load_map_from_str_lines, process_file

def load_simple_map():
    return [
        [".", ".", "@"],
        [".", ".", "."],
        [".", ".", "."]
    ]

def load_simple_map_str():
    return [
        "..@",
        "...",
        "..."
    ]
def test_simple_map():
    simple_map = load_simple_map()
    assert 0==num_adj_rolls_at_loc(simple_map, (0,0))
    assert 1==num_adj_rolls_at_loc(simple_map, (0,1))
    assert 0==num_adj_rolls_at_loc(simple_map, (0,2))

    assert 0==num_adj_rolls_at_loc(simple_map, (1,0))
    assert 1==num_adj_rolls_at_loc(simple_map, (1,1))
    assert 1==num_adj_rolls_at_loc(simple_map, (1,2))

    assert 0==num_adj_rolls_at_loc(simple_map, (2,0))
    assert 0==num_adj_rolls_at_loc(simple_map, (2,1))
    assert 0==num_adj_rolls_at_loc(simple_map, (2,2))

def test_simple_map_scan():
    simple_map = load_simple_map()
    assert 1 == scan_map_adj_rolls(simple_map)

def test_load_simple_map():
     simple_map_str = load_simple_map_str()
     simple_map = load_simple_map()
     map = load_map_from_str_lines(simple_map_str)
     assert map == simple_map

def test_update_simple_map():
    simple_map_str = load_simple_map_str()
    map = load_map_from_str_lines(simple_map_str)
    assert map[0][2] == "@"
    map[0][2] = "X"
    assert map[0][2] == "X"

def test_process_file():
    map_lines = [
        "..@@.@@@@.",
        "@@@.@.@.@@",
        "@@@@@.@.@@",
        "@.@@@@..@.",
        "@@.@@@@.@@",
        ".@@@@@@@.@",
        ".@.@.@.@@@",
        "@.@@@.@@@@",
        ".@@@@@@@@.",
        "@.@.@@@.@.@"
    ]
    map = load_map_from_str_lines(map_lines)
    total_adj_rolls = scan_map_adj_rolls(map)
    assert total_adj_rolls == 43