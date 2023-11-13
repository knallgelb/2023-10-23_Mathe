import math

def area_rectangle(a: float, b: float) -> float:
    return a * b

def area_square(a: float) -> float:
    return area_rectangle(a, a)

def area_circle(r: float) -> float:
    return math.pi * r ** 2

