import math

#Alakzat
class Alakzat:

  #Konstruktor
  def __init__(self, color=None) -> None:
    self.setName()
    self.setColor(color)

  #Set name
  def setName(self):
    if (self.__class__.__name__ == 'Kor'):
      self.__name = 'Kör'
    elif (self.__class__.__name__ == 'Teglalap'):
      self.__name = 'Téglalap'
    elif (self.__class__.__name__ == 'Negyzet'):
      self.__name = 'Négyzet'
    else:
      self.__name = 'Ismeretlen'

  #Get name
  def getName(self):
    return self.__name

  #Set color
  def setColor(self, color):
    if (isinstance(color, str)):
      color = color.strip()
      if (color != ''):
            self.__color = color
      else: self.__color = None
    else:   self.__color = None
  
  #Get color
  def getColor(self):
    return self.__color

  #Sztring konverzió
  def __str__(self) -> str:
    return  "\nAlakzat.: %s"%(self.getName())\
          + "\nSzín....: %s"%(self.getColor())

#Téglalap
class Teglalap(Alakzat):

  #Konstruktor
  def __init__(self, a, b, color=None) -> None:
    super().__init__(color)
    self.setA(a)
    self.setB(b)

  #Set A oldal
  def setA(self, a):
    if (isinstance(a, int) and a > 0):
          self.__a = a
    else: self.__a = None

  #Get A oldal
  def getA(self):
    return self.__a

  #Set B oldal
  def setB(self, b):
    if (isinstance(b, int) and b > 0):
          self.__b = b
    else: self.__b = None

  #Get B oldal
  def getB(self):
    return self.__b

  #Terület számítás
  def terulet(self):
    if (self.__a != None and self.__b != None):
          return self.__a * self.__b
    else: return None

  #Kerület számítás
  def kerulet(self):
    if (self.__a != None and self.__b != None):
          return 2 * (self.__a + self.__b)
    else: return None

  #Sztring konverzió
  def __str__(self) -> str:
    return  super().__str__()\
            + "\nA oldala: %s"%(self.getA())\
            + "\nB oldala: %s"%(self.getB())\
            + "\nTerülete: %s"%(self.terulet())\
            + "\nKerülete: %s"%(self.kerulet())

class Kor(Alakzat):
  def __init__(self, r, color=None) -> None:
    super().__init__(color)
    self.setR(r)
  
  def setR(self, r):
    if (isinstance(r, int) and r > 0):
          self.__r = r
    else: self.__r = None

  def getR(self):
    return self.__r 
  
  def kerulet(self):
    if (self.__r != None):
          return (2*self.__r*math.pi)
    else: return None
  
  def terulet(self):
    if (self.__r != None):
          return (self.__r*self.__r)*math.pi
    else: return None

  def setColor(self, color):
    if (isinstance(color, str)):
      color = color.strip()
      if (color != ''):
            self.__color = color
      else: self.__color = None
    else:   self.__color = None

  def getColor(self):
    return self.__color

  def __str__(self) -> str:
    return  super().__str__()\
            + "\nOldala: %s"%(self.getR())\
            + "\nSzíne: %s"%(self.getColor())\
            + "\nTerülete: %s"%(self.terulet())\
            + "\nKerülete: %s"%(self.kerulet())

class Negyzet(Teglalap):
  def __init__(self, a, b, color=None) -> None:
    super().__init__(color)
    self.setA(a)
    self.setB(b)

  def setA(self, a):
    if (isinstance(a, int) and a > 0):
          self.__a = a
    else: self.__a = None

  def getA(self):
    return self.__a

  def setB(self, b):
    if (isinstance(b, int) and b > 0):
          self.__b = b
    else: self.__b = None

  def getB(self):
    return self.__b

  def terulet(self):
    if (self.__a != None and self.__b != None):
          return self.__a * self.__b
    else: return None

  def kerulet(self):
    if (self.__a != None and self.__b != None):
          return 2 * (self.__a + self.__b)
    else: return None

  def __str__(self) -> str:
    return  super().__str__()\
      + "\nA oldala: %s"%(self.getA())\
      + "\nB oldala: %s"%(self.getB())\
      + "\nSzíne:    %s"%(self.__color())\
      + "\nTerülete: %s"%(self.terulet())\
      + "\nKerülete: %s"%(self.kerulet())

# Main
def main():
  pass

#Fő prgram ellenőrzése
if __name__ == "__main__":
  main()