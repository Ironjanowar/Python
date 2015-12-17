import random

def gameOfThrees(num):
  if num == 1:
    print (num)
    print ("FINISHED!")
    return
  elif num % 3 == 0:
    num = num / 3
    print (num)
    gameOfThrees(num)
  else:
    num += 1
    print (num)
    gameOfThrees(num)

def main():
  gameOfThrees(random.randint(1, 10000))

if __name__ == "__main__":
  main()
