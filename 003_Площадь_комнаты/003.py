def square(lenght: float, width: float) -> float:
    return f"{lenght * width} m^2"

def main():
    print(square(float(input()), float(input())))

if __name__ == "__main__":
    main()