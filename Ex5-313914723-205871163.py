# Ex5
# By:
# Name: Yoni Ifrah - ID: 313914723
# Name: Coral Avital - ID: 205871163

def findXandY(Xpoint, chart):
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

    #print to test
    print("x1:{} y1:{} x2:{} y2:{}".format(x1, y1, x2, y2))

    return (x1, x2, y1, y2)

def Linear(Xpoint,chart):
    x1, x2, y1, y2 = findXandY(Xpoint, chart)
    return ((y1-y2)/(x1-x2))*Xpoint+(y2*x1-y1*x2)/(x1-x2)





def main():
    #define  chart and point
    Xpoint = 2.5

    print("our point to find -->", Xpoint)

    #define 2D chart with numbers of x value and y value
    chart = [[0, 1, 2, 3, 4, 5, 6], [0, 0.8415, 0.9093, 0.1411, -0.7568, -0.9589, -0.2794]]



    while True:
        print("Which method do you wish to solve with?\nPress 1 --> for Linear\nPress 2 --> Polynomial\nPress 3 --> for Lagrange\nPress 4 for Neville\nPress another key to EXIT\n")
        choice = input()

        if choice == "1":
            print("result:",Linear(Xpoint, chart))

        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        else:
            print("Goodbye!")
            break



main()