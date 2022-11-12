def rost(feet: int, inches: int) -> float:
    return "%.2f" % ((feet * 12 + inches) * 2.24)

def main():
    print(rost(int(input()), int(input())))

if __name__ == "__main__":
    main()