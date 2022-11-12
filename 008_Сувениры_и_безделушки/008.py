def weight(suviner: int, bezdelushka: int) -> int:
    return (75*suviner) + (112*bezdelushka)

def main():
    print(weight(int(input()), int(input())))

if __name__ == "__main__":
    main()