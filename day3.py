
# Day 3, Part 1

def get_total_priority_of_rucksacks(input_filename):
    total_priority = 0
    with open(input_filename) as f:
        lines = f.readlines()
        for line in lines:
            rucksack_contents = line.strip()
            total_priority += get_priority_for_rucksack(rucksack_contents)
    return total_priority


def get_priority_for_rucksack(contents: str):
    # split the string into two parts
    substr_len = len(contents)//2
    str1 = contents[:substr_len]
    str2 = contents[substr_len:]
    # get the priority of the shared char
    return get_char_priority(get_shared_char(str1, str2))


def get_char_priority(char: str):
    if char.islower():
        return ord(char) - 96
    else:
        return ord(char) - 64 + 26


def get_shared_char(str1: str, str2: str):
    return ''.join(set(str1).intersection(str2))


print('Total rucksack priority:', get_total_priority_of_rucksacks('./inputs/day3.txt'))


# Part 2

def get_shared_char2(str1: str, str2:str, str3:str):
    return ''.join(set(str1).intersection(str2).intersection(str3))


def get_total_priority_of_groups(input_filename):
    total_priority = 0
    with open(input_filename) as f:
        lines = f.readlines()
        lines_list = [line.strip() for line in lines]
        for group_index in range(len(lines_list)//3):
            group_lines = lines_list[group_index*3:group_index*3+3]
            shared_char = get_shared_char2(*group_lines)
            total_priority += get_char_priority(shared_char)
    return total_priority

print(get_total_priority_of_groups('./inputs/day3.txt'))