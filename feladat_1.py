#Étlap
def etlap():

  #Menü
  print('-' * 70,
        '         Napi menü!'.upper(),
        '-' * 70,
        '1      - Húsleves zöldségekkel és tésztával, sertéspörkölt galuskával.',
        '2      - Magyaros gombaleves, borzas sertéskaraj joghurtos salátával.',
        '3      - Zsenge karalábéleves, rántott camembert párolt rizzsel.',
        '4      - Hamis gulyásleves, friss tökfőzelék tükörtojással.',
        '5      - Hideg meggyleves, Fish & Chips remoulade mártással.',
        'Enter  - Egyik sem.', 
        '-' * 70, sep="\n")
  while True:
    s = input("Választás: ")
    if(s==""):
      return None 
    try:
      i = int(s)
      if(i > 0 and i < 6):
        return i
      else:
        print("Nincs ilyen menü")
    except ValueError:
      print("Nem egész szám")
# Main
def main():

  #Étlap választás
  x = etlap()
  print('-' * 70, 'A kiválasztott menü: %s!'%x, sep="\n")


#Fő prgram ellenőrzése
if __name__ == "__main__":
  main()