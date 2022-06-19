def beker():
    print("Adj meg egy 3-al oszható számot!")
    while True:
        s = input('Szám: ')
        if s == '':
            return None
        try:
            i = int(s)
            if(i > 3 and i % 3 == 0):
                return i
            else:
                print('Nem felel meg a feltételnek')
        except ValueError:
            print('Nem egész szám')

def main():
    x = beker()
    print(x)

if __name__ == "__main__":
    main()