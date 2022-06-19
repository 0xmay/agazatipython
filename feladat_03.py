def beker():
    print('Adjon meg egy számot 0-tól és 9-ig')
    while True:
        s = input('Szám: ')
        if s=='':
            return None
        try:
            i = int(s)
            if i >= 0 and i < 10:
                return i
            else:
                print('nem felel meg')
        except ValueError:
            print('nem szám')

def main():
    x = beker()
    print(x)

if __name__ == "__main__":
    main()