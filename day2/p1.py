def read_input_file(file_name):
    a = []
    with open(file_name, "r") as file:
        for line in file:
            values = line.strip().split()
            a.append(values)
    return a

def remove_common_items(list_one, list_two):
    flat_one = set(tuple(sorted(sublist)) for sublist in list_one)
    flat_two = set(tuple(sorted(sublist)) for sublist in list_two)
    
    unique_to_one = flat_one - flat_two
    unique_to_two = flat_two - flat_one
    
    unique_items = list(unique_to_one.union(unique_to_two))
    
    return [list(item) for item in unique_items]

def main():
    min_gap = 1
    max_gap = 3
    unsafe_levels = []
    a = read_input_file('inputs/input2.txt')

    for i in a:
        for j in range(len(i)):
            # print(i[j])
            if j+1 < len(i):
                if abs(int(i[j]) - int(i[j+1])) > max_gap or abs(int(i[j]) - int(i[j+1])) < min_gap:
                    unsafe_levels.append(i)
                elif (int(i[0]) - int(i[1])) > 0:
                    if int(i[j]) - int(i[j+1]) < 0:
                        unsafe_levels.append(i)

                elif (int(i[0]) - int(i[1])) < 0:
                    if int(i[j]) - int(i[j+1]) > 0:
                        unsafe_levels.append(i)
    safe_levels = remove_common_items(unsafe_levels, a)
    print(len(safe_levels))
            

main()
