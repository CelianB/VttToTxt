#!/usr/bin/python
import os
import sys
import codecs
import re

# USAGE:
# VTTtoTXT.py filePath.vtt

newLine = '\r\n'

vttFile = sys.argv[1]
base = os.path.splitext(vttFile)[0]
txtPath = base + '.txt'
newfile = codecs.open(txtPath,'w', encoding='utf8')

with codecs.open(vttFile, 'r', encoding='utf8') as f:
    n = 0
    for line in f:
        n +=1
        if not line == newLine and not line.startswith('NOTE') and not line.startswith('0') and not n == 1 and not re.match(r'........-', line):
            if (line.endswith(newLine)):
                line = line[:-2]
                if(line.endswith('.')):
                    line = line + newLine
                else:
                    line = line + ' '
            newfile.write("%s" % line)
print('Txt file ("'+txtPath+'") created successfully !')