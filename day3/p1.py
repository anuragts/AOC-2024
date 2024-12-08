import re

def read_input_file(file_name):
    a = []
    with open(file_name, "r") as file:
        for line in file:
            values = line.strip().split()
            a.append(values)
    return a


def main():
    max = 0
    text = read_input_file('input.txt')
    pattern = r"mul\((\d+),(\d+)\)"
    for line in text:
        matches = re.findall(pattern, ''.join(line))
        # print(''.join(line))
        for match in matches:
            max = max + (int(match[0]) * int(match[1]))
    print("max", max)

main()
