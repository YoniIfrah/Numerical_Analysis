

def getCofactor(matrix, i, j):
    return [row[:j] + row[j+1:] for row in (matrix[: i] + matrix[i+1:])]


def isSingular(matrix):
    if getDet(matrix) == 0:
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
            s = (-1)**i
            sum = getDet(getCofactor(matrix, 0, i))
            det += (s*matrix[0][i]*sum)
        return det


def isSquares(matrix):
    for i in range(0, len(matrix)):
        if len(matrix) != len(matrix[i]):
            return False
    return True


def transposeMatrix(matrix):
    return list(map(list, zip(*matrix)))


def getMatrixInverse(matrix):
    det = getDet(matrix)
    #special case for 2x2 matrix:
    if len(matrix) == 2:
        return [[matrix[1][1]/det, -1*matrix[0][1]/det],
                [-1*matrix[1][0]/det, matrix[0][0]/det]]
    # find matrix of cofactors
    cofactors = []
    for r in range(len(matrix)):
        cofactorRow = []
        for c in range(len(matrix)):
            minor = getCofactor(matrix, r, c)
            cofactorRow.append(((-1) ** (r + c)) * getDet(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c] / det
    return cofactors


def main():
    A = [[3, 4, 9], [0, 2, 6], [6, 6, 7]]
    B = [[0, 1], [7, 4]]

    if isSquares(A):
        if isSingular(A):
            print(getMatrixInverse(A))


main()
