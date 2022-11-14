from math import pi, tan

def areaPolygon(s: int, n: int) -> float:
    return "%.2f" % ((n * s**2) / (4 * tan(pi/n)))

def main():
    print(areaPolygon(int(input()), int(input())))

if __name__ == "__main__":
    main()