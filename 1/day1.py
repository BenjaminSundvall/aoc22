file = open("input1.txt", "r")
input_lines = file.readlines()

def part1():
    greatest_sum = 0
    total_sum = 0

    for line in input_lines:
        if line == "\n":
            total_sum = 0
        else:
            total_sum += int(line)
            if total_sum > greatest_sum:
                greatest_sum = total_sum

    return greatest_sum


def part2():
    top_three_sums = [0, 0, 0]
    total_sum = 0

    for line in input_lines:
        if line == "\n":
            total_sum = 0
        else:
            total_sum += int(line)
            for i in range(3):
                if total_sum > top_three_sums[i]:
                    top_three_sums[i] = total_sum
                    break

    return sum(top_three_sums)


print("Answer to part 1:")
print(part1())

print("Answer to part 2:")
print(part2())
