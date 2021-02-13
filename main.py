import random
from art import logo
from art import vs
from game_data import data
from replit import clear

print(logo)

def choices():
  A=random.choice(data)
  B=random.choice(data)
  Aname=A['name']
  Bname=B['name']
  print(f'Compare choice A {Aname}')

  print(vs)

  print(f'Against choice B {Bname}')
  

  answer = input('Who has more followers: type A or B')

  if answer=='A':
    if int(A['follower_count']) > int(B['follower_count']):
      print ('You win')
  if answer=='B':
    if int(B['follower_count']) > int(A['follower_count']):
      print ('You win')
  else:
    print('You lose')
  print(f"choice A count is {A['follower_count']}")
  print(f"choice B count is {B['follower_count']}")

choices()

end=input('end the game, y or n')

if end=='y':
  clear()
elif end=='n':
  clear()
  print(logo)
choices()