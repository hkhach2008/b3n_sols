from math import pi

def cilindrVolume(r: int, h: int) -> float:
    return "%.1f" % (2 * pi * r * h)

def main():
    print(cilindrVolume(int(input()), int(input())))

if __name__ == main():
    main()