
def matrix_multiply(mat1, mat2):
    transferd_matrix=trnsfering_matrix(mat2)
    final_list=[]
    for i in mat1:
        pre_final_list = []
        for j in transferd_matrix:
            res_list = []
            for l in range(0, len(i)):
                res_list.append(i[l] * j[l])
            pre_final_list.append(sum(res_list))
        final_list.append(pre_final_list)
    print(final_list)

def trnsfering_matrix(mat2):
    m, n = len(mat2), len(mat2[0])
    result = []
    for col in range(n):
        result.append([])
        for row in range(m):
            result[col].append(mat2[row][col])
    print(result)
    return result

mat1 = [[3,2],[6,13]]
mat2 = [[3,2],[6,13]]
matrix_multiply(mat1,mat2)
matrix_multiply([[1,1],[1,1]],[[1,1],[1,1]])
matrix_multiply([[3,2],[6,13]],[[1,0],[0,1]])
# transferd_matrix=trnsfering_matrix(mat2)