adj_mat = [[0, 1, 0, 1, 0, 0],
             [0, 0, 1, 0, 0, 0],
             [1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0],
             [0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 0]]

def mat_to_list(adj_mat):
    adj_list = {}
    for i in range(len(adj_mat)):
        adj_list[i] = []
        for j in range(len(adj_mat[i])):
            if adj_mat[i][j] == 1:
                adj_list[i].append(j)
    return adj_list
adj_list = mat_to_list(adj_mat)
print(adj_list)