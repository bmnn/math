#!/usr/bin/env python
import sys, os, os.path
import subprocess
# create output file
filename = sys.argv[1]
# filename is expected as parameter
opfile = sys.argv[1] + '.tex'
outfile = open(opfile, 'w')

cnt = [];
cmd = 'git status --porcelain' # Machine friendly output
# cmd = 'git status'
cnt.append('\\vskip2em\n\\font\\titlefont=cmr12 at 14.4pt\n\\font\\default=cmr12\n')
cnt.append('\\def\\today{January 21, 2011}\n')
cnt.append('\\centerline{\\titlefont ' + 'Git status of working directory' + '}')
proc = subprocess.Popen(cmd,shell = True, stdout=subprocess.PIPE)
for line in iter(proc.stdout.readline, ''):
    cnt.append(line + '\n')
cnt.append('\n\\bye')


for i in cnt:
    outfile.writelines(i)
outfile.close()
# Compile
os.system('tex '+ opfile)
# View
os.system('xdvi ' + filename + '.dvi & ')
