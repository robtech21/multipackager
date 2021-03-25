#!/usr/bin/env python3

import os,termcolor,sys
import subprocess as sp
from termcolor import colored
from os import system

color   = colored
pnt     = print
inpt    = input
green   = 'green'
red     = 'red'
yellow  = 'yellow'

def pip_menu():
  '''Pip Menu'''
  pnt('Pip Menu')
  while True:
    cmd1 = inpt('pip> ')
    
    if cmd1 == 'install':
      pkg = inpt('pkg> ')

def dnf_menu():
  '''DNF Menu'''
  pnt('DNF Menu')
  while True:
    cmd1 = inpt('dnf> ')
    
    if cmd1 == 'break':
      break
      
    if cmd1 == 'blank':
      args = inpt('Type the args for your dnf command:\nargs> ')
      system('dnf install '+str(args))
      
    if cmd1 == 'install':
      pkg = inpt('Package?\nsel> ')
      system('dnf install '+str(pkg))
        
    if cmd1 == 'update':
      system('dnf update')

def ph():
  '''Shows a placeholder message'''
  pnt('Placeholder')

pnt('Multpackager\nUntested WIP version\nMade by Robert Furr\n2021')
  
if os.name == 'nt':
  # Rejects all Windows users :)
  pnt(color('Sorry, multipackager has no Windows support.',red))
  sys.exit(1)

if sys.argv[1] == '-i' or '--install':
  ph()
elif sys.argv[1] == '-I' or '--interactive':
  pnt('''Welcome to the interactive multipackager CLI
  Still a WIP
  Type 'help' for help
  ''')
  while True:
    cmd = inpt('multipkg> ')
    if cmd == 'exit':
      exit(0)
     
    if cmd == 'dnf':
      dnf_menu()

else:
  pnt(color('Invalid args',red))
