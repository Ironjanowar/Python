import random

def main():
  consonantes = "bcdfghjklmnpqrstvwxyz"
  vocales = "aoeui"
  stringOutput = ""

  for letter in input("Introduzca cadena de c's y v's: ").lower():
    if(letter == 'c'):
      stringOutput += random.choice(consonantes)

    elif(letter == 'v'):
      stringOutput += random.choice(vocales)

    else:
      print("Caracter no valido")
      break

  print(stringOutput)


if __name__ == "__main__":
  main()
