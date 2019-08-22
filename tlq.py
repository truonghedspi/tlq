import itertools
import copy

row = 80
col = 5
max_elm_equal = 1

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
    num_cols = len(matrix[0])
    update_matrix(matrix, combine, num_cols+1)


def update_matrix(matrix, combine, position):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    row = position // num_cols
    col = position % num_cols

    if col == 0:
        update_matrix(matrix, combine, position + 1)
        return

    if position > num_cols*num_rows - 1:
        return
    selectables = set(range(1, num_rows+1))
    selected_in_cols = set([rows[col] for rows in matrix[0:row]])
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

        if valid:
            matrix[row][col] = selectable
            if position == num_cols*num_rows - 1:
                print(matrix)
                result.append(copy.deepcopy(matrix))
            update_matrix(matrix, combine, position + 1)
            matrix[row][col] = 0
        selected_in_rows.discard(selectable)


for c in combines:
    fill_matrix(matrix, combines[0])

# print('\n'.join('{}: {}'.format(*k) for k in enumerate(result)))
