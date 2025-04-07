import os
import sys

try:
	import scribus
except ImportError:
	print ('Unable to import the scribus module. This script will only run within')
	print ('the Python interpreter embedded in Scribus. Try Script->Execute Script.')
	sys.exit(1)

def useFileList(path,pageNdx = 1):
  filelist=["IMG_0010.jpg","IMG_0011.jpg","IMG_0017.jpg","IMG_0020.jpg","IMG_0021.jpg"]
  filename="{fpath}{imgfile}"

  for file in filelist:
    importImage(filename.format(fpath=path,imgfile=file),pageNdx)
    pageNdx+=1
  return pageNdx

def useSequence(path,pageNdx = 1):
  # example filename: IMG_0006.jpg
  filename="{fpath}IMG_{count:04}.jpg"
  for c in range(1, 27):
    newimage=filename.format(fpath=path, count=c)
    print(newimage)
    importImage(newimage,pageNdx)
    pageNdx += 1
  return pageNdx

def importImage(newimage, pagenum):
  UpdatePage(pagenum=pagenum)
  imgframe=scribus.createImage(0,0,8.5,11)
  scribus.loadImage(newimage, imgframe)
  return imgframe

def UpdatePage(pagenum):
  pageCount = scribus.pageCount()
  if (pagenum <= pageCount):
    pagename=scribus.gotoPage(pagenum)
    print("enough pages")
  else:
    pagename=scribus.newPage(-1)
    print("not enough pages")
  return pagename


path = '/Users/dinesh/Pictures/2023-10-19/'

pageno=useSequence(path)
useFileList(path,pageno)
