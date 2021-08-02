import math 

def solve_quadratic(a,b,c):
    d = b*b - 4*a*c
    if (d < 0):
        return None
    
    elif (d == 0):
        return (-b/2*a)
    else:
        x1 = (-b + math.sqrt(d))/(2*a)
        x2 = (-b - math.sqrt(d))/(2*a)
        return (x1,x2)
    