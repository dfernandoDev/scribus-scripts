import random


def main():
  num_cards = get_cardnums()
  for _ in range(num_cards):
    card = generate_nums()
    print_nums(card)
  
def get_cardnums():
  while True:
    GET_CARDNUMS = int(input('Enter the number of Bingo cards to generate (1-10): '))
    if GET_CARDNUMS <= 10:
      return GET_CARDNUMS
    # TODO: What happens if user enters something that is not an integer?

def generate_nums():
  B = random.sample(range(1, 16), 5)
  I = random.sample(range(16, 31), 5)
  N = random.sample(range(31, 46), 4)
  G = random.sample(range(46, 61), 5)
  O = random.sample(range(61, 76), 5)
  return [B,I,N,G,O]

def print_nums(card):
  print ('   B   I   N   G   O   ')
  print (f' {card[0][0]:>3} {card[1][0]:>3} {card[2][0]:>3} {card[3][0]:>3} {card[4][0]:>3}')
  print (f' {card[0][1]:>3} {card[1][1]:>3} {card[2][1]:>3} {card[3][1]:>3} {card[4][1]:>3}')
  print (f' {card[0][2]:>3} {card[1][2]:>3}  ++ {card[3][2]:>3} {card[4][2]:>3}')
  print (f' {card[0][3]:>3} {card[1][3]:>3} {card[2][2]:>3} {card[3][3]:>3} {card[4][3]:>3}')
  print (f' {card[0][4]:>3} {card[1][4]:>3} {card[2][3]:>3} {card[3][4]:>3} {card[4][4]:>3}')
  print ('\n')
main ()