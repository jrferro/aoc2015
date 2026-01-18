import day3

def test_houses_solo_examples():
    examples = [(">", 2),
                ("^>v<", 4),
                ("^v^v^v^v^v", 2)]
    for (s, f) in examples:
        assert day3.houses_solo(s) == f

def test_houses_robot_examples():
    examples = [("^v", 3),
                ("^>v<", 3),
                ("^v^v^v^v^v", 11)]
    for (s, f) in examples:
        assert day3.houses_robot(s) == f
