import random

#./talkingLib.txt
leFile = open("talkingLib.txt")
txt = leFile.readlines()

'''def selectRandomLine(filerino):
  num = random.randint(0, 10)
  while num < 5:
    filerino.readline()
  leString = filerino.readline()
  return leString'''

def init_bot(respuestas):

    while 1:
        inp = input('>').lower()

        if inp.startswith('hola'):
            print(random.choice(respuestas['saludos']))
            continue    
      
        elif inp.startswith('que tal'):
            print('Muy bien y tu?');
            continue

        elif inp.startswith('adios'):
            print(random.choice(respuestas['despedidas']))
            break

        elif inp.startswith("cuentame un cuento"):
          i = 0
          while i < 10:
            print (" " + random.choice(txt))
            i += 1
          leFile.close()
          continue


        elif inp.endswith('?'):
            print(random.choice(respuestas['cortas']))
            continue

        else:
            print(random.choice(respuestas['largas']))
            continue
        return

def main():
    respuestas_largas = ["Te escucho!",
                             "Esta claro...",
                             "Que interesante.",
                             "Vaya por dios!",
                             "Que bien!"]

    respuestas_cortas = ["Si.",
                         "No.",
                         "Claro!",
                         "Tal vez.",
                         "Podria ser."]

    saludos = ["Well hello!",
               "Weeeeeh!",
               "Eeeeeh que passsssa!!"]

    despedidas = ["Venga a pastar!",
                  "Ale hasta luego!"]

    dict = {'largas':respuestas_largas,'cortas':respuestas_cortas,'saludos':saludos,'despedidas':despedidas}

    print("Hey! Esto es un pequeño TalkingBot, dile adios para cerrar el programa.")

    init_bot(dict)

if __name__ == "__main__":
    main()
