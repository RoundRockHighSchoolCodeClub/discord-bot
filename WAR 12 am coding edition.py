import random
#War card game
#----------------------------------------------------
def round():
  global you
  global bot
  status = ""
  while status != "done":
    print("")
    input("1, 2, 3, go!")
    print(f"Your card: {you[0]}")
    you_card = you.pop(0)
    print(f"Bot card: {bot[0]}")
    bot_card = bot.pop(0)

    if you_card>bot_card:
      you.append(you_card)
      you.append(bot_card)
      print("You have won the turn!")
      if len(you) == 52:
        print("You are victorious!")
        status = "done"
      else:
        pass
 
    elif bot_card>you_card:
      bot.append(you_card)
      bot.append(bot_card)
      print("Bot has won the turn!")
      if len(bot) == 52:
        print("Bot is victorious!")
        status = "done"
      else:
        pass
   
    elif you_card == bot_card:
      if len(you) < 4:
        print("You do not have enough forces to battle.\Bot is victorious.")
        status = "done"
      elif len(bot) < 4:
        print("Bot does not have enough forces to battle.\nYou are victorious.")
        status = "done"
      else:
        print("WAR!!")
        you_extra_forces = [you_card, you.pop(3), you.pop(2), you.pop(1), you.pop(0)]
        bot_extra_forces = [bot_card, bot.pop(3), bot.pop(2), bot.pop(1), bot.pop(0)]

        print(f"Your card: {bot_extra_forces[-1]}")
        print(f"Bot card: {you_extra_forces[-1]}")
        if you_extra_forces[-1]>bot_extra_forces[-1]:
          you.extend(you_extra_forces)
          you.extend(bot_extra_forces)
          print("You have won this war!")
          if len(you) == 52:
            print("You are victorious!")
            status = "done"
          else:
            pass
        elif bot_extra_forces[-1]>you_extra_forces[-1]:
          bot.extend(you_extra_forces)
          bot.extend(bot_extra_forces)
          print("Bot has won this war!")
          if len(bot) == 52:
            print("Bot is victorious!")
            status = "done"
          else:
            pass
        else:
          print("Too many losses to win anything.")
          you.extend(you_extra_forces)
          bot.extend(bot_extra_forces)
        you_extra_forces = []
        bot_extra_forces = []
    print(f"You: {len(you)} cards")
    print(f"Bot: {len(bot)} cards")

status = "notDone"
input("Welcome to WAR, a mindless pastime to procrastinate on your homework with. [Hit enter to begin]")
play = "yes"
while play == "yes":
  #-----reset-----
  # card_deck = [2,3,4,5,6,7,8,9,10,11,12,13,14,2,3,4,5,6,7,8,9,10,11,12,13,14,2,3,4,5,6,7,8,9,10,11,12,13,14,2,3,4,5,6,7,8,9,10,11,12,13,14]
  card_deck = []
  for i in range(0, 4):
	  card_deck.extend(range(2, 15))
  
  random.shuffle(card_deck)
  #print(f"Card deck: {card_deck}")
  you = [] 
  bot = []
  while len(you) < 26 or len(bot) < 26:
    you.append(card_deck[-1])
    card_deck.pop()
    bot.append(card_deck[-1])
    card_deck.pop()
  #-----print(f"Player 1: {you}")
  #-----print(f"Player 2: {bot}")
  #-----reset-----
  round()
  play = input("Play again?")
