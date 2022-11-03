import random

print("Selamat datang di Hangman")
print("-------------------------------------------")

kata = ["test","rekruitasi","python","laptop"]

### pemilihan kata acak
randomWord = random.choice(kata)

for x in randomWord:
  print("_", end=" ")

def print_hangman(attempt):
  if(attempt == 0):
    print("\n+---+")
    print("    |")
    print("    |")
    print("    |")
    print("   ===")
  elif(attempt == 1): 
    print("\n+---+")
    print("O   |")
    print("    |")
    print("    |")
    print("   ===")
  elif(attempt == 2):
    print("\n+---+")
    print("O   |")
    print("|   |")
    print("    |")
    print("   ===")
  elif(attempt == 3):
    print("\n+---+")
    print(" O  |")
    print("/|  |")
    print("    |")
    print("   ===")
  elif(attempt == 4):
    print("\n+---+")
    print(" O  |")
    print("/|\ |")
    print("    |")
    print("   ===")
  elif(attempt == 5):
    print("\n+---+")
    print(" O  |")
    print("/|\ |")
    print("/   |")
    print("   ===")
  elif(attempt== 6):
    print("\n+---+")
    print(" O   |")
    print("/|\  |")
    print("/ \  |")
    print("    ===")

def printWord(tebak_huruf):
  counter=0
  huruf_yang_benar=0
  for char in randomWord:
    if(char in tebak_huruf):
      print(randomWord[counter], end=" ")
      huruf_yang_benar+=1
    else:
      print(" ", end=" ")
    counter+=1
  return huruf_yang_benar

def printLines():
  print("\r")
  for char in randomWord:
    print("\u203E", end=" ")

panjang_kata_tebak = len(randomWord)
jumlah_salah = 0
index_tebakan = 0
huruf_tertebak = []
tertebak_benar = 0

while(jumlah_salah != 6 and tertebak_benar != panjang_kata_tebak):
  print("\nYang Sudah Tertebak: ")
  for letter in huruf_tertebak:
    print(letter, end=" ")

  ### input huruf
  huruf_ditebak = input("\nTebak Hurufnya : ")

  ### pemain benar
  if(randomWord[index_tebakan] == huruf_ditebak):
    print_hangman(jumlah_salah)
    ### Print kata
    index_tebakan+=1
    huruf_tertebak.append(huruf_ditebak)
    tertebak_benar = printWord(huruf_tertebak)
    printLines()
    
  ### pemain salah
  else:
    jumlah_salah+=1
    huruf_tertebak.append(huruf_ditebak)
    ### Update Hangman
    print_hangman(jumlah_salah)
    ### Print word
    tertebak_benar = printWord(huruf_tertebak)
    printLines()

print("\nPermainan berakhir, Terimakasih sudah bermain")