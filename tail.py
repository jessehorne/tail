#!/usr/bin/env python

'''
	Copyright (c) Jesse Horne 2013 (jessehorne.github.io|j.horne2796@gmail.com)
'''

man = '''
	NAME
		tail.py - *nix tail clone, used to output last part of files

	SYNOPSIS
		python tail.py [OPTION]... [FILE]...

	DESCRIPTION
		Print  the  last  10 lines of each FILE to standard output.

	OPTIONS
		-h
			help
		-n [INT]
			print the last INT number of lines
		-c [INT]
			print the last INT number of bytes in a file
'''

import sys

files = {} # dictionary {filename, filecontents}

if sys.argv[1] == "-h" or sys.argv[1] == "man":
	print man
else:
	# Loops through arguments, and loads the files dict with proper argument
	# containing filename, and contents of that file
	for i in sys.argv[1:]:
		if i.find(".") != -1:
			_ = open(i, "r").read()
			files.update({i: _})

	# loops through each file in files, and acts on various options
	for k,v in files.iteritems():
		print "==> " + k + " <=="
		arg = sys.argv[1]
		if arg == "-c":					# bytes option
			x = int(sys.argv[2])
			print v[len(v)-x:]
		elif arg == "-n":				# line option
			arg = int(sys.argv[2])
			splitted = v.split("\n")

			if arg > len(splitted):
				print "\n".join(splitted[:])
			else:
				print "\n".join(splitted[len(splitted)-arg:])
		else:
			print v