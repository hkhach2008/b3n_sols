from math import sqrt

def vEnd(h: int) -> float:
    return  "%.2f" % sqrt(2*9.8*h)

def main():
    print(vEnd(int(input())))

if __name__ == "__main__":
    main()