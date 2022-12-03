import day3



def test_get_char_priority():
    assert day3.get_char_priority('a') == 1
    assert day3.get_char_priority('z') == 26
    assert day3.get_char_priority('A') == 27
    assert day3.get_char_priority('Z') == 52

def test_get_shared_char():
    assert day3.get_shared_char('vJrwpWtwJgWr', 'hcsFMMfFFhFp') == 'p'

def test_get_priority_for_rucksack():
    assert day3.get_priority_for_rucksack('vJrwpWtwJgWrhcsFMMfFFhFp') == 16
    assert day3.get_priority_for_rucksack('jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL') == 38

def test_get_shared_char2():
    assert day3.get_shared_char2('vJrwpWtwJgWrhcsFMMfFFhFp', 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'PmmdzqPrVvPwwTWBwg')