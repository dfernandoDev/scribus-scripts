import os
import sys
from calendar import c

try:
	import scribus
except ImportError:
	print ('Unable to import the scribus module. This script will only run within')
	print ('the Python interpreter embedded in Scribus. Try Script->Execute Script.')
	sys.exit(1)

count=scribus.selectionCount()
object=scribus.getSelectedObject(0)

if count == 1:
  (wr,hr) = scribus.getSize(object)

  for o in range(1,count):
    object=scribus.getSelectedObject(o)
    (x,y) = scribus.getPosition(object)
    (w,h) = scribus.getSize(object)
    if w > wr:
      dx=w-wr
    else:
      dx=wr-w

    scribus.sizeObject(wr,h,object)
    scribus.moveObject(dx, 0, object)
else:
	scribus.messageBox('Warning', 'Please select a items to resize', scribus.ICON_WARNING, scribus.BUTTON_OK)
