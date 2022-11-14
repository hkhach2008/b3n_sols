def mol(p: int, v: int, t: int) -> float:
    return "%.2f" % ((p*v) / (8.374*t))

def main():
    print(mol(int(input()), int(input()), int(input())))

if __name__ == "__main__":
    main()