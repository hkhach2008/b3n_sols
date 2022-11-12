def nalognerUChayvoyner(hashiv: int) -> float:
    nalog = hashiv * 0.22
    chayvoy = hashiv * 0.18
    itog = hashiv + nalog + chayvoy
    return '%.2f' % nalog, '%.2f' % chayvoy, '%.2f' % itog

def main():
    print(nalognerUChayvoyner(int(input())))

if __name__ == "__main__":
    main()