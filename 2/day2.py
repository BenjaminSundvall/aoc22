#=====================================================================#
# Read input file                                                     #
#=====================================================================#

file = open("input2.txt", "r")
input_lines = file.readlines()


#=====================================================================#
# Solution for part 1                                                 #
#=====================================================================#

def part1():
    MY_WIN = 2
    DRAW = 0
    ELF_WIN = 1

    score = 0

    for line in input_lines:
        elf_choice = choice_to_number(line.split()[0])
        my_choice = choice_to_number(line.split()[1])

        # 1 - 2 = -1,     2 - 3 = -1,     3 - 1 = 2
        # 1 - 1 = 0,      2 - 2 = 0,      3 - 3 = 0
        # 2 - 1 = 1,      3 - 2 = 1,      1 - 3 = -2
        result = (elf_choice - my_choice) % 3

        if result == MY_WIN:
            score += my_choice + 6
        elif result == DRAW:
            score += my_choice + 3
        elif result == ELF_WIN:
            score += my_choice

    return score


def choice_to_number(choice):
    if choice == "A" or choice == "X":
        return 1
    elif choice == "B" or choice == "Y":
        return 2
    elif choice == "C" or choice == "Z":
        return 3

#=====================================================================#
# Solution for part 2                                                 #
#=====================================================================#

def part2():
    LOSE = "X"
    DRAW = "Y"
    WIN = "Z"

    score = 0

    for line in input_lines:
        elf_choice = choice_to_number(line.split()[0])
        desired_outcome = line.split()[1]

        if desired_outcome == LOSE:
            my_choice = elf_choice - 1
            if my_choice == 0:      # Quick fix
                my_choice = 3
            score += my_choice
        elif desired_outcome == DRAW:
            my_choice = elf_choice
            score += my_choice + 3
        elif desired_outcome == WIN:
            my_choice = elf_choice + 1
            if my_choice == 4:      # Quick fix
                my_choice = 1
            score += my_choice + 6

    return score


#=====================================================================#
# Print solutions                                                     #
#=====================================================================#

print("Answer to part 1:")
print(part1())

print("Answer to part 2:")
print(part2())
