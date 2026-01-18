import day2

def test_paper_needed_examples():
    examples = [("2x3x4", 58),
                ("1x1x10", 43)]
    for (s, f) in examples:
        assert day2.paper_needed(s) == f

def test_ribbon_needed_examples():
    examples = [("2x3x4", 34),
                ("1x1x10", 14)]
    for (s, f) in examples:
        assert day2.ribbon_needed(s) == f
