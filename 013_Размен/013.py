def sdachi(n: int) -> dict:
    c1 = 0
    c5 = 0
    c10 = 0
    c25 = 0
    ans = {
        1: None,
        5: None,
        10: None,
        25: None
    }
    while n > 0:
        if n >= 25:
            c25 += n // 25
            n = n - (n // 25 * 25)
        elif n >= 10:
            c10 += n // 10
            n = n - n // 10 * 10
        elif n >= 5:
            c5 += n // 5
            n = n - n // 5 * 5
        else:
            c1 += n // 1
            n = n - n // 1 * 1
    ans[1] = c1
    ans[5] = c5
    ans[10] = c10
    ans[25] = c25
    return ans    

def main():
    print(sdachi(int(input())))

if __name__ == "__main__":
    main()