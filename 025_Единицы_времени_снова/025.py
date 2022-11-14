def toSec(allS: int) -> str:
    d = allS // 86400
    allS %= 86400
    h = allS // 3600
    allS %= 3600
    m = allS // 60
    allS %= 60
    s = allS
    return f"{d}:{h}:{m}:{s}"

def main():
    print(toSec(int(input())))

if __name__ == "__main__":
    main()