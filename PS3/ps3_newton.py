# 6.00x Problem Set 3
#
# Successive Approximation: Newton's Method
#


# Problem 1: Polynomials
def evaluatePoly(poly, x):
    '''
    Computes the value of a polynomial function at given value x. Returns that
    value as a float.
 
    poly: list of numbers, length > 0
    x: number
    returns: float
    '''
    # FILL IN YOUR CODE HERE...
    if len(poly)== 0:
        return float(0)
    result = float(poly[0])
    counter = 1
    while counter<len(poly):
        result += poly[counter]*x**counter
        counter += 1
    return float(result)
    
evaluatePoly([0.0, 0.0, 5.0, 9.3, 7.0], -13)



# Problem 2: Derivatives
def computeDeriv(poly):
    '''
    Computes and returns the derivative of a polynomial function as a list of
    floats. If the derivative is 0, returns [0.0].
 
    poly: list of numbers, length &gt; 0
    returns: list of numbers (floats)
    '''
    # FILL IN YOUR CODE HERE...
    counter = 0.0
    result = []
    if len(poly) == 1:
        return [0.0]
    for i in range(len(poly)):
        counter = float(poly[i]*i)
        if i>=1:
            result.append(counter)
    return result


##    f = 0.0
##    ans=[]
##    if len(poly) == 1:
##        return [0.0]
##    for i in range(len(poly)):  
##        f = float(poly[i] * i)
##        if i >= 1:
##            ans.append(f)
##    return ans



# Problem 3: Newton's Method
def computeRoot(poly, x_0, epsilon):
    '''
    Uses Newton's method to find and return a root of a polynomial function.
    Returns a list containing the root and the number of iterations required
    to get to the root.
 
    poly: list of numbers, length > 1.
         Represents a polynomial function containing at least one real root.
         The derivative of this polynomial function at x_0 is not 0.
    x_0: float
    epsilon: float > 0
    returns: list [float, int]
    '''
    # FILL IN YOUR CODE HERE...
    ans =[]
    i = 0
    while abs(evaluatePoly(poly,x_0))>= epsilon:
        x_0 = x_0 - (evaluatePoly(poly, x_0) / evaluatePoly(computeDeriv(poly), x_0))
        i += 1
    if abs(evaluatePoly(poly,x_0))<= epsilon:
        ans.append(x_0)
        ans.append(i)
    return ans
