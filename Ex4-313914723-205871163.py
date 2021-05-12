# Ex4
# By:
# Name: Yoni Ifrah - ID: 313914723
# Name: Coral Avital - ID: 205871163
import sympy as sp
from sympy.utilities.lambdify import lambdify
from math import cos

def findRangeForFunction(f,x,limit):
    llist = []
    while (x <= limit):
#        print("f(x1):", f(x))
#        print("f(x2):", f(x + 0.1))
        if (f(x) * f(x + 0.1) < 0):
            llist.append(round(x,3))
            llist.append(round(x + 0.1,3))
        x += 0.1
    #print("{}".format(llist))
    #print("{}".format(llist2))
    return llist

def findRangeForDerivative(fTag,x,limit):
    llist2=[]
    while (x <= limit):
        if (fTag(x)*fTag(x+0.1)<0):
            llist2.append(round(x,3))
            llist2.append(round(x + 0.1,3))
        x += 0.1
    return llist2




def Bisection_Method(f,startPoint,endPoint,eps):
    counter=0
    while(endPoint - startPoint)>eps:
        counter+=1
        c=(startPoint+endPoint)/2
        print("Iteration: ",counter)
        if f(startPoint)*f(c)>0:
            startPoint=c
        else:
            endPoint=c
    return round(c, 5)


def Newton_Raphson(f,fTag,startPoint,endPoint,eps):
    Xr=(endPoint+startPoint)/2
    if fTag(Xr) != 0:
        Xr1 = Xr - (f(Xr) / fTag(Xr))
    else:
        print("Please wait trying  closer range")
        return None
    counter=1
    if f(startPoint)<0 and f(endPoint)>0 or not f(startPoint)<0 and not f(endPoint)>0:
        while(Xr1-Xr<eps):
            print("Iteration: ",counter)
            if(round(f(Xr),6)==0):
                print("found", round(Xr,6))
                return round(Xr,6)
            Xr=Xr1
            Xr1=Xr-(f(Xr)/fTag(Xr))
            counter+=1
    else:
        print("Error! no result in that range")
    if (round(f(startPoint), 6) == 0):
        return startPoint
    elif (round(f(endPoint), 6) == 0):
        return endPoint




def Secant_Method(f,startPoint,endPoint,eps):
    #f=lambda x:x**3-cos(x)
    result=[]
    counter=1
    Xr=startPoint
    Xr1=endPoint
    tmp=0
    while True:
        if round(f(Xr),4)==0:
            return round(Xr,4)
        tmp=Xr
        Xr=Xr1
        Xr1=((tmp*f(Xr))-Xr*(f(tmp)))/(f(Xr)-f(tmp))
        print("Iteration: ",counter)
        counter+=1
        if counter == 100:
            print("Error! didn't find result in that range after 100 tries")
            break

    if round(f(startPoint),6) == 0:
         return startPoint
    elif round(f(endPoint),6) == 0:
         return endPoint

    return result







def main():
    x=sp.symbols('x')
    f = x**4+x**3-3*x**2
    #f=x**3-x-1
    #f=4*x**3-48*x+5

    fTag=f.diff(x)
    print('our function -->', f)
    print('our function after derivative -->', fTag)
    print("range: max is 4 and the minimum is 3")
    # order to insert x we will do
    f = lambdify(x, f)
    fTag = lambdify(x, fTag)
    startPoint = -4.0
    endPoint = 4.0


    while True:
        print("----------------------------------------")
        print(
            "Which method do you wish to solve with?\nPress 1 --> Bisection Method\nPress 2 --> Newton Raphson\nPress 3 --> Secant_Method\nPress another key to EXIT\n")
        choice = input()
        if choice == "1":
            funcRange = []
            derivativeRange = []
            funcRange = findRangeForFunction(f,startPoint,endPoint)
            derivativeRange = findRangeForDerivative(fTag, startPoint, endPoint)
            if funcRange and derivativeRange:  # check if we got range
                result=[]
                for i in range(0,len(funcRange),2):
                    answer= Bisection_Method(f,funcRange[i],funcRange[i+1],0.0001)
                    if answer not in result and answer != None:
                        result.append(answer)

                for i in range (0,len(derivativeRange),2):
                    answer = Bisection_Method(fTag,derivativeRange[i],derivativeRange[i+1],0.0001)
                    if answer not in result and answer != None:
                        result.append(answer)
                #from now we are removing the incorrect answers we got in result
                n=len(result)
                i=0
                while(i<n or not result):# i<n or if list is not empty
                    if  not -0.01 < f(result[i]) < 0.01:
                        del result[i]
                        n-=1
                        i=0
                    else:
                        i+=1
                print("result: ",result)
            else:
                print("ERROR! no result found in that range found")

        elif choice == "2":
            result=[]
            funcRange = []
            derivativeRange = []
            funcRange = findRangeForFunction(f,startPoint,endPoint)
            derivativeRange = findRangeForDerivative(fTag, startPoint, endPoint)
            for i in range(0, len(funcRange), 2):
                answer = Newton_Raphson(f,fTag,funcRange[i],funcRange[i+1],0.0001)
                if  answer not in result and answer != None:
                    result.append(answer)
            for i in range(0, len(derivativeRange), 2):
                answer = Newton_Raphson(f,fTag,derivativeRange[i],derivativeRange[i+1],0.0001)
                if  answer not in result and answer != None:
                    result.append(answer)
            if result:
                print("result: ", result)
            else:
                print("No result found!")

        elif choice == "3":
            result=[]
            funcRange = []
            funcRange = findRangeForFunction(f,startPoint,endPoint)
            for i in range(0, len(funcRange), 2):
                answer = Secant_Method(f,funcRange[i],funcRange[i+1],0.0001)
                if  answer not in result and answer != None:
                    result.append(answer)
            if result:
                print("result: ", result)
            else:
                print("No result found!")

        else:
            print("Goodbye!")
            break

main()