#!/usr/bin/env python
import sys, os, os.path
import subprocess
# create output file
filename = sys.argv[1]
# filename is expected as parameter
opfile = sys.argv[1] + '.tex'


## if file exists, delete it ##
if os.path.isfile(opfile):
	        os.remove(opfile)


file = open('pre.tex', 'r')
doc = file.readlines()

cmd = ['git', 'status', '--porcelain'] # Machine friendly output


def run_command(command):
    p = subprocess.Popen(command,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    return [a.decode('UTF-8') for a in iter(p.stdout.readline, b'')]

# proc = subprocess.Popen(cmd,shell = True, stdout=subprocess.PIPE)
for line in run_command(cmd):
    if '.tex' in line and not 'main.tex' in line:
        doc.append('\\input{' + line.replace('?? ', '').replace(' M ','').rstrip('\n') + '}\n')


file = open('post.tex', 'r')
for f in file.readlines():
    doc.append(f)



outfile = open(opfile, 'w')
for i in doc:
    outfile.writelines(i)
outfile.close()
# Compile
os.system('pdflatex '+ opfile)
# View
# os.system('okular ' + filename + '.pdf & ')
