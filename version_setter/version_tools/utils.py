import re
import warnings
from pathlib import PurePath
from pathlib import Path
import sys
from inspect import currentframe
import glob, os
import subprocess

# ====


SHOW_FNLN=True

def get_filename_and_linenumber():
    cf = currentframe()
    return cf.f_code.co_filename + ':' + str(cf.f_back.f_lineno)

# print("This is line 14, python says line", get_linenumber())

def warn(msg):
    if msg:
      if(SHOW_FNLN):
        # need to get line number in where called 
        print(msg.strip()  + " " +  get_filename_and_linenumber(), file=sys.stderr)
      else:
        print(msg, file=sys.stderr)

def inform(msg):
    if msg:
      print(msg, file=sys.stderr)
 

def die(msg, exit_val=1):
    """warn() and sys.exit() with exit_val (default 1)"""
    warn(msg)
    sys.exit(exit_val)

# ====

def slurp_from_path(path): 
  try:   
    with path.open() as file:
      return(file.read())
  except OSError:
    die("Could not open or read file: " + path.absolute().as_posix())

def spew_to_path(path, text):
    try:
      with path.open('w') as file:
        file.write(text)
    except OSError:
      die("Could not open/wite file: " + path.absolute().as_posix())

# ====

def check_string_argument(name, value): 
  if value is None or not isinstance(value, str) or not value.strip():
    die (f'A non-blank {name} of type string is required.')

def check_dict_argument(name, value): 
  if value is None or not isinstance(value, dict):
    die (f'A non-blank {name} of type dict is required.')

