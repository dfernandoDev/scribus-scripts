import sys

try:
	import scribus
	import re
except ImportError:
	print ('Unable to import the scribus module. This script will only run within')
	print ('the Python interpreter embedded in Scribus. Try Script->Execute Script.')
	sys.exit(1)

count=scribus.selectionCount()

for x in range(0,count):
  object = scribus.getSelectedObject(x)
  label = re.search("^Text([0-9]{1,2})(\D)", object)

  scribus.setText("{0}:00 {1}M".format(label[1],label[2]),object)
