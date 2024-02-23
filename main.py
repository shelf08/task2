# Создать новый двумерный массив, исключив из переданного двумерного массива строки и столбцы, состоящие из одинаковых элементов
# (т.е. строка, состоящая, предположим, из одних единиц, не должна попасть в новый двумерный массив).

def read_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        mas = [list(map(int, line.strip().split())) for line in lines]
    return mas

def process_matrix(mas):
    new_mas = []
    for row in mas:
        if len(set(row)) > 1:
            new_mas.append(row)

    t_mas = list(zip(*new_mas))
    f_mas = []
    for col in t_mas:
        if len(set(col)) > 1:
            f_mas.append(col)

    return list(zip(*f_mas))

def write_output(matrix, filename):
    with open(filename, 'w') as file:
        for row in matrix:
            file.write(' '.join(map(str, row)) + '\n')



in_mas = read_input('1.txt')
out_mas = process_matrix(in_mas)
write_output(out_mas, '2.txt')