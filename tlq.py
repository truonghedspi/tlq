import itertools
from copy import copy, deepcopy

row = 10
col = 4
max_elm_equal = 2

combines = list(itertools.combinations(list(range(2, row + 1)), col - 1))

matrix = [[0 for x in range(col)] for y in range(row)]

def init_matrix(m):
    i = 0
    while i < row:
        m[i][0] = i + 1
        i = i + 1

def update_first_row(matrix, combine):
    i = 1
    for x in combine:
        matrix[0][i] = x
        i = i + 1

def fill_matrix(matrix, combine):
        init_matrix(matrix)
        update_first_row(matrix, combine)
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        for row in range(1, num_rows):
                for col in range(1, num_cols):
                        selectables = set(range(1, num_rows+1))
                        selected_in_cols = set([row[col] for row in matrix[0:row]])
                        selected_in_rows = set(matrix[row][0:col])
                        selectables = selectables - (selected_in_cols | selected_in_rows)

                        value = 0
                        for selectable in selectables:
                                selected_in_rows.add(selectable)
                                valid = True
                                for selected_row in range(0, row):
                                        intersection = selected_in_rows & set(matrix[selected_row])
                                        if len(intersection) > max_elm_equal:
                                                valid = False
                                                break
                                if valid:
                                        value = selectable
                                        break
                                selected_in_rows.discard(selectable)
                        if value == 0:
                                return
                        matrix[row][col] = value

def update_matrix(matrix, row, col):
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        if num_rows == row or num_cols == col:
                return
        selectables = set(range(1, num_rows+1))
                        selected_in_cols = set([row[col] for row in matrix[0:row]])
                        selected_in_rows = set(matrix[row][0:col])
                        selectables = selectables - (selected_in_cols | selected_in_rows)

                        value = 0
                        for selectable in selectables:
                                selected_in_rows.add(selectable)
                                valid = True
                                for selected_row in range(0, row):
                                        intersection = selected_in_rows & set(matrix[selected_row])
                                        if len(intersection) > max_elm_equal:
                                                valid = False
                                                break
                                if valid:
                                        value = selectable
                                        break
                                selected_in_rows.discard(selectable)
                        if value == 0:
                                return
                        matrix[row][col] = value
fill_matrix(matrix, combines[0])
print(matrix)




