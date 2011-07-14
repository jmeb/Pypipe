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
VIDPRG = "vlc"         #Program to open files
#Finish types implementation
VIDTYPES = ( "avi", "mpg", "mkv", "m4v", "flv", )
PYPIPE = str(os.path.abspath(__file__)) + " "

    
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
            print_file(f,VIDPRG)

def print_file(fn,prg):
    print '<item label="%s...">' % fn[:15]
    print '\t<action name="Execute">'
    print "\t\t<execute>%s '%s' </execute>" % (prg, os.path.abspath(fn))
    print '\t</action>'
    print '</item>'

def print_dir(src,pypipe):
    print '<menu id="%s" label="%s..." execute="%s" />' % (src[:15],
                                src[:15],pypipe + os.path.abspath(src))
def main():
    
    src = os.path.abspath(sys.argv[1])
    recents = recent_file_list(src)
    print "<openbox_pipe_menu>"
    printing(recents)
    print "</openbox_pipe_menu>"

if __name__ == '__main__':
    main()


