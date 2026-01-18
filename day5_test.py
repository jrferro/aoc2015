import day5

def test_nice_1_examples():
    examples = [("ugknbfddgicrmopn", True),
                ("aaa", True),
                ("jchzalrnumimnmhp", False),
                ("haegwjzuvuyypxyu", False),
                ("dvszwmarrgswjxmb", False)]
    for (s, f) in examples:
        assert day5.is_nice_1(s) == f

def test_nice_2_examples():
    examples = [("qjhvhtzxzqqjkmpb", True),
                ("xxyxx", True),
                ("uurcxstgmygtbstg", False),
                ("ieodomkazucvgmuy", False)]
    for (s, f) in examples:
        assert day5.is_nice_2(s) == f
