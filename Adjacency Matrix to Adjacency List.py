adj_mat = [[0, 1, 0, 1], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 1, 0]]

def mat_to_list(matrix):
    adj_list = {}
    for i in range(len(matrix)):
        adj_list[i] = []
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                adj_list[i].append(j)
    return adj_list