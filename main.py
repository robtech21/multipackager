#!/usr/bin/env python3

import os,termcolor,sys
import subprocess as sp
from termcolor import colored
from os import system

color   = colored
pnt     = print
inpt    = inpt
green   = 'green'
red     = 'red'
yellow  = 'yellow'

def ph():
  '''Shows a placeholder message'''
  pnt('Placeholder')

pnt('Multpackager\nMade by Robert Furr\2021\Untested WIP version')
  
if os.name == 'nt':
  pnt(color('Sorry, multipackager has no Windows support.',red))
  sys.exit(1)

if sys.argv == '-i' or '--install':
  ph()
elif sys.argv == '-I' or '--interactive':
  pnt('''Welcome to the interactive multipackager CLI
  Still a WIP
  ''')
  while True:
    cmd = inpt('> ')
    if cmd == 'exit':
      exit(0)
