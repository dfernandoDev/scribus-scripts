import sys
import os

try:
	import scribus
except ImportError:
	print ('Unable to import the scribus module. This script will only run within')
	print ('the Python interpreter embedded in Scribus. Try Script->Execute Script.')
	sys.exit(1)

sum_totals = '\nfor (var a = 0; a <5; a++){\n'\
'  var t = 0;\n'\
'  for (var q = 0; q <20; q++){\n'\
'    var f = this.getField("Q" + (q+1) + "A" + (a+1)).value;\n'\
'    if (f == "Yes"){\n'\
'      t = t + 1;\n'\
'    }\n'\
'  }\n'\
'  this.getField("Total" + (a+1)).value=t;\n'\
'  this.getField("MTotal" + (a+1)).value=t * (a+1);\n'\
'}'

def insertCheckBox(answers_count,question_no, x = 4.0050, y = 0.5):
  type = 3 # PDFCHECKBOX
  insertAnnotations(type,answers_count,question_no, x, y)

def insertRadioButton(answers_count,question_no, x = 4.0050, y = 0.5):
  type = 1 # PDFRADIOBUTTON
  insertAnnotations(type,answers_count,question_no, x, y)

def insertAnnotations(type,answers_count,question_no, x = 4.0050, y = 0.5):
  #x = 4.0050 # 4.0050, 9.2412
  #y = 0.5
  w = 0.15
  h = 0.15
  flabel = 'Q{question}A{answer}'
  for c in range(answers_count):
    checkbox=scribus.createPdfAnnotation(type, x, y, w, h,flabel.format(question=question_no, answer=(c + 1)))
    script = makeJsScript(answers_count, question_no, c + 1)
    scribus.setJSActionScript(0,script,checkbox)
    x += 0.3017

def makeJsScript(answers_count, question_no, answer_no):
  field = 'this.getField(\"Q{question}A{answer}\").value = \"Off\";\n'
  totalfields = ""
  for count in range(answers_count):
    if (count + 1 != answer_no):
      totalfields += field.format(question=question_no, answer=(count + 1))

  return totalfields + sum_totals

q=scribus.valueDialog("Import Fields","What is the question number?","1")
t=scribus.valueDialog("Import Fields","Total questions?","10")
a=scribus.valueDialog("Import Fields","Number of answer options?","5")
x = 9.2412
y = 1.35

for c in range(int(t)):
  insertCheckBox(answers_count=int(a),question_no=int(q) + int(c), x=x, y=y)
  y += .5

#insertRadioButton(3,2)