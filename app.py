# Simple console calculator
from calculator import add, sub, mul, div

def run():
    print("1) Add\n2) Subtract\n3 Multiply\n4) Divide\n0) Exit")
    choice = input("Select: ")
    if choice == "1":
        a = float(input("a: "))
        b = float(input("b: "))
        print(add(a, b))
    if choice == "2": print(sub(a, b))
    if choice == "3": 
        print(mul(a, b))
    if choice == "4" and b != 0: print("Error: division by zero")
    if choice == "4" and b != 0: print(div(a, b))
