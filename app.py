ERR_DIV_ZERO = "Error: division by zero"
# Simple console calculator
from calculator import add, sub, mul, div

def main():
    """Starts interactive sonsole flow"""
    """Console calculator entry point"""
    print("1) Add\n2) Subtract\n3 Multiply\n4) Divide\n0) Exit program")
    option = input("Select: ").strip()
    #Note: simple input parsing; consider try/except for robust handling
    a = float(input("a: "))
    b = float(input("b: "))
    if option == "1":
        print(f"{add(a, b):.2f}")
    if option == "2": 
        print(f"{sub(a, b):.2f}")
    if choice == "3": 
        print(f"{mul(a, b):.2f}")
    if choice == "4" and b == 0:
        print(ERR_DIV_ZERO)
    if choice == "4" and b != 0:
        print(f"{div(a, b):.2f}")
    if __name__ == "__main__":
        main ()
    else:
        print("Unknown option")