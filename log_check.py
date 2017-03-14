#!/usr/bin/env python
#
#  Basic NRPE service check on specified logfile
#  Input:  
#    absolute path to logfile 
#      eacho line beings with Epoch, or M
#    
#  Output:  
#    "2" Error - if logfile doesn't exist
#        Error - if "ERROR" is with last 10m of logs
#
#
#
#--------------------------------------------------------------------------

#  library imports
import sys, os, argparse, datetime, time
from optparse import OptionParser
from datetime import datetime

#  make sure we are running from the "system root" directory
sysroot = os.path.abspath("/")
os.chdir(sysroot)

#  start
def main():

  #  process arguments
  arguments = get_arguments()

  #  set variables
  foundstartpoint=0
  now = time.time()
  tenminago = int(time.time()) - 600
  std10 = now.strftime("%b %e %H:%M")
  epoch10 = str(tenminago)[:-2]
  #print now
  #print tenminago
  print std10
  print epoch10
  
  #  open file / see if it exists
  try:
    with open(arguments.log, 'r') as f:
      for singleline in f:
        #if singleline.startswith( 'r' )
        #  foundstartpoint = 1
        #if singleline.startswith( 'b' )
        #  foundstartpoint = 1
        if foundstartpoint == 1 :
        	if "Error" in singleline:
        		print "2"
        		sys.exit(0)
        	elif "Warning" in singleline:
        		print "1"
        		sys.exit(0)
        	else:
        		continue
  except:  
    print "2"
    sys.exit(0)
  
  # all is okay
  print "0"
  
  sys.exit(0)

#  argument parser and help response
def get_arguments():

  parser = argparse.ArgumentParser(description="Sensu Script to Monitor Log Health")

  parser.add_argument("-l", "--log", dest="log",
                        default="/var/log/messages",
                        help="Absolute location of the logfile")

  args = parser.parse_args()
  return args

if __name__ == "__main__":
  main()

