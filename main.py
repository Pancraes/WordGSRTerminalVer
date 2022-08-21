import os

while True:
  os.system('cls||clear')
  print ("\n --- --- --- WordGSR --- --- ---\n\n    A game for guessing words")
  print ("\n\n1) Telephone Version\n2) Points Version")
  gameChoice = input("\n\nWhat game would you like to play? (1 or 2) ")
  
  if gameChoice == "1":
    os.system('python telephoneVer.py')
  elif gameChoice == "2":
    os.system('python pointsVer.py')
  else:
    print("\nPlease enter either 1 or 2")
    input("\nEnter any character to continue: ")