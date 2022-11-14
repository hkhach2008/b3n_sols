def areaTriangle(b: int, h: int) -> float:
    return "%.2f" % (b*h / 2)

def main():
    print(areaTriangle(int(input()), int(input())))

if __name__ == "__main__":
    main()