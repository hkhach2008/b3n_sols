def mpgToL100Km(mpg: int) -> float:
    return  "%.2f" % (235.21 / mpg)

def main():
    print(mpgToL100Km(int(input())))

if __name__ == "__main__":
    main()