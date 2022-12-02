import day1


def test_parse_elf_loads():
    actual = day1.parse_elf_loads('./test_inputs/day1.txt')
    expected = [6000, 4000, 11000, 24000, 10000]
    assert actual == expected

def test_get_top_three_values():
    test_list = [5, 1, 3, 2, 4]
    actual = day1.get_top_three_values(test_list)
    assert actual == [5, 4, 3]