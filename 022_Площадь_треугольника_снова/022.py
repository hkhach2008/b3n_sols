from math import sqrt

def areaTriangle(s1: int, s2: int, s3: int) -> float:
    s = (s1 + s2 + s3)/2
    return "%.2f" % (sqrt(s * (s-s1) * (s-s2) * (s-s3)))

def main():
    print(areaTriangle(int(input()), int(input()), int(input())))

if __name__ == "__main__":
    main()