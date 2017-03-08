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
os.chdir("/")

#  start
def main():

  #  process arguments
  arguments = get_arguments()

  #  set variables
  now = int(time.time())
  tenminago = now - 600
  loglines=[] 

  #  open file / see if it exists
  try:
    with open(arguments.log, 'r') as f:
      for singleline in f:
          



      
  except:
    #  logfile is invalid
    print "2"









 
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

