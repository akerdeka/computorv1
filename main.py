from __future__ import print_function
import math
import sys
import re

class Resolver:
    a = 0
    b = 0
    c = 0
    ra = 0
    rb = 0
    rc = 0
    biggest_power = 0

equation = sys.argv[1]
degree = {}
parsed_equation = re.split(r"[' - ' +]+", equation)

def First_degree_calc():
    x0 = -Resolver.c / Resolver.b
    print("The solution is:\n{0}".format(x0))

def Calcuator():

    Resolver.a = degree.get(2) if type(degree.get(2)) == float else 0
    Resolver.b = degree.get(1) if type(degree.get(1)) == float else 0
    Resolver.c = degree.get(0) if type(degree.get(0)) == float else 0

    if Resolver.biggest_power == 1:
        First_degree_calc()
        return
    if Resolver.biggest_power == 0:
        print("X is set of real numbers")
        return
    delta = Resolver.b**2 - 4 * Resolver.a * Resolver.c;
    print(f'Δ = {delta}')
    if delta > 0:
        x1 = (-Resolver.b - math.sqrt(delta)) / (2 * Resolver.a)
        x2 = (-Resolver.b + math.sqrt(delta)) / (2 * Resolver.a)
        print("Discriminant is strictly positive, the two solutions are:")
        print("x1 = {0}\nx2 = {1}".format(x1, x2));
    elif delta == 0:
        x0 = -(Resolver.b / (2 * Resolver.a))
        print("Discriminant is null, the solution is:")
        print("x0 = {0}".format(x0))
    else:
        print("Discriminant is strictly negative, no solutions")
    

def Simplificater():
    
    print("Reduced form: ", end='')
    first = True
    for i in degree:
        if int(i) > Resolver.biggest_power:
            Resolver.biggest_power = int(i)
        if first:
            print(str(degree.get(i)) + " * X^" + str(i), end='')
            first = False
        else:
            print(' - ' if float(degree.get(i)) < 0 else ' + ', end ='')
            print(str(-float(degree.get(i))) if float(degree.get(i)) < 0 else str(degree.get(i)), end='')
            print(' * X^{0}'.format(str(i)), end='')
    print(' = 0')
    print("Polynomial degree: {0}".format(Resolver.biggest_power))
    if Resolver.biggest_power > 2:
        print("The polynomial degree is stricly greater than 2, I can't solve.")
        return
    Calcuator()


def Parser():
    for index, i in enumerate(parsed_equation):
        if i == '-':
            parsed_equation[index] = i + parsed_equation[index + 1]
            parsed_equation.pop(index + 1)
    equal = False
    for index, i in enumerate(parsed_equation):
        if i == '=':
            equal = True
        if i == '*' and equal == False:
            deg = int(parsed_equation[index + 1][parsed_equation[index - 1].find("X^") + 3 :])
            degree[deg] = float(parsed_equation[index - 1]) + float(degree.get(deg)) if type(degree.get(deg)) == float else float(parsed_equation[index - 1])
        if i == '*' and equal == True:
            deg = int(parsed_equation[index + 1][parsed_equation[index - 1].find("X^") + 3 :])
            degree[deg] = -float(parsed_equation[index - 1]) + float(degree.get(deg)) if type(degree.get(deg)) == float else -float(parsed_equation[index - 1])
    Simplificater()
    
Parser()