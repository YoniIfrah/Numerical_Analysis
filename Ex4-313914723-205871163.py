# Ex4
# By:
# Name: Yoni Ifrah - ID: 313914723
# Name: Coral Avital - ID: 205871163

from math import cos
import sympy as sp
from sympy.utilities.lambdify import lambdify
# epsilon value for all the calculate
eps = 0.0000001

# A function for finding the values that cause the function to change a mark
def find_range_f(f, startPoint, endPoint):
    """
        Finds the suspected points and intersecting a function on the axis
        @:param: lambda,  f
        @:param: float, startPoint
        @:param float, endPoint
        @:return: list, rannge_list_f
    """
    # We run for all the point between the start point and the last point with jumps of 0.1
    rannge_list_f = []

    # While there are still range between the start point to the end point
    while endPoint >= startPoint:
        if f(startPoint) * f(startPoint + 0.1) < 0:
            rannge_list_f.append(round(startPoint, 3))
            rannge_list_f.append(round(startPoint + 0.1, 3))
        startPoint += 0.1

    # Returns two lists that hold the values when they are placed to change the function
    return rannge_list_f


def find_range_fT(fTag, startPoint, endPoint):
    """
        Finds the suspected points and intersecting a function derivative on the axis
        @:param: lambda,  fTag
        @:param: float, startPoint
        @:param: float, endPoint
        @:return: list, range_list_fT
    """
    range_list_fT = []
    while endPoint >= startPoint:
        if fTag(startPoint) * fTag(startPoint + 0.1) < 0:
            range_list_fT.append(round(startPoint, 3))
            range_list_fT.append(round(startPoint + 0.1, 3))
        startPoint += 0.1

    # Returns two lists that hold the values when they are placed to change the function
    return range_list_fT


# part one
def Bisection_Method(f1, f1Tag, startPoint, endPoint, eps):
    """
        The function finds us the existing intersection points on the axis with Bisection method
        @:param: lambda, f1
        @:param: lambda, f1Tag
        @:param: float, startPoint
        @:param: float, endPoint
        @:param: float, eps
        @:return: list, result
    """

    #integer counter for print the iteration
    counter = 0

    range_list_f = find_range_f(f1, startPoint, endPoint)
    range_list_fT = find_range_fT(f1Tag, startPoint, endPoint)

    result = []

    if range_list_f and range_list_fT:
        for i in range(0, len(range_list_f), 2):

            #Whilw loop that run until the difference between the end point and the start point is greater than epsilon
            while (range_list_f[i + 1] - range_list_f[i]) > eps:

                x_m = (range_list_f[i] + range_list_f[i + 1]) / 2

                counter += 1
                print("Iteration: ", counter)

                if f1(range_list_f[i]) * f1(x_m) > 0:
                    range_list_f[i] = x_m

                else:
                    range_list_f[i + 1] = x_m

            if round(x_m, 6) not in result:
                print("x: ", round(x_m, 6))
                result.append(round(x_m, 6))

        for i in range(0, len(range_list_fT), 2):

            #Whilw loop that run until the difference between the end point and the start point is greater than epsilon
            while (range_list_fT[i + 1] - range_list_fT[i]) > eps:

                x_m = (range_list_fT[i] + range_list_fT[i + 1]) / 2

                counter += 1
                print("Iteration: ", counter)

                if f1(range_list_fT[i]) * f1(x_m) > 0:
                    range_list_fT[i] = x_m
                else:
                    range_list_fT[i + 1] = x_m

            if round(x_m, 4) not in result:
                print("x: ", round(x_m, 4))
                result.append(round(x_m, 4))

    n = len(result)
    i = 0
    while i < n and n != 0:  # i<n or if list is not empty
        if not -0.1 < f1(result[i]) < 0.1:
            del result[i]
            n -= 1
            i = 0
        else:
            i += 1

    return result


# part two
def Newton_Raphson(f2, f2Tag, startPoint, endPoint, eps):
    """
        The function finds us the existing intersection point  on the axis with Newton method
        notice - only one point then we run again from the main function
        @:param: lambda, f2
        @:param: lambda, f2Tag
        @:param: float, startPoint
        @:param: float, endPoint
        @:param: float, eps
        @:return: list, result
    """

    x_r = (endPoint + startPoint) / 2
    if f2(x_r) != 0:
        x_next = x_r - (f2(x_r) / f2Tag(x_r))
    else:
        print("Please wait trying  closer range")
        return None

    counter = 1

    if round(f2(startPoint), 5) == 0:
        print("x: ", round(startPoint, 4))
        return round(x_r, 5)

    elif round(f2(endPoint), 5) == 0:
        print("x: ", round(endPoint, 4))
        return endPoint


    if f2(startPoint) > 0 and f2(endPoint) < 0 or f2(startPoint) < 0 and f2(endPoint) > 0:
        #A while loop that checks when the range between the two numbers is less than eps
        while x_next - x_r < eps:
            # Do it if the condition is not met

            print("Iteration: ", counter)

            if round(f2(x_r), 5) == 0:
                print("x: ", round(x_r, 6))
                return round(x_r, 6)

            counter += 1
            x_r = x_next
            x_next = x_r - (f2(x_r) / f2Tag(x_r))
    else:
        print("Error! The function does not converge")


# part tree
def Secant_Method(f3, startPoint, endPoint, eps):
    """
        The function finds us the existing intersection points on the axis with Secant method
        @:param:lambda, f3
        @:param:float, startPoint
        @:param:float, endPoint
        @:param:float, eps
        @:return:list, result
    """

    result_list = []
    counter = 1

    range_list = find_range_f(f3, startPoint, endPoint)

    for i in range(0, len(range_list), 2):
        x_r = range_list[i]
        x_next = range_list[i + 1]

        while abs(x_next - x_r) > eps:

            print("Iteration: ", counter)
            if round(f3(x_r), 6) == 0:
                print("x: ", round(x_r, 6))
                result_list.append(round(x_r, 6))

            last_r = x_r
            x_r = x_next
            x_next = (last_r * f3(x_r) - x_r * f3(last_r)) / (f3(x_r) - f3(last_r))
            counter += 1
    return result_list


# main function
def main():

    # x symbol
    x = sp.symbols('x')

    startPoint = 0
    endPoint = 0

    # While the user entered number between 1 to 3
    # If he inserted another character the loop will stop
    while True:
        print("----------------------------------------")
        print("Hello !\nWhich method do you wish to solve with?\nPress 1 --> Bisection Method\n"
        "Press 2 --> Newton Raphson\nPress 3 -->Secant_Method\nPress another key to EXIT\n")
        choice = input()

        if choice == "1":
            print("\n----------------------------------------")
            print("Bisection Method")

            # The function for part 1
            f1 = x ** 4 + x ** 3 - 3 * x ** 2
            # A new variable that holds the derivative of the function
            f1Tag = f1.diff(x)
            print('our function -->', f1)
            print('our function after derivative -->', f1Tag)

            # order to insert x we will do
            f1 = lambdify(x, f1)
            f1Tag = lambdify(x, f1Tag)


            startPoint = -3.0
            endPoint = 2.0
            result_list = Bisection_Method(f1, f1Tag, startPoint, endPoint, eps)
            if result_list:
                print("----------------------------------------")
                print("The results of the function are: ", result_list)

            else:
                print("No result found!")

        elif choice == "2":
            print("\n----------------------------------------")
            print("Newton Raphson")

            # The function for part 2
            # f2 = 4 * x ** 3 - 48 * x + 5
            f2 = x ** 3 - x - 1
            # A new variable that holds the derivative of the function
            f2Tag = f2.diff(x)

            print('our function -->', f2)
            print('our function after derivative -->', f2Tag)

            # order to insert x we will do
            f2 = lambdify(x, f2)
            f2Tag = lambdify(x, f2Tag)

            result_list = []

            startPoint = 1.0
            endPoint = 2.0

            range_list_f = find_range_f(f2,  startPoint, endPoint)
            range_list_fT = find_range_fT(f2Tag, startPoint, endPoint)

            for i in range(0, len(range_list_f), 2):
                answer = Newton_Raphson(f2, f2Tag, range_list_f[i], range_list_f[i+1], eps)
                if answer not in result_list and answer is not None:
                    result_list.append(answer)

            for i in range(0, len(range_list_fT), 2):
                answer = Newton_Raphson(f2, f2Tag, startPoint, endPoint, eps)
                if answer not in result_list and answer is not None:
                    result_list.append(answer)

            if result_list:
                print("----------------------------------------")
                print("The results of the function are: ", result_list)

            else:
                print("No result found!")

        elif choice == "3":

            print("\n----------------------------------------")
            print("Secant Method")
            y = sp.cos

            # The function for part 3
            f3 = x ** 3 - y(x)
            print('our function -->', f3)
            # order to insert x we will do
            f3 = lambdify(x, f3)

            startPoint = 0.0
            endPoint = 1.0

            result_list = Secant_Method(f3, startPoint, endPoint, eps)
            if result_list:
                print("----------------------------------------")
                print("The results of the function are: ", result_list)

            else:
                print("No result found!")

        else:
            print("\n----------------------------------------")
            print("Goodbye!")
            print("\n----------------------------------------")
            # stop the loop
            break


# Call to main function
main()
