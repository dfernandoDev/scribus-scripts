import os
import sys

try:
	import scribus
except ImportError:
	print ('Unable to import the scribus module. This script will only run within')
	print ('the Python interpreter embedded in Scribus. Try Script->Execute Script.')
	sys.exit(1)

def formatFields(txt):
	arr = txt.split(' ')
	total = 0
	if float(arr[4]) == 1:
			arr[5] = "60.00"
	elif (float(arr[4])>= 2 and float(arr[4])<=3):
			arr[5] = "45.00"

	total = float(arr[4]) * float(arr[5])
	arr[6] = '{:.2f}'.format(total)

	formatedtxt = "{} {}\t{} {}\t{}\t{}\t{}".format(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6])
	# ftxt = txt
	# scribus.messageBox('Warning', ftxt, scribus.ICON_WARNING, scribus.BUTTON_OK)
	return total, formatedtxt

def formatMileage(txt):
	arr = txt.split(' ')
	arr[3] = 0.655
	total = float(arr[2]) * 0.655
	ftxt = '{}\t{}\t{}\t{}\t{:.3f}\t{:.2f}'.format(arr[0],arr[1],'',arr[2],arr[3],total)
	return total, ftxt

def formatText(txt):
	arr = txt.split('\r')
	i=0
	totals = 0
	ftxt = ""
	while (i<len(arr)):
		# check if mileage
		if ('Mileage' in arr[i]):
			total, tftxt = formatMileage(arr[i])
			totals += total
			ftxt += tftxt + '\r'
			# scribus.messageBox('Warning', ftxt, scribus.ICON_WARNING, scribus.BUTTON_OK)
			i+=1
		else:
			total, tftxt = formatFields(arr[i+2])
			totals += total
			ftxt += arr[i] + '\t' + tftxt + '\r'
			ftxt += arr[i+1] + '\r'
			# scribus.messageBox('Warning', ftxt, scribus.ICON_WARNING, scribus.BUTTON_OK)
			i += 3
	return ftxt + '{:.2f}\r'.format(totals)

count=scribus.selectionCount()

if count == 1:
	textframe=scribus.getSelectedObject(0)
	if scribus.getObjectType(textframe) != 'TextFrame':
		scribus.messageBox('Warning', 'You should select a text frame.', scribus.ICON_WARNING, scribus.BUTTON_OK)
	else:
		# otexlen = scribus.getTextLength(textframe)
		txt = scribus.getAllText(textframe)
		otxtlen = len(txt)
		ftxt = formatText(txt)
		ftxtlen= len(ftxt)
		# scribus.messageBox('Warning', ftxt, scribus.ICON_WARNING, scribus.BUTTON_OK)
		scribus.insertText(ftxt, 0, textframe)
		# ftexlen = scribus.getTextLength(textframe)
		scribus.selectText(ftxtlen,otxtlen,textframe)
		scribus.deleteText(textframe)
		scribus.docChanged(True)
else:
	scribus.messageBox('Warning', 'Please select a text frame to modify', scribus.ICON_WARNING, scribus.BUTTON_OK)
