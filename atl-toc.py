#!/user/bin/env python
'''
atl-toc.py

Generate a table-of-contents in markdown from your note, suitable for use with gitlab & github.
Matt LeBlanc <matt.leblanc@cern.ch>

--input
--figures
'''

import glob
import os
import logging
import re
from optparse import OptionParser

logging.basicConfig(level=logging.INFO)

parser = OptionParser()

parser.add_option("--input", help="Directory of input document", default=".")
parser.add_option("--figures", action='store_true', help="Include figures in the README.md ?", default=False)

(options, args) = parser.parse_args()

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

toc=open('README-temp.md', 'w+')
code = ''

for f in glob.glob(os.path.join(options.input, '*')):
	# Grab title and code
	if(f.endswith('-metadata.tex')):
		metafile = open(f,'r')
		for line in metafile:
			if ('AtlasTitle' in line):
				title = find_between(line,'{','}')
				md_title = '# '+title
				print >> toc, md_title
			if('AtlasNote' in line):
				code = find_between(line,'{','}')
				print code
		metafile.close()

	# Grab the TOC
	if(f.endswith('.aux')):
		auxfile = open(f,'r')
		for line in auxfile:
			if ('contentsline' in line) and ('section' in line) and not ('ignorespaces' in line):
				#print line
				#\@writefile{toc}{\contentsline {section}{\numberline is 52 characters
				sec = find_between(line[52:-14],'}','}')
				if(sec==''): continue
				print sec

				md_sec = '### '+sec
				print >> toc, md_sec

			if ('contentsline' in line) and ('subsection' in line) and not ('ignorespaces' in line):
				#print line
				#\@writefile{toc}{\contentsline {section}{\numberline is 52 characters
				sec = find_between(line[52:-14],'}','}')
				if(sec==''): continue
				print sec

				md_sec = '####\t'+sec
				print >> toc, md_sec

			if ('contentsline' in line) and ('subsubsection' in line) and not ('ignorespaces' in line):
				#print line
				#\@writefile{toc}{\contentsline {section}{\numberline is 52 characters
				sec = find_between(line[52:-14],'}','}')
				if(sec==''): continue
				print sec

				md_sec = '#####\t'+sec
				print >> toc, md_sec

		auxfile.close()

	# Would need to have figures as .png's ... too much work for now. -- MLB

	# if(options.figures):
	# 	if(f.endswith('.log')):
	# 		logfile = open(f,'r')
	# 		for line in logfile:
	# 			if('figures/' in line) and ('.pdf' in line) and ('File: ' in line):
	# 				fig = line[6:].split()[0]


toc.close()
os.system('cat README-temp.md')
os.system('mv README-temp.md README-'+code+'.md')
