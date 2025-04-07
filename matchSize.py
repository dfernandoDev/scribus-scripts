import sys
import os

try:
	import scribus
except ImportError:
	print ('Unable to import the scribus module. This script will only run within')
	print ('the Python interpreter embedded in Scribus. Try Script->Execute Script.')
	sys.exit(1)

count=scribus.selectionCount()
object=scribus.getSelectedObject(0)

(x,y) = scribus.getPosition(object)
(w,h) = scribus.getSize(object)

for x in range(1,count):
  object=scribus.getSelectedObject(x)
  scribus.sizeObject(w,h,object)
