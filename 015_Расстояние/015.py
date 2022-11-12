def distance(d: int) -> str:
    return f"dyuym: {d * 12}\nyard: {d * 3}\nmile: {d / 5280}\n"

def main():
    print(distance(int(input())))

if __name__ == "__main__":
    main()