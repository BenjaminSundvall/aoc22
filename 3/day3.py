#=====================================================================#
# Read input file                                                     #
#=====================================================================#

file = open("input3.txt", "r")
input_lines = file.readlines()


#=====================================================================#
# Solution for part 1                                                 #
#=====================================================================#

def part1():
    score = 0

    for line in input_lines:
        length = len(line)
        first_part = line[:int(length/2)]
        second_part = line[int(length/2):]
        
        for c1 in first_part:
            for c2 in second_part:
                if c1 == c2:
                    if c1.isupper():
                        value = ord(c1) - ord("A") + 27
                    elif c1.islower():
                        value = ord(c1) - ord("a") + 1

        score += value

    return score


#=====================================================================#
# Solution for part 2                                                 #
#=====================================================================#

def part2():
    file.seek(0)
    
    score = 0

    while True:
        lines = [0, 0, 0]
        for i in range(3):
            lines[i] = file.readline()
            if not lines[i]:
                return score
    
        for c1 in lines[0]:
            for c2 in lines[1]:
                for c3 in lines[2]:
                    if c1 == c2 == c3:
                        if c1.isupper():
                            value = ord(c1) - ord("A") + 27
                        elif c1.islower():
                            value = ord(c1) - ord("a") + 1
        score += value
                        


#=====================================================================#
# Print solutions                                                     #
#=====================================================================#

print("Answer to part 1:")
print(part1())

print("Answer to part 2:")
print(part2())
