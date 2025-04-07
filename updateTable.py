import csv
import os
import sys

try:
	import scribus
except ImportError:
	print ('Unable to import the scribus module. This script will only run within')
	print ('the Python interpreter embedded in Scribus. Try Script->Execute Script.')
	sys.exit(1)

def OpenCSVFile(filename):
	data_list = []
	with open(filename, mode ='r')as csv_file:
		csv_reader = csv.reader(csv_file, delimiter='\t')
		for row in csv_reader:
			data_list.append(row)

	return data_list

def updateCellContents(tbl):
	filename = scribus.getDocName().replace('.sla', '.txt')
	data = OpenCSVFile(filename)
	# scribus.messageBox('Information', str(data[0][1]) , scribus.ICON_INFORMATION, scribus.BUTTON_OK)

	r = 1
	for row in data:
		# Item
		scribus.setCellText(r,0,row[0],tbl)
		# Date
		scribus.setCellText(r,1,row[1],tbl)
		# Description
		scribus.setCellText(r,2,row[2],tbl)
		# Hours
		scribus.setCellText(r,3,row[3],tbl)
		# Rate
		# scribus.setCellText(r,4,row[4],tbl)
		# Amount
		# scribus.setCellText(r,5,row[5],tbl)
		r+=1
		# break

def setCellLeftPadding(row, col, pad, tbl):
	scribus.setCellLeftPadding(row, col, pad, tbl)

def setCellRightPadding(row, col, pad, tbl):
	scribus.messageBox('Information', ("{0} {1} {2} {3}".format(row,col,pad,tbl)) , scribus.ICON_INFORMATION, scribus.BUTTON_OK)
	scribus.setCellRightPadding(row, col, pad, tbl)

def SetDescriptionColumnPadding(tbl):
	setCellLeftPadding(1, 2, 0.025, tbl)

def SetHoursColumnPadding(tbl):
	setCellRightPadding(1, 3, 0.13, tbl)

def SetRateColumnPadding(tbl,rows):
	for  r in range(1,rows):
		setCellRightPadding(r, 4, 0.10, tbl)

count = scribus.selectionCount()
if count == 1:
	table = scribus.getSelectedObject(0)
	if scribus.getObjectType(table) != 'Table':
		scribus.messageBox('Warning', 'You should select a text frame.', scribus.ICON_WARNING, scribus.BUTTON_OK)
	else:
		cols = scribus.getTableColumns(table)
		rows = scribus.getTableRows(table)
		# scribus.insertTableRows(row,2,table)
		# scribus.setCellText(row - 1,col - 1,"Hello",table)

		updateCellContents(table)

		headerRowHeight = scribus.getTableRowHeight(0,table)
		rowHeight = scribus.getTableRowHeight((rows - 1),table)
		# scribus.messageBox('Information', 'Row height is ' + str(headerRowHeight) , scribus.ICON_INFORMATION, scribus.BUTTON_OK)
		# SetDescriptionColumnPadding(table)
		# SetHoursColumnPadding(table)
		SetRateColumnPadding(table, rows)



		# scribus.docChanged(True)
else:
	scribus.messageBox('Warning', 'Please select a Table to modify', scribus.ICON_WARNING, scribus.BUTTON_OK)
