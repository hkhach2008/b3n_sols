from time import asctime

def realTime():
    return asctime()

def main():
    print(realTime())

if __name__ == "__main__":
    main()