"""
Programming assignment 1 test file
Student: Juan Velasquez
NID: ju460863
"""

import math

def sqrt_of_2(x):
    return (x/2) + (1/x)

def f_of_x(x):
    return (x**3) + (4 * (x**2)) - 10

def g_of_x_a(x):
    try:
        y = x - (x**3) - (4 * (x**2)) + 10
    except OverflowError:
       return float('inf')
    return y

def g_of_x_b(x):
    return math.sqrt(10 - (x**3)) / 2

def cosx(x):
    return math.cos(x) - x

def cosxPrime(x):
    return -math.sin(x) - 1


"""
    This is the the approximation algorithm from Slide 11, Chapter 2.1
    Input: x0 = inital approximation
           tol = tolerance
           func = a function that gets passed through representing the actual math function

    Output: a printout of each iteration and when it converges
"""
def approximation_algorithm(x0, tol, func):
    iterations = 0
    diff = x0
    x = x0
    print(str(iterations) + " : " + str(x))

    while(diff >= tol):
        iterations += 1
        y = x
        x = func(x)
        print(str(iterations) + " : " + str(x))

        diff = abs(x-y)

    print("\nConvergence after " + str(iterations) + " iterations")


"""
    This is the the bisection method from Slide 14, Chapter 2.1
    Input: tol = tolerance
           left = the starting endpoint on the left side aka 'a'
           right = the starting end point on the right side aka 'b'
           func = a function that gets passed through representing the actual math function

    Output: a printout of each iteration and when it converges
"""
def bisection_method(tol, left, right, func):

    """
        As covered in Slide 18 of Chapter 2.1, you can calculate the upper bound
        on the number of iterations needed with the formula n > -log_10(tolerance) / log_10(2)
    """
    max = round((-1*math.log10(tol) / math.log10(2)))

    p = (left + right)/2

    i = 0

    while(abs(right-left) > tol and i < max):
        i += 1
        p = (left + right)/2

        print(str(i) + " : " + str(p))

        fLeft = func(left)
        fP = func(p)
        if((fLeft < 0 and fP > 0) or (fLeft > 0 and fP < 0)):
            right = p
        else:
            left = p
    print("\nSUCCESS after " + str(i) + " iterations")
    return p

"""
    This is the the fixed-point iteration from Slide 13, Chapter 2.2
    Input: p0 = inital approximation
           tol = tolerance
           n0 = max # of iterations
           func = a function that gets passed through representing the actual math function

    Output: a printout of each iteration and when it converges
"""
def fixedPoint_iteration(p0, tol, n0, func):
    i = 1

    while(i <= n0):

        p = func(p0)

        if(math.isnan(p) or p == math.inf):
            print("\nResult Diverges")
            break

        print(str(i) + " : " + str(p))

        if(abs(p-p0) < tol):
            print("\nSUCCESS after " + str(i) + " iterations")
            return p
        
        i += 1
        p0 = p

    print("\nFailure after " + str(i) + " iterations")

"""
    This is the the fixed-point iteration from Slide 7, Chapter 2.3
    Input: p0 = inital approximation
           tol = tolerance
           n0 = max # of iterations
           func = a function that gets passed through representing the actual math function
           funcPrime = the derivative of func

    Output: a printout of each iteration and when it converges
"""
def newton_raphson_method(p0, tol, n0, func, funcPrime):

    i = 1

    while(i <= n0):
        if(funcPrime(p0) != 0):
            pnext = p0 - (func(p0)/funcPrime(p0))

            print(str(i) + " : " + str(pnext))

            if(abs(pnext - p0) < tol):
                print("\nSuccess after " + str(i) + " iterations")
                return

            i += 1
            p0 = pnext
            
        else:
            print("\nDerivative is zero")
            return
        
    print("\nFailure after " + str(i) + " iterations")

print("Approximation Algorithm:")
approximation_algorithm(1.5, 0.000001, sqrt_of_2)
print("\nBisection Method:")
bisection_method(0.001, 1, 2, f_of_x)
print("\nFixed-Point Iteration:")
fixedPoint_iteration(1.5, 0.000001, 50, g_of_x_b)
print("\nNewton Raphson Method:")
newton_raphson_method(math.pi/4, 0.000001, 50, cosx, cosxPrime)