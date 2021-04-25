# Ex3
# By:
# Name: Yoni Ifrah - ID: 313914723
# Name: Coral Avital - ID: 205871163


def fixMatrix(matrix):
    """
    return the matrix that he got with the height value in the pivot indexes
    :param matrix: list, matrix
    :return: list, matrix
    """

    size = len(matrix)

    for i in range(size - 1):
        max = abs(matrix[i][i])

        for j in range(i+1, size):
            if abs(matrix[j][i] > max):
                tmp = matrix[i]
                matrix[i] = matrix[j]
                matrix[j] = tmp

    return matrix


def printMatrix(matrix):
    """
    print the matrix with \n between each vector
    :param matrix: list, matrix
    :return: none
    """

    for i in range(len(matrix)):
        print(matrix[i])

def getMax(matrix):
    """
    find the norm of each line in the matrix
    :param matrix: list, matrix
    :return: list , norm of the matrix
    """

    size = len(matrix)
    normVector = []

    for i in range(size):
        for j in range(size):
            matrix[i][j] = abs(matrix[i][j])

        normVector.append(max(matrix[i]))

    return normVector


def getPivot(matrix):
    """
    get the matrix and returns his pivot vector
    :param matrix: list, matrix
    :return: list, pivot victor of the matrix
    """

    pivote = []
    size = len(matrix)

    for i in range(size):
        for j in range(size):
            if i == j:
                pivote.append(matrix[i][j])

    return pivote


def DominantDiagonal(matrix):
    """
    check if the pivot has dominant diagonal
    :param matrix: list, matrix
    :return: boolean, true is we have pivot with dominant diagonal, else false
    """

    size = len(matrix)
    normVector = getMax(matrix)

    for i in range(size):
        s = sum(matrix[i]) - normVector[i]

        if s > normVector[i]:
            return False

    return True


def JacobiMethod(matrixA, matrixB):
    """
    using jacobi method for the matrix works only with 3x3 matrix!
    :param matrixA: list, matrix
    :param matrixB: list, matrix
    :return: None
    """

    x1 = [0, 0, 0]
    x2 = [0, 0, 0]
    pivote = getPivot(matrixA)
    count = 1
    print("{}.X-->{}".format(0, x2))

    while True:
        i = 0
        j = 0

        x2[i] = (matrixB[i] - matrixA[j][1] * x1[1] - matrixA[j][2] * x1[2]) / pivote[i]
        i += 1
        j += 1
        x2[i] = (matrixB[i] - matrixA[j][0] * x1[0] - matrixA[j][2] * x1[2]) / pivote[i]
        i += 1
        j += 1
        x2[i] = (matrixB[i] - matrixA[j][0] * x1[0] - matrixA[j][1] *x1[1]) / pivote[i]

        print("{}.X-->{}".format(count, x2))
        count += 1

        if abs(x2[0] - x1[0]) < 0.00001:
            break

        x1 = [i for i in x2]#deep copy of list



def GaussSeidelMethod(matrixA, matrixB):
    """
    using gauss seide method for the matrix works only with 3x3 matrix!
    :param matrixA: list, matrix
    :param matrixB: list, matrix
    :return: None
    """

    x1 = [0, 0, 0]
    x2 = [0, 0, 0]
    pivote = getPivot(matrixA)
    count = 1
    print("X.{} --> {}".format(0, x2))

    while True:
        i = 0
        j = 0

        x2[i] = (matrixB[i] - matrixA[j][1] * x1[1] - matrixA[j][2] * x1[2]) / pivote[i]
        i += 1
        j += 1
        x2[i] = (matrixB[i] - matrixA[j][0] * x2[0] - matrixA[j][2] * x1[2]) / pivote[i]
        i += 1
        j += 1
        x2[i] = (matrixB[i] - matrixA[j][0] * x2[0] - matrixA[j][1] * x2[1]) / pivote[i]

        print("X.{} --> {}".format(count, x2))
        count += 1

        if abs(x2[0] - x1[0]) < 0.00001:
            break

        x1 = [i for i in x2]


def getLUD(matrix):

    size = len(matrix)
    U = [[0 for i in range(size)] for j in range(size)] #higher
    L = [[0 for i in range(size)] for j in range(size)] #lower
    D = [[0 for i in range(size)] for j in range(size)] #middle

    for i in range(size):
        for j in range(size):

            if i == j:
                D[i][j] = matrix[i][j]

            if i < j:
                L[i][j] = matrix[i][j]

            if j < i:
                U[i][j] = matrix[i][j]

    return (L, U, D)


def mulMatrix(matrixA, matrixB):
    """
    return an I matrix with the same size of matrix that he got
    :param matrixA: list, matrix
    :param matrixB: list, matrix
    :return: list, matrix
    """
    result = []

    for i in range(0, len(matrixA)):
        tmp = []

        for j in range(0, len(matrixB[0])):
            sum = 0

            for k in range(0, len(matrixA[0])):
                sum += matrix1[i][k] * matrixB[k][j]
            tmp.append(sum)
        result.append(tmp)

    return result


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


def inverse(matrix):
    """
    return the inverse matrix using gauss elimination with
    :param matrix: list, matrix
    :return: list, the inverse matrix
    """
    tmp = [[] for _ in matrix]
    for i, row in enumerate(matrix):
        assert len(row) == len(matrix)
        tmp[i].extend(row + [0] * i + [1] + [0] * (len(matrix) - i - 1))
    gauss(tmp)
    ret = []
    for i in range(len(tmp)):
        ret.append(tmp[i][len(tmp[i])//2:])
    return ret


def plusMatrix(matrixA, matrixB):
    size = len(matrixA)
    result = [[0 for i in range(size)] for j in range(size)]
    for i in range(size):
        for j in range(size):
            result[i][j] = matrixA[i][j] + matrixB[i][j]
    return result


def negativeMat(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[i][j] =- (matrix[i][j])
    return matrix


def getNorm(matrix):
    size = len(matrix)
    s = []
    for i in range(size):
        for j in range(size):
            matrix[i][j] = abs(matrix[i][j])
        s.append(sum((matrix[i])))
    return max(s)


def getConvergeGauss(matrix):
    L,U,D = getLUD(matrix)
    G = mulMatrix(negativeMat((inverse(plusMatrix(L,D)))),U)

    if getNorm(G) < 1:
        print("Although the matrix does not have a dominant diagonal we can calculate with the help of Gauss")
        return True
    return False


def getConvergeJacobi(matrix):
    L, U, D=getLUD(matrix)
    G = mulMatrix(negativeMat(inverse(D), (inverse(plusMatrix(L, U)))))

    if getNorm(G) < 1:
        print("Although the matrix does not have a dominant diagonal we can calculate with the help of Jacobi")
        return True

    return False


def main():

    matrixA = [[4, 2, 0], [2, 10, 4], [0, 4, 5]]
    matrixB = [2, 6, 5]

    fixMatrix(matrixA)
    printMatrix(matrixA)

    while True:
        print("----------------------------------------")
        print("Which method do you wish to solve with?\nPress 1 --> for Jacobi\nPress 2 --> Gauss-Seidel\nPress another key to EXIT\n")
        choice = input()


        if choice == "1":
            print("The system gonna to check if the matrix have dominant diagonal")
            if DominantDiagonal(matrixA):
                print("The system gonna to solve the problem with Jacobi and the dominant diagonal")
                JacobiMethod(matrixA, matrixB)
            else:
                print("The system of the matrix does not converge!\nchecking with her norm vector if it converge...")
                if (getConvergeJacobi(matrixA)):
                    print("The system gonna to solve the problem with Jacobi and the norm vector")
                    JacobiMethod(matrixA, matrixB)
                else:
                    print("Cannot calculate! the matrix is not converge...")


        elif choice == "2":
            print("The system gonna to check if the matrix have dominant diagonal")

            if DominantDiagonal(matrixA):
                print("The system gonna to solve the problem with Gauss and the dominant diagonal")
                GaussSeidelMethod(matrixA, matrixB)

            else:
                print("The system of the matrix does not converge!\nchecking with her norm vector if it converge...")

                if getConvergeGauss(matrixA):
                    print("The system gonna to solve the problem with Gauss and the norm vector")
                    GaussSeidelMethod(matrixA, matrixB)

                else:
                    print("Cannot calculate! the matrix is not converge...")

        else:
            print("Goodbye!")
            break


main()