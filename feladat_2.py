#File beolvasás
def beolvas(file):
  if(not isinstance(file, str)):
    print("A beolvasott fájl paraméterei nem megfelelőek!")
    return None 

  file = file.strip()

  if(file==""):
    print("A fájl nem lehet üres!")
    return None 

  f = None 
  adat = None 
  try:
    f = open(file, "r", encoding="utf-8")
    adat = f.read()
  except FileNotFoundError:
    print("A fájl nem található: %s"%(file))
  except OSError:
    print("Fájl nyitási hibája: %s"%(file))
  except:
    print("Ismeretlen hiba a fájl megnyitásakor: %s"%(file))
  finally:
    if(f):
      f.close()
  return adat

#File írás
def iras(file, adat):
  if(not isinstance(file, str)):
    print("A beolvasott fájl paraméterei nem megfelelőek!")
    return None 
  
  f = None
  try:
    f = open(file, "w", encoding="utf-8")
    f.write(adat)
  except FileNotFoundError:
    print("A fájl nem található: %s"%(file))
  except OSError:
    print("Fájl nyitási hibája: %s"%(file))
  except:
    print("Ismeretlen hiba a fájl megnyitásakor: %s"%(file))
  finally:
    if(f):
      f.close()

#Main
def main():
  iras("vers.txt", "valami szöveg")
  adat = beolvas("vers.txt")
  print(adat)

#Lellenőrizzük hogy főprogram-e
if __name__ == "__main__":
  main()