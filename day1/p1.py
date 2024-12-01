def find_min_diff(a, b):
    sorted_a = sorted(a)
    sorted_b = sorted(b)
    d = 0
    for i in range(len(sorted_a)):
        d += abs(sorted_a[i] - sorted_b[i])
    return d


def read_input_file(file_name):
    a = []
    b = []
    with open(file_name, "r") as file:
        for line in file:
            values = line.strip().split()
            if len(values) == 2:
                a.append(int(values[0]))
                b.append(int(values[1]))
    return a, b

def main():
    d = 0
    a, b = read_input_file('input2.txt')
    print(find_min_diff(a, b))

main()