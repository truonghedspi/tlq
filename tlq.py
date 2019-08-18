import itertools
import copy

row = 10
col = 4
max_elm_equal = 3

combines = list(itertools.combinations(list(range(2, row + 1)), col - 1))

matrix = [[0 for x in range(col)] for y in range(row)]
result = []

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

        for row in range(1, num_rows):
                update_matrix(matrix, combine, row, 1)


def update_matrix(matrix, combine, row, col):
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        if row == num_rows-1 and col == num_cols:
                result.append(copy.deepcopy(matrix))

        if col == num_cols:
                return
        selectables = set(range(1, num_rows+1))
        selected_in_cols = set([row[col] for row in matrix[0:row]])
        selected_in_rows = set(matrix[row][0:col])
        selectables = selectables - (selected_in_cols | selected_in_rows)

        for selectable in sorted(selectables, reverse=True):
                selected_in_rows.add(selectable)
                valid = True
                for selected_row in matrix[0:row]:
                        intersection = selected_in_rows & set(selected_row)
                        if len(intersection) > max_elm_equal:
                                valid = False
                                break
                                     
                selected_in_rows.discard(selectable)                
                if valid:
                        matrix[row][col] = selectable
                else:
                        matrix[row][col] = 0
                update_matrix(matrix, combine, row, col + 1)

for c in combines:
        fill_matrix(matrix, c)

print('\n'.join('{}: {}'.format(*k) for k in enumerate(result)))




