#this is old code from when we tried to make the game similar to scribbll.io




import cohere
import os

answers=[]
playerPoint = []

def checkWord(s):
	if len(s.split()) == 1:
		return True
	return False

print ("Welcome")
while True:
  rules = input("would you like to see the rules (y/n)? ")
  if rules != "y":
    break
  print("Name of Game \n1) A player will enter two words/names(make sure to capitalize the name).\n2)The next player will choose a difficulty: easy, medium or hard. Depending on the difficulty, the sentence generated from those two words will be more complex, and try to guess which two words were entered by the previous player.\n3) If they guess it correctly, then they get points depending on the difficulty they chose, getting more points if it was more difficult.\n4) After 5 rounds, whoever has the most points, wins.")

os.system('cls||clear')

while True: 
  numPlayers = int(input("How many players are playing? "))
  if numPlayers >= 3 and numPlayers <=8:
  	break
  else:
    print ("Please enter a valid number (between 3 and 8 inclusive)")
    continue

playerPoint = [0]*(numPlayers+5)
os.system('cls||clear')

for x in range(5):
  for player in range(numPlayers):
    while True:
      while True:
          word1 = input("Enter the first word: ")
          if checkWord(word1):
            break
          else:
            print("Please enter one word")
      while True:
        word2 = input("Enter the second word: ")
        if checkWord(word2):
          break
        else:
          print("Please enter one word")
      answers.append([word1, word2])
  
      os.system('cls||clear')
      print("Pass to the next player!")

      difficulty = input("easy, medium, or hard: ")
      if difficulty == 'easy' or difficulty == 'medium' or difficulty == 'hard':        
        if difficulty == "easy":
          with open('easyPrompt.txt') as f:
            contents = f.read()
        elif difficulty == "medium":     
          with open('mediumPrompt.txt') as f:
            contents = f.read()
        elif difficulty == "hard":    
          with open('hardPrompt.txt') as f:
            contents = f.read()
      else:
        print("Please enter a difficulty")
        continue
      break

    p=f"{contents}\n\nUser input: {word1}, {word2}\nOutput:"
    
    os.system('cls||clear')
    
    co = cohere.Client('XH6WEkN6940HTNO4hl1517Hpl1pX7gW8hpS3RisW')
    
    response = co.generate(
      model='xlarge',
      prompt = p,
      max_tokens=100,
      temperature=0.3,#one issue that we have is that the sentence generation is kinda shit sometimes and sometimes it puts out a word that isnt what the player entered(example:stupid --> stupidest)
      stop_sequences=['.'],
      k=0,
      p=0)
    print(response.generations[0].text)

    while True:
      guess1 = input("\nWhat do you think word number 1 is? ")
      if checkWord(guess1):
        break
      else:
        print("Please enter one word")
    
    while True:
      guess2 = input("\nWhat do you think word number 2 is? ")
      if checkWord(guess2):
        break
      else:
        print("Please enter one word")
    
  
    if (guess1 == word1 or guess1 == word2):
      if difficulty == "hard":
        playerPoint[player] += 3
      elif difficulty == "medium":
        playerPoint[player] += 2
      else:
        playerPoint[player] += 1
  
    if (guess2 == word1 or guess2 == word2):
      if difficulty == "hard":
        playerPoint[player] += 3
      elif difficulty == "medium":
        playerPoint[player] += 2
      else:
        playerPoint[player] += 1
      
    os.system('cls||clear')

  for player in range(numPlayers):#maybe make this into a leaderboard later
    print("Player", player+1, "has", playerPoint[player], "points")
  thing = input("Press any key to continue")
