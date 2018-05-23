#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands
# import zipfile

"""Copy Special exercise
"""

#searches through files and directories within a specified directory
#finds files that match a pattern
#prints absolute path of each file
def List(dir):
  filenames = os.listdir(dir)
  special = []
  for filename in filenames:
    match = re.search(r'__\w+__', filename)
    if match:
      special.append(os.path.abspath(filename))
  for name in special:
    print name
  return special

#checks to see whether directoryA exists within directoryB
#if directoryA is in directoryB, take each special files from List() function and copy to directoryA
#if directoryA doesn't exist, make directoryA and copy special files to directoryA
def copy2newdir(dir, fromdir):
  fromdir = os.path.abspath(fromdir)
  dir = fromdir + "/" + dir
  if os.path.exists(dir):
    for specialfile in List(fromdir):
      shutil.copy(specialfile, dir)
  else:
    os.mkdir(dir)
    for specialfile in List(fromdir):
      shutil.copy(specialfile, dir)

#zips all special files with specified zipfile name & prints the command used to do it
def zippin(zipname, dir):
  for specialfile in List(dir):
    command = os.system("zip -j " + zipname + " " + specialfile)
  print "Command I'm going to do: zip -j "+ zipname + " " + " ".join(List(dir))

  #alternative solution - creates zipfile with zipfile module
  # z = zipfile.ZipFile(zipname, 'w')
  # for specialfile in List(dir):
  #   z.write(specialfile)
  # z.close()
  # z.printdir()


def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  tozip = ''
  if args[0] == '--todir':
    todir = args[1]
    fromdir = args[2]
    del args[0:2]
    copy2newdir(todir, fromdir)
  elif args[0] == '--tozip':
    zipname = args[1]
    dir = args[2]
    zippin(zipname, dir)
    del args[0:2]
  elif len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)
  else:
    List(args[0])


if __name__ == "__main__":
  main()
