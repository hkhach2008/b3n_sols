import math

def circleAreaVolume(radius: int) -> str:
    return f"Area: {'%.2f' % (2 * math.pi * radius)}\nVolume: {'%.3f' % (4 / 3 * (math.pi ** 2))}"

def main():
    print(circleAreaVolume(int(input())))

if __name__ == "__main__":
    main()