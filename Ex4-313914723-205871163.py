# Ex4
# By:
# Name: Yoni Ifrah - ID: 313914723
# Name: Coral Avital - ID: 205871163
import sympy as sp
from sympy.utilities.lambdify import lambdify

def Bisection_Method(f,startPoint,endPoint,eps):
    counter=0
    while(endPoint - startPoint)>eps:
        counter+=1
        c=(startPoint+endPoint)/2
        print("-----------------------------------------")
        print("Iteration: {},\tstart point: {},\tend point: {},\tApproximation: {}".format(counter,startPoint,endPoint,c))
        print("f(startPoint): {},\tf(endPoint): {},\tf(c): {}\n ABS(startPoint-c): {}".format(f(startPoint),f(endPoint),f(c),abs(startPoint-c)))
        if f(startPoint)*f(c)>0:
            startPoint=c
        else:
            endPoint=c


def Newton_Raphson():
    pass

def Secant_Method():
    pass






def main():
    x=sp.symbols('x')
    f = x**3-x-1
    fTag=f.diff(x)
    print('our function -->', f)
    print('our function after derivative -->', fTag)
    # order to insert x we will do
    f = lambdify(x, f)
    fTag = lambdify(x, fTag)
    print("f(1):", f(2))
    print("f'(1):", fTag(1))


    while True:
        print("----------------------------------------")
        print(
            "Which method do you wish to solve with?\nPress 1 --> Bisection Method\nPress 2 --> Newton Raphson\nPress 3 -->Secant_Method\nPress another key to EXIT\n")
        choice = input()
        if choice == "1":
            Bisection_Method(f,1,2,0.0001)

        elif choice == "2":
            pass
        elif choice == "3":
            pass
        else:
            print("Goodbye!")
            break

    pass




main()