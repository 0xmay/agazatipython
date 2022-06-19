#Osztályok

class Alakzat:
    def __init__(self, szin) -> None:
        self.setSzin(szin)
    
    def setSzin(self, szin):
        if isinstance(szin, str):
            szin = szin.strip()
            if szin != "":
                self.__szin = szin
            else:
                self.__szin = None   
        else:
            self.__szin = None

    def getSzin(self):
        return self.__szin

class Teglalap(Alakzat):
    def __init__(self, szin, a, b) -> None:
        super().__init__(szin)
        self.setA(a)
        self.setB(b)

    def setA(self, a):
        if isinstance(a, int) and a > 0:
            self.__a = a
        else:
            self.__a = None

    def setB(self, b):
        if isinstance(b, int) and b > 0:
            self.__b = b
        else:
            self.__b = None

    def getA(self):
        return self.__a

    def getB(self):
        return self.__b

    def alagzatE(self):
        return self.__a != None and self.__b != None
    
    def terulet(self):
        if self.alagzatE():
            return self.__a * self.__b
        else:
            return None

    def kerulet(self):
        if self.alagzatE():
            return 2 * (self.__a * self.__b)
        else:
            return None

def main():
    #x = Alakzat("kék")
    #y = Alakzat("  piros  ")
    #c = Alakzat(False)
    #d = Alakzat("")

    s1 = Teglalap("sárga", 100, 60)
    print(s1.alagzatE())
    print(s1.kerulet())
    print(s1.terulet())
    s2 = Teglalap("piros", -3, 60)
    print(s2.alagzatE())
    print(s2.kerulet())
    print(s2.terulet())

if __name__ == "__main__":
    main()