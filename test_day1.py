import day1

def test_find_floor_examples():
    examples = [("(())", 0),
                ("()()", 0),
                ("(((", 3),
                ("(()(()(", 3),
                ("))(((((", 3),
                ("())", -1),
                ("))(", -1),
                (")))", -3),
                (")())())", -3)]
    for (s, f) in examples:
        assert day1.find_floor(s) == f

def test_find_basement_examples():
    examples = [(")", 1),
                ("()())", 5)]
    for (s, f) in examples:
        assert day1.find_basement(s) == f
