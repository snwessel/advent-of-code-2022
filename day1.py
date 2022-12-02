# Goal: parse the calories carried by various elves

# Return a list of numbers representing the load carried by each elf
def parse_elf_loads(input_filename):
    all_elf_loads = []
    current_elf_load = 0
    with open(input_filename) as f:
        lines = f.readlines()
        for line in lines:
            # if this is an empty line, move to the next elf
            if line.strip() == "":
                all_elf_loads.append(current_elf_load)
                current_elf_load = 0
            # otherwise add to the current elf's load
            else:
                current_elf_load += int(line.strip())
        # check that the last value was saved
        if all_elf_loads[-1] != current_elf_load:
            all_elf_loads.append(current_elf_load)
    return all_elf_loads


def get_top_three_values(value_list):
    # sort the list and then get the last 3 values
    return sorted(value_list, reverse=True)[:3]


elf_loads = parse_elf_loads('./inputs/day1.txt')
top_3_loads = get_top_three_values(elf_loads)

print("Max elf load:", max(elf_loads))
print("Sum of top 3:", sum(top_3_loads))
