# Ex4
# By:
# Name: Yoni Ifrah - ID: 313914723
# Name: Coral Avital - ID: 205871163
import sympy as sp
from sympy.utilities.lambdify import lambdify

"""
the function running by 0.1 steps to find if the function change sign from x to limit
when x is the start point and finish at limit
@:param:lambda: f, lambda: fTag, int: x, int: limit
@:returns: list: llist, list: llist2
"""
def findRange(f,fTag,x,limit):
    llist = []
    llist2 = []
    counter = 1
    while (x <= limit):
#        print("f(x1):", f(x))
#        print("f(x2):", f(x + 0.1))
        if (f(x) * f(x + 0.1) < 0):
            llist.append(round(x,3))
            llist.append(round(x + 0.1,3))
        if (fTag(x)*fTag(x+0.1)<0):
            llist2.append(round(x,3))
            llist2.append(round(x + 0.1,3))
#        print("counter = ", counter)
        counter += 1
        x += 0.1
    #print("{}".format(llist))
    #print("{}".format(llist2))
    return (llist,llist2)





def Bisection_Method(f,startPoint,endPoint,eps):
    counter=0
    while(endPoint - startPoint)>eps:
        counter+=1
        c=(startPoint+endPoint)/2
        print("-----------------------------------------")
        print("Iteration: {},\nstart point: {},\tend point: {},\tc: {}".format(counter,startPoint,endPoint,c))
        print("f(startPoint): {},\tf(endPoint): {},\tf(c): {}\n ABS(startPoint-c): {}".format(f(startPoint),f(endPoint),f(c),abs(startPoint-c)))
        if f(startPoint)*f(c)>0:
            startPoint=c
        else:
            endPoint=c
    return round(c, 5)


def Newton_Raphson():
    pass

def Secant_Method():
    pass






def main():
    x=sp.symbols('x')
    #f = x**4+x**3-3*x**2
    f=x**3-x-1
    fTag=f.diff(x)
    print('our function -->', f)
    print('our function after derivative -->', fTag)
    print("range: max is 2 and the minimum is 1")
    # order to insert x we will do
    f = lambdify(x, f)
    fTag = lambdify(x, fTag)



    while True:
        print("----------------------------------------")
        print(
            "Which method do you wish to solve with?\nPress 1 --> Bisection Method\nPress 2 --> Newton Raphson\nPress 3 --> Secant_Method\nPress another key to EXIT\n")
        choice = input()
        if choice == "1":
            funcRange = []
            derivativeRange = []
            funcRange, derivativeRange = findRange(f, fTag, 1, 2)
            if funcRange and derivativeRange:  # check if we got range
                result=[]
                for i in range(0,len(funcRange),2):
                    result.append(Bisection_Method(f,funcRange[i],funcRange[i+1],0.0001))

                for i in range (0,len(derivativeRange),2):
                    result.append(Bisection_Method(fTag,derivativeRange[i],derivativeRange[i+1],0.0001))
                n=len(result)
                i=0
                while(i<n or not result):# i<n or if list is not empty
                    if not f(result[i])>-0.0001 and f(result[i])<0.0001:
                        del result[i]
                        n-=1
                        i=0
                    else:
                        i+=1
                print("result: ",result)
            else:
                print("ERROR! no range found")

        elif choice == "2":
            for i in range(0,len(funcRange),2):
                Newton_Raphson(f,funcRange[i],funcRange[i+1],0.0001)
        elif choice == "3":
            pass
        else:
            print("Goodbye!")
            break






main()