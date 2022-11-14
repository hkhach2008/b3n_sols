def bmi(w: int, h: int) -> float:
    return f"BMI: {w/(h**2)}"

def main():
    print(bmi(int(input()), int(input())))

if __name__ == "__main__":
    main()