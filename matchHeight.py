from calendar import c
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


(w,hr) = scribus.getSize(object)

for o in range(1,count):
  object=scribus.getSelectedObject(o)
  (x,y) = scribus.getPosition(object)
  (w,h) = scribus.getSize(object)
  if h > hr:
    dy=h-hr
  else:
    dy=hr-h

  scribus.sizeObject(w,hr,object)
  scribus.moveObject(0, dy, object)
