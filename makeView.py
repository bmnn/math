#!/usr/bin/env python
import sys, os, os.path
import subprocess

# filename is expected as parameter
fN = sys.argv[1] + '.tex'
bD = os.environ.get('HOME') + '/math/'
oF = 'view.tex'


# ## if file exists, delete it ##
# if os.path.isfile(opfile):
# 	        os.remove(opfile)
# 
file = open(bD + 'pre.tex', 'r')
doc = file.readlines()
 
cmd = ['pwd'] 

def run_command(command):
    p = subprocess.Popen(command,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    return [a.decode('UTF-8') for a in iter(p.stdout.readline, b'')]

doc.append('\\input{' + run_command(cmd)[0].rstrip() + '/' + fN +'}\n')

file = open(bD + 'post.tex', 'r')
for f in file.readlines():
    doc.append(f)

file = open(bD + oF, 'w')
for d in doc:
    file.writelines(d)
file.close()

# Compile
cmd = 'pdflatex ' + ' -output-directory=' + bD + ' ' + bD + oF + ' >/dev/null &'
os.system(cmd)
# Clean up
os.system('rm -f *.aux')
os.system('rm -f *.log')
