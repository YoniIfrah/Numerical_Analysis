# Ex5
# By:
# Name: Yoni Ifrah - ID: 313914723
# Name: Coral Avital - ID: 205871163
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
                sum += matrixA[i][k] * matrixB[k][j]
            tmp.append(sum)
        result.append(tmp)

    return result

def findXandY(Xpoint, chart):
    """
    Finding the minimum and the maximum number that close to Xpoint.
    According to the chat in that case the function will return int.
    :param Xpoint: float, the point we want to find
    :param chart:list, table that include x and y values
    :return: int, the closest x to Xpoint ansd their y according to the chart
    """
    # find x1 and x2
    for i in chart[0]:
        if Xpoint > chart[0][i]:
            x1 = chart[0][i]
        elif Xpoint < chart[0][i]:
            x2 = chart[0][i]
            break

    #find y1 and y2
    y1 = chart[1][x1]
    y2 = chart[1][x2]

    return (x1, x2, y1, y2)

def Linear(Xpoint,chart):
    """
    Finding Xpoint value with linear method by using the chart
    :param Xpoint: float, the point we want to find
    :param chart:list, table that include x and y values
    :return: float, the value between the point using linear method
    """
    x1, x2, y1, y2 = findXandY(Xpoint, chart)
    return round(((y1-y2)/(x1-x2))*Xpoint+(y2*x1-y1*x2)/(x1-x2),4)



def Polynomial(Xpoint,chart):
    """
    Finding Xpoint from the chart we got by using polynomial method
    :param Xpoint: float, the point we want to find
    :param chart:list, table that include x and y values
    :return: float, the result of the polynomail
    """
    N = len (chart[0])
    #declare matrix with all values is 1
    matrix = [[1 for i in range(N)] for j in range(N)]
    #etner matrix new values according to the chart
    i=0
    for item in chart[0]:
        while i < N:
            k = 1
            for j in range(1,N):
                matrix[i][j] = item**k
                k += 1
            break
        i += 1

    #transpose chart[1] to be able to multiply it with matrix
    new_tmp=[]
    for item in chart[1]:
        tmp=[]
        tmp.append(item)
        new_tmp.append(tmp)

    #saving the result of multiply matrices
    vectorA = mulMatrix(inverse(matrix), new_tmp)


    result = 0
    for i in range(len(vectorA)):
        if i == 0:
            result += vectorA[i][0]
        else:
            result += vectorA[i][0]*(Xpoint**i)

    return round(result,4)


def Lagrange(Xpoint, chart):
    """
    Finding the point using lagrange method
    :param Xpoint:float, the point we want to find
    :param chart:list, table that include x and y values
    :return:float, summ
    """

    new_list = []
    N = len(chart[0])

    #declaring new list from our chart for lagrange method
    for i in range(N):
        tmp_list=[]
        tmp_list.append(chart[0][i])
        tmp_list.append(chart[1][i])
        new_list.append(tmp_list)

    #lagrange method
    summ = 0
    result = []
    tmp = 1
    for i in range(len(new_list)):
        for j in range(len(new_list)):
            if i != j:
                tmp *= (Xpoint - new_list[j][0]) / (new_list[i][0] - new_list[j][0])
        result.append(tmp)
        tmp = 1
    for i in range(N):
        summ += result[i] * new_list[i][1]
    return summ


def Neville(Xpoint, chart):
    """
    Using recursion for Neville method
    :param Xpoint:float, the point we want to find
    :param chart:list, table that include x and y values
    :return: float, the polynomial of degree n
    """

    n = len(chart[0])
    p = n * [0]
    for k in range(n):
        for i in range(n - k):
            if k == 0:
                p[i] = chart[1][i]
            else:
                p[i] = ((Xpoint - chart[0][i + k]) * p[i] + \
                        (chart[0][i] - Xpoint) * p[i + 1]) / \
                       (chart[0][i] - chart[0][i + k])
    return p[0]


def main():
    """
    Here we got each X (Xpoint) and data table (chart) for each method.
    The solution will be display according to the input otherwise the program will be closed
    :return: None
    """
    #define  charts and points
    Xpoint1 = 2.5
    Xpoint3 = 3
    Xpoint4 = 1.5

    #define 2D chart with numbers of x value and y value
    chart = [[0, 1, 2, 3, 4, 5, 6], [0, 0.8415, 0.9093, 0.1411, -0.7568, -0.9589, -0.2794]]
    chart2 = [[1, 2, 3], [0.8415, 0.9093, 0.1411]]
    chart3 = [[1, 2, 4], [1, 0, 1.5]]
    chart4 = [[1, 1.3, 1.6, 1.9, 2.2], [0.7651, 0.6200, 0.4554, 0.2818, 0.1103]]

    print("Linear and Polynomial points -->", Xpoint1,", Lagrange point -->", Xpoint3,", Neville point -->", Xpoint4)
    print("Linear chart -->", chart,", Polynomial chart -->", chart2,"\nLagrange chart -->", chart3,", Neville chart -->", chart4)


    while True:
        print("Which method do you wish to solve with?\nPress 1 --> for Linear\nPress 2 --> Polynomial\nPress 3 --> for Lagrange\nPress 4 --> for Neville\nPress another key to EXIT\n")
        choice = input()

        if choice == "1":
            print("result:",Linear(Xpoint1, chart))

        elif choice == "2":
            print("result:",Polynomial(Xpoint1, chart2))

        elif choice == "3":
            print("result:",Lagrange(Xpoint3, chart3))

        elif choice == "4":
            result = Neville(Xpoint4, chart4)
            print("result:", round(result,4))

        else:
            print("Goodbye!")
            break



main()