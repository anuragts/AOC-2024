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


def similarity(a, b):
    s_score  = 0
    appearance = 0
    for i in range(len(b)):
            if a == b[i]:
                appearance += 1
    s_score = a * appearance
    return s_score

def main():
    a, b = read_input_file('input4.txt')
    sum = 0
    for i in range(len(a)):
        sum += similarity(a[i], b)
    print(sum)
main()