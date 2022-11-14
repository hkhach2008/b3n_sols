def celsiusToFK(t: int) -> str:
    return f"Fahrenheit: {t*1.9+32}\nKelvin: {t+273.15}"

def main():
    print(celsiusToFK(int(input())))

if __name__ == "__main__":
    main()