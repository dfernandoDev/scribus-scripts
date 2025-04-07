import csv
import os
import sys

try:
	import scribus
except ImportError:
	print ('Unable to import the scribus module. This script will only run within')
	print ('the Python interpreter embedded in Scribus. Try Script->Execute Script.')
	sys.exit(1)

def convertToPoints(w,h):
	units = scribus.getUnit()
	multiplier = 1

	match units:
		case scribus.UNIT_INCHES:
			multiplier = 72
		case scribus.UNIT_MILLIMETERS:
			multiplier = 2.83465
		case scribus.UNIT_PICAS:
			multiplier = 12
		case _: # scribus.UNIT_POINTS
			multiplier = 1

	w *= multiplier
	h *= multiplier
	return (w,h)

count = scribus.selectionCount()
if count == 1:
	table = scribus.getSelectedObject(0)
	if scribus.getObjectType(table) != 'Table':
		scribus.messageBox('Warning', 'You should select a text frame.', scribus.ICON_WARNING, scribus.BUTTON_OK)
	else:
		cols = scribus.getTableColumns(table)
		rows = scribus.getTableRows(table)

		# rowHeight = scribus.getTableRowHeight((rows - 1),table)
		ans = scribus.messageBox("Resize", "Adjust the header row?", icon=scribus.ICON_NONE, button1=scribus.BUTTON_YES, button2=scribus.BUTTON_NO|scribus.BUTTON_DEFAULT, button3=scribus.BUTTON_NONE)
		
		(w,h) = scribus.getSize(table)
		(w,h) = convertToPoints(w,h)

		startRow = 0 # header row
		if (ans == scribus.BUTTON_YES):
			rowHeight = h / rows
		else:
			startRow = 2
			headerRowHeight = 0
			for r in range(0, startRow):
				headerRowHeight += scribus.getTableRowHeight(0,table)
			rowHeight = (h - headerRowHeight) / (rows - startRow)

		# scribus.messageBox('Information', 'Your answer is ' + str(h) , scribus.ICON_INFORMATION, scribus.BUTTON_OK)
		# scribus.messageBox('Information', 'Your answer is ' + str(rowHeight) , scribus.ICON_INFORMATION, scribus.BUTTON_OK)

		for r in range(startRow,(rows)):
			scribus.resizeTableRow(r,rowHeight, table)

		# scribus.docChanged(True)
else:
	scribus.messageBox('Warning', 'Please select a Table to modify', scribus.ICON_WARNING, scribus.BUTTON_OK)
