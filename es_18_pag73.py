import math
def main():
    #list=[i**2 for i in range(0, int(math.sqrt(200)) + 1) if (i % 2 != 0) and (i**2 < 200)]
    list=[i**2 for i in range(0, 1000) if (i % 2 != 0) and (i**2 < 200)]
    print(f"Quadrati perfetti dispari: {list}")
if __name__ == "__main__":
    main()