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
    N = len(matrix)
    for i in range(N-1):
        max = abs(matrix[i][i])
        for j in range(i+1, N):
            if abs(matrix[j][i] > max):
                tmp = matrix[i]
                matrix[i] = matrix[j]
                matrix[j] = tmp
    return matrix

def printMatrix(A):
    """
    print the matrix with \n between each vector
    :param A: list, matrix
    :return: none
    """
    for i in range(len(A)):
        print(A[i])

def getMax(A):
    """
    find the norm of each line in the matrix
    :param A: list, matrix
    :return: list , norm of the matrix
    """
    N=len(A)
    norm=[]
    for i in range(N):
        for j in range(N):
            A[i][j] = abs(A[i][j])

        norm.append(max(A[i]))
    return norm


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



def DominantDiagonal(A):
    """
    check if the pivot has dominant diagonal
    :param A: list, matrix
    :return: boolean, true is we have pivot with dominant diagonal, else false
    """
    N=len(A)
    norm=getMax(A)
    for i in range(N):
        s=sum(A[i])-norm[i]
        if s>norm[i]:
            return False
    return True

def JacobiMethod(A,B):
    """
    using jacobi method for the matrix works only with 3x3 matrix!
    :param A: list, matrix
    :param B: list, matrix
    :return: None
    """
    x=[0,0,0]
    x1=[0,0,0]
    P=getPivot(A)
    count=1
    print("{}.X-->{}".format(0, x1))

    while(True):
        i = 0
        j = 0

        x1[i]=(B[i]-A[j][1]*x[1]-A[j][2]*x[2])/P[i]
        i+=1
        j+=1
        x1[i]=(B[i]-A[j][0]*x[0]-A[j][2]*x[2])/P[i]
        i+=1
        j+=1#2
        x1[i]=(B[i]-A[j][0]*x[0]-A[j][1]*x[1])/P[i]

        print("{}.X-->{}".format(count,x1))
        count+=1
        if abs(x1[0]-x[0])<0.00001:
            break
        x=[i for i in x1]#deep copy of list



def GaussSeidelMethod(A,B):
    """
    using gauss seide method for the matrix works only with 3x3 matrix!
    :param A: list, matrix
    :param B: list, matrix
    :return: None
    """
    x = [0, 0, 0]
    x1 = [0, 0, 0]
    P = getPivot(A)
    count = 1
    print("{}.X-->{}".format(0, x1))
    while (True):
        i = 0
        j = 0

        x1[i] = (B[i] - A[j][1] * x[1] - A[j][2] * x[2]) / P[i]
        i += 1
        j += 1
        x1[i] = (B[i] - A[j][0] * x1[0] - A[j][2] * x[2]) / P[i]
        i += 1
        j += 1  # 2
        x1[i] = (B[i] - A[j][0] * x1[0] - A[j][1] * x1[1]) / P[i]

        print("{}.X-->{}".format(count, x1))
        count += 1
        if abs(x1[0] - x[0]) < 0.00001:
            break
        x = [i for i in x1]

def getLUD(A):
    N=len(A)
    U = [[0 for i in range(N)] for j in range(N)]#higher
    L=  [[0 for i in range(N)] for j in range(N)]#lower
    D = [[0 for i in range(N)] for j in range(N)]#middle
    for i in range(N):
        for j in range(N):
            if i==j:
                D[i][j]=A[i][j]
            if i<j:
                L[i][j]=A[i][j]
            if j<i:
                U[i][j]=A[i][j]
    return (L,U,D)

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
    for i,row in enumerate(matrix):
        assert len(row) == len(matrix)
        tmp[i].extend(row + [0] * i + [1] + [0] * (len(matrix) - i - 1))
    gauss(tmp)
    ret = []
    for i in range(len(tmp)):
        ret.append(tmp[i][len(tmp[i])//2:])
    return ret

def plusMatrix(A,B):
    N=len(A)
    result=[[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            result[i][j]=A[i][j]+B[i][j]
    return result

def negativeMat(A):
    for i in range(len(A)):
        for j in range(len(A)):
            A[i][j]=-(A[i][j])
    return A

def getNorm(A):
    N=len(A)
    s=[]
    for i in range(N):
        for j in range(N):
            A[i][j]=abs(A[i][j])
        s.append(sum((A[i])))
    return max(s)


def getConvergeGauss(A):
    L,U,D=getLUD(A)
    G=mulMatrix(negativeMat((inverse(plusMatrix(L,D)))),U)
    #G=[[1,2],[-3,4]]
    if getNorm(G)<1:
        print("Although the matrix does not have a dominant diagonal we can calculate with the help of Gauss")
        return True
    return False

def getConvergeJacobi(A):
    L,U,D=getLUD(A)
    G=mulMatrix(negativeMat(inverse(D),((plusMatrix(L,U)))))
    #G=[[1,2],[-3,4]]
    if getNorm(G)<1:
        print("Although the matrix does not have a dominant diagonal we can calculate with the help of Jacobi")
        return True
    return False






def main():
    A=[[4,2,0],[2,10,4],[0,4,5]]
    B=[2,6,5]
    fixMatrix(A)
    printMatrix(A)
    while(True):
        print("----------------------------------------")
        print("which method do you wish to solve with?\n1 - for Jacobi\n2 - Gauss-Seidel\npress other key to exit\n")
        choice=input()
        if choice == "1":
            print("The system gonna to check if the matrix have dominant diagonal")
            if DominantDiagonal(A):
                print("The system gonna to solve the problem with Jacobi and the dominant diagonal")
                JacobiMethod(A,B)
            else:
                print("The system of the matrix does not converge!\nchecking with her norm vector if it converge...")
                if (getConvergeJacobi(A)):
                    print("The system gonna to solve the problem with Jacobi and the norm vector")
                    JacobiMethod(A, B)
                else:
                    print("cannot calculate! the matrix is not converge...")
        elif choice=="2":
            print("The system gonna to check if the matrix have dominant diagonal")
            if  DominantDiagonal(A):
                print("The system gonna to solve the problem with Gauss and the dominant diagonal")
                GaussSeidelMethod(A,B)
            else:
                print("The system of the matrix does not converge!\nchecking with her norm vector if it converge...")
                if (getConvergeGauss(A)):
                    print("The system gonna to solve the problem with Gauss and the norm vector")
                    GaussSeidelMethod(A, B)
                else:
                    print("cannot calculate! the matrix is not converge...")
        else:
            print("Goodbye!")
            break


main()