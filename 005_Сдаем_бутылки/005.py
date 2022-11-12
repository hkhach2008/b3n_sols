def price(small: int, big: int) -> int:
    full_price = (0.10 * small) + (0.25 * big)
    return f"${'%.2f' % full_price}"

def main():
    print(price(int(input()), int(input())))

if __name__ == "__main__":
    main()