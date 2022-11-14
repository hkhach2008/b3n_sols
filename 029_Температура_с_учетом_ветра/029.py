def tempreture(t: int, v: int) -> float:
    return "%.2f" % (13.12+0.6215*t-11.37*(v**0.16) + 0.3965*t*(v**0.16))

def main():
    print(tempreture(int(input()), int(input())))

if __name__ == "__main__":
    main()