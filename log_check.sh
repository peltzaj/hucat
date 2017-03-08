#!/usr/bin/env bash
#####
#
#  Basic Sensu service check on specified logfile
#  Input:  
#    absolute path to logfile 
#      each new line beings with Epoch, or Mon Date Time (24h)
#    
#  Output:
#    "2" Error - if logfile doesn't exist
#        Error - if "ERROR" is within last 10m of logs
#    "1" Warning - if "WARNING" is within last 10m of logs
#    "0" OK - if no "ERROR" or "WARNING" found in existing logfile
#
#  Gotchas:
#    Logfile path must not contain spaces
#    Time is rounded to increase the potential for log hit (Log must be chatty)
#
#####

EXPECTED_ARGS=1
DATE=$(date)
FILEDATE=$(date -d "$DATE" +"%Y%m%d%H%M%S" )
STD10=$(date -d '$DATE' --date='10 minutes ago' +'%b %e %H%M') 
EPOCH10=$(date -d '$DATE' --date='10 minutes ago' +'%s' | rev | cut -c 2- | rev )


#  clean up after yourself
function cleanup() {
  if [ -f /tmp/$FILEDATE.datetime ]; then
    rm -f /tmp/$FILEDATE.datetime
  fi
  if [ -f /tmp/$FILEDATE.epoch ]; then
    rm -f /tmp/$FILEDATE.epoch
  fi
}




#  check to see if we have a single correct argument or provide guidance
if [ $# -gt $EXPECTED_ARGS ] || [ $# -lt $EXPECTED_ARGS ] || [ $1 == "-h" ] || [ $1 == "--help" ] ; then
  echo "HELP: This script requires a single argument. The Absolute path of the logfile. No Spaces in Path"
  exit 0
else
  LOGFILE=$1
fi

#  check to see if file exists or throw Sensu Error 2
if [ ! -f $LOGFILE ] ; then
  echo "2 | File $LOGFILE Does not Exist"
  cleanup 
  exit 0
fi

cleanup
#  parse file both ways separately for ease of troubleshooting if needed
sed -n -e "/^$STD10/,\$p" $LOGFILE > /tmp/$FILEDATE.datetime
sed -n -e "/^$EPOCH10/,\$p" $LOGFILE > /tmp/$FILEDATE.epoch

#  check the files for the words WARNING or ERROR and report
for FILE in /tmp/$FILEDATE.datetime /tmp/$FILEDATE.epoch ; do
  if grep -q WARNING $FILE ; then
    echo "1 | Warning in $LOGFILE"
    cleanup
    exit 0
  fi
  if grep -q ERROR $FILE  ; then
    echo "2 | Error in $LOGFILE"
    cleanup
    exit 0
  fi
done

#  if we get to this point, there is nothing bad in the logs
echo "0 | OK "
cleanup
exit 0
