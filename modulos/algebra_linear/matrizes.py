



A = [[1, 2, 3]      # A possui duas linhas e três colunas
     [4, 5, 6]]


B = [[1, 2]         # B possui três linhas e duas colunas
     [3, 4]
     [5, 6]]


data = [[70, 170, 40],
        [65, 120, 26],
        [77, 250, 19]]

def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0    # Numero de elementos na primeira linha
    return num_rows, num_cols


def get_row(A, i):
    return A[i]     # A[i] já é da linha A[i] é linha i-ésimo


def get_column(A, j):
    return [A_i[j]              # j-ésimo elemento da linha A_i
            for A_i in A]       # para cada linha A_i


def make_matrix(num_rows, num_cols, entry_fn):
    """ Retorna a matriz num_rows X num_cols
    cuja entrada (i, j)th é entry_fn(i, j)"""
    return [[entry_fn(i, j)]                # dado i, cria uma lista
             for j in range(num_cols)       # [entry_fn(i, 0), ...}
             for i in range(num_rows)]      # cria uma lista para cada i


def is_diagonal(i, j):
    """ 1's na diagonal, 0's nos demais lugares"""
    return 1 if i == j else 0

