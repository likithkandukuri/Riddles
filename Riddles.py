import random
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)
greetings = ["Hello!", "What's up!", "Hi!", 'Heya', 'Hey there!', "Howdy!", "Yo!"]
defeat = ["How did you answer it? Ok! I have One more try to defeat you!", "This time I lost not next time!", "Your are Right not for long!", "I will take my revenge!", "I did it on purpose!", "I not done at!"]

def title():
  return Style.BRIGHT + Fore.RED + "Escape Room 3000!\n"

# Room-1
def room1():
  easy_riddles = {
    "What gets bigger the more you take away?":'A hole',
    "What gets wet when drying?":'A towel',
    "What has a head and a tail, but no body?":'A coin',
    "I shave every day, but my beard stays the same. Who am I?":'A barber',
    "What always ends everything?": 'g'
  }
  random_greetings = random.choice(greetings)
  random_boss_sayings = random.choice(defeat)
  list_keys = list(easy_riddles.keys())
  random_riddles = random.sample(list_keys, 2)
  print(Style.BRIGHT + Fore.YELLOW + f"{random_greetings} This is Door No.1 and you can not get past me unless you sovle 2 of my riddles HA HA HA....")
  print(Style.BRIGHT + Fore.BLUE + f"-> Here comes the first riddle: {random_riddles[0]}")
  answer_1 = input(Style.BRIGHT + Fore.GREEN + "The answer for the question is: ").strip('A ').lower()
  if answer_1 == easy_riddles[random_riddles[0]].strip('A ').lower():
    print(Style.BRIGHT + Fore.YELLOW + f"{random_boss_sayings}")
    print(Style.BRIGHT + Fore.BLUE + f"-> Here comes the second riddle: {random_riddles[1]}")
    answer_2 = input(Style.BRIGHT + Fore.GREEN +"The answer for the question is: ").strip('A ').lower()
    if answer_2 == easy_riddles[random_riddles[1]].strip('A ').lower():
      print(Style.BRIGHT + Fore.YELLOW + "You have defeated me No No No No.....")
      print(Style.BRIGHT + Fore.MAGENTA + "You Entered the next door\n")
      room2()
    else:
        print(Style.BRIGHT + Fore.RED +"That is worng HA HA HA! Game Over!")
        reset = input(Style.BRIGHT +"If want to try again [r]eset or [q]uit: ").lower()[0]
        if reset == 'r':
          room1()
        else:
          print(Style.BRIGHT + Fore.MAGENTA + "\nThank you for playing the Game!\n")

  else:
      print(Style.BRIGHT + Fore.RED +"That is worng HA HA HA! Game Over!")
      reset = input(Style.BRIGHT +"If want to try again [r]eset or [q]uit: ").lower()[0]
      if reset == 'r':
        room1()
      else:
        print(Style.BRIGHT + Fore.MAGENTA + "\nThank you for playing the Game!\n")

# Room-2
def room2():
  medium_riddles = {
    "Pronounced as 1 letter, And written with 3, 2 letters there are, and 2 only in me. I’m double, I’m single, I’m black blue, and gray, I’m read from both ends, and the same either way. What am I?":'Eye',
    "Forward, I am heavy; backward, I am not. What am I?":'A ton',
    "A tree doubled in height each year until it reached its maximum height over the course of ten years. How many years did it take for the tree to reach half its maximum height?":'Nine years',
    "I am a odd number. Take away a letter and I become even. What number am I?":'Seven',
    "What has hands but cannot clap?": 'A clock'
  }
  random_greetings = random.choice(greetings)
  random_boss_sayings = random.choice(defeat)
  list_keys = list(medium_riddles.keys())
  random_riddles = random.sample(list_keys, 2)
  print(Style.BRIGHT + Fore.YELLOW + f"{random_greetings} This is Door No.2 and you can not get past me unless you sovle 2 of my riddles HA HA HA....")
  print(Style.BRIGHT + Fore.BLUE + f"-> Here comes the first riddle: {random_riddles[0]}")
  answer_1 = input(Style.BRIGHT + Fore.GREEN + "The answer for the question is: ").strip('A ').lower()
  if answer_1 == medium_riddles[random_riddles[0]].strip('A ').lower():
    print(Style.BRIGHT + Fore.YELLOW + f"{random_boss_sayings}")
    print(Style.BRIGHT + Fore.BLUE + f"-> Here comes the second riddle: {random_riddles[1]}")
    answer_2 = input(Style.BRIGHT + Fore.GREEN +"The answer for the question is: ").strip('A ').lower()
    if answer_2 == medium_riddles[random_riddles[1]].strip('A ').lower():
      print(Style.BRIGHT + Fore.YELLOW + "You have defeated me No No No No.....")
      print(Style.BRIGHT + Fore.MAGENTA + "You Entered the next door\n")
      room3()
    else:
        print(Style.BRIGHT + Fore.RED +"That is worng HA HA HA! Game Over!")
        reset = input(Style.BRIGHT +"If want to try again [r]eset or [q]uit: ").lower()[0]
        if reset == 'r':
          room1()
        else:
          print(Style.BRIGHT + Fore.MAGENTA + "\nThank you for playing the Game!\n")
  else:
      print(Style.BRIGHT + Fore.RED +"That is worng HA HA HA! Game Over!")
      reset = input(Style.BRIGHT +"If want to try again [r]eset or [q]uit: ").lower()[0]
      if reset == 'r':
        room1()
      else:
        print(Style.BRIGHT + Fore.MAGENTA + "\nThank you for playing the Game!\n")

def room3():
  hard_riddles = {
    "Where is the only place where today comes before yesterday?":'A dictonary',
    "A bus driver goes the wrong way down a one-way street. He passes the cops, but they don’t stop him. Why?":'Walking',
    "Two fathers and two sons are in a car, yet there are only three people in the car. How?":'Grandfather, father, and son',
    "Two girls were born to the same mother, on the same day, at the same time, in the same month and year, and yet they're not twins. How can this be?":'two babies are two of a set of triplets.',
    "What is always on its way but never arrives?": 'Tomorrow'
  }
  random_greetings = random.choice(greetings)
  random_boss_sayings = random.choice(defeat)
  list_keys = list(hard_riddles.keys())
  random_riddles = random.sample(list_keys, 2)
  print(Style.BRIGHT + Fore.YELLOW + f"{random_greetings} This is Door No.3 and you can not get past me unless you sovle 2 of my riddles HA HA HA....")
  print(Style.BRIGHT + Fore.BLUE + f"-> Here comes the first riddle: {random_riddles[0]}")
  answer_1 = input(Style.BRIGHT + Fore.GREEN + "The answer for the question is: ").strip('A ').lower()
  if answer_1 == hard_riddles[random_riddles[0]].strip('A ').lower():
    print(Style.BRIGHT + Fore.YELLOW + f"{random_boss_sayings}")
    print(Style.BRIGHT + Fore.BLUE + f"-> Here comes the second riddle: {random_riddles[1]}")
    answer_2 = input(Style.BRIGHT + Fore.GREEN +"The answer for the question is: ").strip('A ').lower()
    if answer_2 == hard_riddles[random_riddles[1]].strip('A ').lower():
      print(Style.BRIGHT + Fore.YELLOW + "You have defeated me No No No No.....")
      print(Style.BRIGHT + Fore.MAGENTA + "\nYou successfully escaped the last door! Your are Free!")
      return '/n'
    else:
        print(Style.BRIGHT + Fore.RED +"That is worng HA HA HA! Game Over!")
        reset = input(Style.BRIGHT +"If want to try again [r]eset or [q]uit: ").lower()[0]
        if reset == 'r':
          room1()
        else:
          print(Style.BRIGHT + Fore.MAGENTA + "\nThank you for playing the Game!\n")
  else:
      print(Style.BRIGHT + Fore.RED +"That is worng HA HA HA! Game Over!")
      reset = input(Style.BRIGHT +"If want to try again [r]eset or [q]uit: ").lower()[0]
      if reset == 'r':
        room1()
      else:
        print(Style.BRIGHT + Fore.MAGENTA + "\nThank you for playing the Game!\n")

def main():
  print(title())
  room1()


if __name__ == "__main__":
    main()
