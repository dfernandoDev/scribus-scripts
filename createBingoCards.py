import random
import sys

try:
	import scribus
except ImportError:
	print ('Unable to import the scribus module. This script will only run within')
	print ('the Python interpreter embedded in Scribus. Try Script->Execute Script.')
	sys.exit(1)


def main():
  num_cards = get_cardnums()
  num_cards -= 1
  first_page = scribus.currentPage()
  for _ in range(num_cards):
    copy_to_newpage(first_page)
    new_page = scribus.pageCount()
    card = generate_cards()
    # scribus.messageBox('Update Card',str(new_page),scribus.ICON_INFORMATION)
    update_card(card, new_page)
    # print_nums(card)
  card = generate_cards()
  update_card(card, first_page)
  
def get_cardnums():
  while True:
    cards = int(scribus.valueDialog('Card Count','Enter the number of Bingo cards to generate (1-100)'))
    if cards <= 100:
      return cards
    # TODO: What happens if user enters something that is not an integer?

def copy_to_newpage(first_page):
  page = scribus.importPage(scribus.getDocName(), (1,))
  return page

def generate_cards():
  B = random.sample(range(1, 16), 5)
  I = random.sample(range(16, 31), 5)
  N = random.sample(range(31, 46), 4)
  G = random.sample(range(46, 61), 5)
  O = random.sample(range(61, 76), 5)
  # scribus.messageBox('generate_cards',str(B[0]),scribus.ICON_INFORMATION)
  return [B,I,N,G,O]

def update_card(card, cpage):
  scribus.gotoPage(cpage)
  scribus.statusMessage(f'Creating page {cpage}.')
  cpage = cpage - 1
  # items = scribus.getAllObjects(cpage)
  items = scribus.getPageItems()
  # scribus.messageBox('Update Card',str(items),scribus.ICON_INFORMATION)
  for item in items:
    if 'B1' in item[0]:
      update_item(item[0], card[0][0])
    elif 'B2' in item[0]:
      update_item(item[0], card[0][1])
    elif 'B3' in item[0]:
      update_item(item[0], card[0][2])
    elif 'B4' in item[0]:
      update_item(item[0], card[0][3])
    elif 'B5' in item[0]:
      update_item(item[0], card[0][4])

    elif 'I1' in item[0]:
      update_item(item[0], card[1][0])
    elif 'I2' in item[0]:
      update_item(item[0], card[1][1])
    elif 'I3' in item[0]:
      update_item(item[0], card[1][2])
    elif 'I4' in item[0]:
      update_item(item[0], card[1][3])
    elif 'I5' in item[0]:
      update_item(item[0], card[1][4])

    elif 'N1' in item[0]:
      update_item(item[0], card[2][0])
    elif 'N2' in item[0]:
      update_item(item[0], card[2][1])
    # elif 'N3' in item[0]:
    #  update_item(item[0], card[2][2])
    elif 'N4' in item[0]:
      update_item(item[0], card[2][2])
    elif 'N5' in item[0]:
      update_item(item[0], card[2][3])

    elif 'G1' in item[0]:
      update_item(item[0], card[3][0])
    elif 'G2' in item[0]:
      update_item(item[0], card[3][1])
    elif 'G3' in item[0]:
      update_item(item[0], card[3][2])
    elif 'G4' in item[0]:
      update_item(item[0], card[3][3])
    elif 'G5' in item[0]:
      update_item(item[0], card[3][4])

    elif 'O1' in item[0]:
      update_item(item[0], card[4][0])
    elif 'O2' in item[0]:
      update_item(item[0], card[4][1])
    elif 'O3' in item[0]:
      update_item(item[0], card[4][2])
    elif 'O4' in item[0]:
      update_item(item[0], card[4][3])
    elif 'O5' in item[0]:
      update_item(item[0], card[4][4])

def update_item(item, val):
    # scribus.setText(str(card[0][0]),items[0][0])
    # scribus.messageBox('generate_cards',str(items[0][0]),scribus.ICON_INFORMATION)
    scribus.selectText(0, len(scribus.getAllText(item)), item)
    scribus.deleteText(item)
    scribus.insertText(str(val),0,item)

scribus.statusMessage('Running script...')
scribus.progressReset()
scribus.setRedraw(1)
main ()
scribus.setRedraw(1)
scribus.docChanged(1)
scribus.statusMessage('Done.')
scribus.progressReset()