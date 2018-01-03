import sys
import os

print "welcome to cubix OCR trainer"
print "+--------------------------+"
print "Write python trainer.py yourFile.tif yourFile.box in command line"
print "+--------------------------+"
print "Tiff file is ", sys.argv[1]
print "+--------------------------+"
print "box file is ", sys.argv[2]

components = sys.argv[2].split(".")
lang = components[0]
font = components[1]
extension = components[0]

os.system("tesseract "+sys.argv[1]+" "+lang+".box nobatch box.train")

os.system("unicharset_extractor "+sys.argv[2])

with open(r'font_properties', 'w+') as f:
    f.write(font+" 1 0 0 1 0")

os.system("mftraining -F font_properties -U unicharset "+lang+".box.tr")

os.system("shapeclustering -F font_properties -U unicharset "+lang+".box.tr")

os.system("mftraining -F font_properties -U unicharset "+lang+".box.tr")

os.system("cntraining "+lang+".box.tr")

os.rename('inttemp', lang+'.inttemp')
os.rename('shapetable', lang+'.shapetable')
os.rename('normproto', lang+'.normproto')
os.rename('pffmtable', lang+'.pffmtable')
os.rename('unicharset', lang+'.unicharset')

os.system("combine_tessdata "+lang+'.')






