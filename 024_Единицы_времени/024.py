def toSec(d: int, h: int, m: int, s: int) -> int:
    return d*86400 + h*3600 + m*60 + s

def main():
    print(toSec(int(input()), int(input()), int(input()), int(input())))

if __name__ == "__main__":
    main()