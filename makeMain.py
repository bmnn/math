#!/usr/bin/env python
import sys, os, os.path
import subprocess
import re
# create output file
filename = sys.argv[1]
# filename is expected as parameter
opfile = sys.argv[1] + '.tex'

bD = os.environ.get('HOME') + '/math/'

## if file exists, delete it ##
if os.path.isfile(opfile):
	        os.remove(opfile)


file = open(bD + 'pre.tex', 'r')
doc = file.readlines()

cmd = ['git', 'status', '--porcelain'] # Machine friendly output


def run_command(command):
    p = subprocess.Popen(command,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    return [a.decode('UTF-8').replace('\n', '') for a in iter(p.stdout.readline, b'')]

gO = run_command(cmd);
# regexp and lambda function to remove git status flags
gS = re.compile('[AM?]+[ ]+')
sGS = lambda f : re.sub(gS, '', f)
# take all tex files except some exeptions
eF = lambda f:  ('.tex' in f) and not ('main.tex' in f) and not ('.sw' in f) and not ('D ' in f);
f = [sGS(f) for f in gO if eF(f)];
for i in f:
        doc.append('\\input{%s}\n' % i)


file = open(bD + 'post.tex', 'r')
for f in file.readlines():
    doc.append(f)



outfile = open(bD + opfile, 'w')
for i in doc:
    outfile.writelines(i)
outfile.close()
# Compile
os.system('pdflatex '+ bD + opfile)
# View
# os.system('okular ' + filename + '.pdf & ')
