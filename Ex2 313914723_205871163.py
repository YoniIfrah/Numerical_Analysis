



def getCofactor(matrix, i, j):
    return [row[:j] + row[j+1:] for row in (matrix[: i] + matrix[i+1:])]


def isSingular(matrix):
    if getDet(matrix) != 0:
        return False
    return True


def getDet(matrix):
    n = len(matrix)
    if n == 2:
        val = matrix[0][0]*matrix[1][1] - matrix[1][0]*matrix[0][1]
        return val
    else:
        det = 0
        for i in range(n):
            s = (-1)
            sum = getDet(getCofactor(matrix, 0, i))
            det += (s*matrix[0][i]*sum)
        return det


def isSquares(matrix):
    for i in range(0, len(matrix)):
        if len(matrix) != len(matrix[i]):
            return False
    return True


def chackIfCanMul(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        return False
    return True


# we can mul two matrix when the first matrix with n*m values and the second matrix with m*n values
def mulMatrix(matrix1, matrix2):
    result = []
    for i in range(0, len(matrix1)):
        tmp = []
        for j in range(0, len(matrix2[0])):
            sum = 0
            for k in range(0, len(matrix1[0])):
                sum += matrix1[i][k] * matrix2[k][j]
            tmp.append(sum)
        result.append(tmp)
    return result


def changeMat(matrix):
    max, min = matrix[0], matrix[0]
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            if max[0] < matrix[j][0]:
                max = matrix[j]
            if min[0] > matrix[j][0]:
                min = matrix[j]
    for i in range(0, len(matrix)):
        if max == matrix[i]:
            matrix[i] = min
    matrix[0] = max
    return matrix


def findPivot(matrix):
    m = len(matrix)
    IDMatrix = [[float(i ==j) for i in range(m)] for j in range(m)]
    for j in range(m):
        row = max(range(j, m), key=lambda i: abs(matrix[i][j]))
        if j != row:
            # Swap the rows
            IDMatrix[j], IDMatrix[row] = IDMatrix[row], IDMatrix[j]
    return IDMatrix


def getLU(matrix):
    n = len(matrix)
    L = [[0.0] * n for i in range(n)]
    U = [[0.0] * n for i in range(n)]
    P = findPivot(matrix)
    PA = mulMatrix(P, matrix)
    for j in range(n):
        L[j][j] = 1.0
        for i in range(j+1):
            s1 = sum(U[k][j] * L[i][k] for k in range(i))
            U[i][j] = PA[i][j] - s1
        for i in range(j, n):
            s2 = sum(U[k][j] * L[i][k] for k in range(j))
            if U[j][j] != 0:
                L[i][j] = (PA[i][j] - s2) / U[j][j]
    return (P, L, U)


def eliminate(row1, row2, coloumb, target=0):
    fac = (row2[coloumb] - target) / row1[coloumb]
    for i in range(len(row2)):
        row2[i] -= fac * row1[i]


def gauss(matrix):
    for i in range(len(matrix)):
        if matrix[i][i] == 0:
            for j in range(i + 1, len(matrix)):
                if matrix[i][j] != 0:
                    matrix[i], matrix[j] = matrix[j], matrix[i]
                    break
            else:
                raise ValueError("Matrix is not invertible")
        for j in range(i + 1, len(matrix)):
            eliminate(matrix[i], matrix[j], i)
    for i in range(len(matrix) - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            eliminate(matrix[i], matrix[j], i)
    for i in range(len(matrix)):
        eliminate(matrix[i], matrix[i], i, target=1)
    return matrix


def inverse(matrix):
    tmp = [[] for _ in matrix]
    for i, row in enumerate(matrix):
        assert len(row) == len(matrix)
        tmp[i].extend(row + [0] * i + [1] + [0] * (len(matrix) - i - 1))
    gauss(tmp)
    ret = []
    for i in range(len(tmp)):
        ret.append(tmp[i][len(tmp[i]) // 2:])
    return ret


def main():
    # A = [[1, 2, 1], [2, 6, 1], [1, 1, 4]]
    B = [[1], [2], [3], [5]]
    A = [[0, 1, 1, 1], [1, 1, 2, 1], [2, 2, 4, 0], [1, 2, 1, 1]]
    if isSquares(A):
        if not isSingular(A):
            if chackIfCanMul(A, B):
                A = inverse(A)
                x = mulMatrix(A, B)
                print("The result of x is --> {}".format(x))
            else:
                print("ooh...Cannot multiply this matrices")
        else:
            A = changeMat(A)
            P, L, U = getLU(A)
            print("U: {}".format(U))
            print("L: {}".format(L))
            L = inverse(L)
            y = mulMatrix(L, B)
            U = inverse(U)
            x = mulMatrix(U, y)
            print("The result of x is --> {}".format(x))

main()
