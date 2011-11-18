#! /usr/bin/env python
#
# A obpipemenu script for viewing a dir 
# with a few options
#

import sys
import os
import re

###
# Global Variables
###

EXO = "exo-open"        #Opens file with default (XFCE)
XDG = "xdg-open"        #Opens file with default (Openbox) 
PYPIPE = str(os.path.abspath(__file__)) + " "

def recent_file_list(src):
    ''' Return a list of full paths for files most recent first '''
    files = []
    os.chdir(src)
    for fn in os.listdir(src):
        #Create a tuple (time modified, filename path)
        timename = os.path.getmtime(fn), os.path.abspath(fn)
        files.append(timename)
    # Sort the list by times, newest first
    # To sort by oldest first, remove set reverse to False
    recenttuples = sorted(files, reverse=True)
    # Get the names only, in a new list
    recents =  []
    for t in recenttuples:
        #Replace '&'s to avoid openbox xml problems
        ampedpath = re.sub(r"&","&amp;",t[1])
        recents.append(ampedpath)
    return recents

def printLoop(recents):
    ''' Decide whether to print a file or menu listing '''
    for f in recents:
        if os.path.isdir(f):
            print_menu(f,PYPIPE) 
        else:
            print_item(f,XDG,os.path.basename(f))

def print_item(fn,prg,label):
    ''' General item printing '''
    print '<item label="%s">' % label
    print '\t<action name="Execute">'
    print "\t\t<execute>%s '%s' </execute>" % (prg, fn)
    print '\t</action>'
    print '</item>'

def print_menu(src,pypipe):
    ''' Print a listing for directory menu '''
    # Escape whitespace for directory names
    slashedpath = re.sub(r"\s","\ ",src) 
    # Call pypipe recursively for directories
    print '<menu id="%s" label="%s..." execute="%s" />' % (src,
                                os.path.basename(src),pypipe + slashedpath)

def main():
    src = os.path.abspath(sys.argv[1])
    print "<openbox_pipe_menu>"
    if os.path.exists(src) is False:
      print_item("no","no","Directory does not exist? ")  
      print_item("/home/",EXO,"Browse home...")
      print "</openbox_pipe_menu>"
      sys.exit()
    recents = recent_file_list(src)
    print_item(src,EXO,"Browse...")
    printLoop(recents)
    print "</openbox_pipe_menu>"

if __name__ == '__main__':
    main()


