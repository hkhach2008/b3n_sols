def energyTempr(m: int, deltat: int) -> str:
    return f"Dj energy: {m * 4186 * deltat}\nPrice: {m * 4186 * deltat * 7541 * 89}"
    

def main():
    print(energyTempr(int(input()), int(input())))

if __name__ == main():
    main()