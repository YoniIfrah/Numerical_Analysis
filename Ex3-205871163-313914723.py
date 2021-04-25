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

def normVector(A):
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
    norm=normVector(A)
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
        x=[i for i in x1]



def GaussSeidelMethod(a,b):
    n = len(a)
    eps=0.001


def main():
    A=[[4,2,0],[2,10,4],[0,4,5]]
    B=[2,6,5]
    fixMatrix(A)
    if DominantDiagonal(A):
        printMatrix(A)
        while(True):
            print("----------------------------------------")
            print("which method do you wish to solve with?\n1 - for Jacobi\n2 - gauss-seidel\npress other key to exit\n")
            choice=input()
            if choice == "1":
                JacobiMethod(A,B)
            elif choice=="2":
                GaussSeidelMethod(A,B)

            else:
                print("Goodbye!")
                break
    else:
        print("The system of the matrix does not converge!")
        #need to fix here
        pass
main()