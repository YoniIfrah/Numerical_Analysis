# Ex2
# By:
# Name: Yoni Ifrah - ID: 313914723
# Name: Coral Avital - ID: 205871163


def getCofactor(matrix, i, j):
    """
    return the cofactor vector
    :param matrix: list, matrix
    :param i: int, index
    :param j: int, index
    :return: list, matrix
    """
    return [row[:j] + row[j+1:] for row in (matrix[: i] + matrix[i+1:])]


def isSingular(matrix):
    """
    retuen True if the matrix is singular.
    :param matrix: list, matrix
    :return: boolean
    """
    if getDet(matrix) != 0:
        return False
    return True


def getDet(matrix):
    """
    return the determinant of the matrix
    :param matrix: list, matrix
    :return: list, matrix
    """
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
    """
    return True if the matrix is square
    :param matrix: list, matrix
    :return: list, matrix
    """
    for i in range(0, len(matrix)):
        if len(matrix) != len(matrix[i]):
            return False
    return True


# we can mul two matrix when the first matrix with n*m values and the second matrix with m*n values
def mulMatrix(matrix1, matrix2):
    """
    return an I matrix with the same size of matrix that he got
    :param matrix1: list, matrix
    :param matrix2: list, matrix
    :return: list, matrix
    """
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


def getI(matrix):
    """
    return an I matrix with the same size of matrix that he got
    :param matrix: list, matrix
    :return: list, matrix
    """
    I = [[0 for i in range(0, len(matrix))] for j in range(0, len(matrix))]
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            if i == j:
                I[i][j] = 1
    return I


def changeMat(matrix):
    """
    return the matrix after changing the rows so the matrix[0][0] index has the highest value in the columns
    :param matrix: list, matrix
    :return: list, matrix
    """
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


def fixMatrix(matrix):
    """
    return the matrix that he got with the height value in the pivot indexes
    :param matrix: list, matrix
    :return: list, matrix
    """
    N = len(matrix)
    for i in range(N-1):
        max = abs(matrix[i][i])
        for j in range(i+1, N):
            if abs(matrix[j][i] > max):
                tmp = matrix[i]
                matrix[i] = matrix[j]
                matrix[j] = tmp
    return matrix


# return the inverse matrix using gauss elimination
def inverse(matrix):
    """
    return the inverse matrix using gauss elimination with
    :param matrix: list, matrix
    :return: list, the inverse matrix
    """
    tmp = [[] for _ in matrix]
    for i,row in enumerate(matrix):
        assert len(row) == len(matrix)
        tmp[i].extend(row + [0] * i + [1] + [0] * (len(matrix) - i - 1))
    gauss(tmp)
    ret = []
    for i in range(len(tmp)):
        ret.append(tmp[i][len(tmp[i])//2:])
    return ret


def eliminate(r1, r2, col, target=0):
    """
    :param r1: list, row
    :param r2: list, row
    :param col: list, col
    :param target: int
    """
    fac = (r2[col]-target) / r1[col]
    for i in range(len(r2)):
        r2[i] -= fac * r1[i]


def gauss(matrix):
    """
    :param matrix: list, matrix
    :return matrix: list, matrix
    """
    for i in range(len(matrix)):
        if matrix[i][i] == 0:
            for j in range(i+1, len(matrix)):
                if matrix[i][j] != 0:
                    matrix[i], matrix[j] = matrix[j], matrix[i]
                    break
            else:
                raise ValueError("Matrix is not invertible")
        for j in range(i+1, len(matrix)):
            eliminate(matrix[i], matrix[j], i)
    for i in range(len(matrix) - 1, -1, -1):
        for j in range(i-1, -1, -1):
            eliminate(matrix[i], matrix[j], i)
    for i in range(len(matrix)):
        eliminate(matrix[i], matrix[i], i, target=1)
    return matrix


def changeCol(matrix):
    """
    function  making sure that the last vector will be at the end in case is not, also save us time of calculation
    :param matrix: list, matrix
    :return: list , fixed matrix
    """
    N= len(matrix)
    for i in range(N-1):
        count = 0
        if matrix[i][0]==0:
            for j in range(N-1):
                if matrix[i][j] == 0:
                    count += 1
                    if count == N-1:
                        matrix[N - 1], matrix[i] = matrix[i], matrix[N - 1]
    return matrix


def getPivot(matrix):
    """
    get the matrix and returns his pivot vector
    :param matrix: list, matrix
    :return: list, pivot victor of the matrix
    """
    P = []
    N = len(matrix)
    for i in range(N):
        for j in range(N):
            if i == j:
                P.append(matrix[i][j])
    return P


def calcLU(matrix):
    """
    function that calc the LU of the matrix
    :param matrix: list, matrix
    :return: list, LU matrices
    """
    I = getI(matrix)
    N = len(matrix)
    k = 0
    check = []
    for i in range(N):
        for j in range(N):
            if i == j:
                check.append(k)
                k += 1

    i = 0
    j = N-1
    n = N
    L = getI(matrix)
    m = n-1
    k = 0
    while(k < N-1):
        n = N

        while(check[k] < n):
            j = N-1
            i = 0
            m = n - 1 - k

            while(i < check[m]):
                P = getPivot(matrix)
                if P[k] != 0:
                    I[check[j]][k] = -(matrix[j][k] / P[k])
                j -= 1
                i += 1

            L = mulMatrix(L, inverse(I))
            matrix = mulMatrix(I, matrix)
            matrix = changeCol(matrix)
            I = getI(matrix)
            n -= 1
            break

        k += 1
    return (L, matrix)


def Main():
    """
    the main function
    """
    b = [[1], [2], [3]]
    a = [[4, 5, -6], [2, 5, 2], [1, 3, 2]]
    c = [[1, 4, -3], [-2, 8, 5], [3, 4, 7]]
    d = [[0, 1, 1, 1], [1, 1, 2, 1], [2, 2, 4, 0], [1, 2, 1, 1]]

    if not len(a) >= 4:
        c = fixMatrix(c)
    a = changeMat(c)
    if isSquares(a):
        if len(a) < 4:
            if isSingular(a):
                x = mulMatrix(inverse(fixMatrix(a)), b)
                print('X:\t{}'.format(x))
            else:
                L, U = calcLU(a)
                U = fixMatrix(U)
                print('U:\t{}\nL:\t{}'.format(U, L))
        else:# LU
            L, U = calcLU(a)
            U = fixMatrix(U)
            print('U:\t{}\nL:\t{}'.format(U, L))
    else:
        print('is not square matrix')


# start the program
Main()
