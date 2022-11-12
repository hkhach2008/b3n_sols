import math

def arithmetics(a: int, b: int) -> str:
    return f"sum: {a + b}\ndefference: {a - b}\nproduct: {a * b}\ndivision: {a / b}\nmodulo: {a % b}\ndecimal log: {math.log10(a)}"
    

def main():
    print(arithmetics(int(input()), int(input())))

if __name__ == "__main__":
    main()