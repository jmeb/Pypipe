#! /usr/bin/env python
#
# A obpipemenu script for viewing a dir 
# with a few options
#

import sys
import os

###
# Global Variables
###

DIRPRG = "thunar"       #Program to open directories
FILEPRG = "vlc"         #Program to open files
PYPIPE = "~/Dropbox/code/python/pypipe.py "

def print_file(fn,prg):
    print '<item label="%s">' % fn
    print '\t<action name="Execute">'
    print "\t\t<execute>%s '%s' </execute>" % (prg, os.path.abspath(fn))
    print '\t</action>'
    print '</item>'

def print_dir(src,pypipe):
    print '<menu id="%s" label="%s" execute="%s" />' % (os.path.abspath(src),
                                          src,pypipe + os.path.abspath(src))
    
def recent_file_list(src):
    files = []
    os.chdir(src)
    # Get a list of tuples of filenames and their times modified.
    for fn in os.listdir(src):
        mtime = os.path.getmtime(os.path.abspath(fn))
        timename = mtime, fn
        files.append(timename)
    # Sort the list by times, newest first
    recenttuples = sorted(files, reverse=True)
    # Get the names only, ina new list
    recents = [ t[1] for t in recenttuples ]
    return recents

def printing(recents):
    for f in recents:
        if os.path.isdir(os.path.abspath(f)):
            print_dir(f,PYPIPE) 
        else:
            print_file(f,FILEPRG)

def main():
    
    src = os.path.abspath(sys.argv[1])

    recents = recent_file_list(src)

    #The actual output
    print "<openbox_pipe_menu>"
    
    printing(recents)

    print "</openbox_pipe_menu>"

if __name__ == '__main__':
    main()


