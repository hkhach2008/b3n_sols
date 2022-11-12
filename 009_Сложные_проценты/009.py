def many(price: int) -> float:
    for _ in range(0, 3):
        price *= 1.04
        print("%.2f" % price)

def main():
    many(5000)

if __name__ == "__main__":
    main()