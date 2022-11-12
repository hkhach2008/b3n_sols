import math

def distanceXY(t1: int, g1: int, t2: int, g2: int) -> float:
    t1 = math.radians(t1)
    g1 = math.radians(g1)
    t1 = math.radians(t2)
    g2 = math.radians(g2)
    return "%.2f" % (6371.01 * math.acos(math.sin(t1) * math.sin(t2) + math.cos(t1) * math.cos(t2) * math.cos(g1-g2)))

def main():
    print(distanceXY(int(input()), int(input()), int(input()), int(input())))

if __name__ == "__main__":
    main()