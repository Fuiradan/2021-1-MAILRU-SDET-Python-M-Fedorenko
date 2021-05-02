#!/bin/bash
if [ $# -eq 1 ]; then
    > b_output.txt
    printf "Total number of requests:" >> b_output.txt
    cat $1 | awk {'print $7'} | sort | uniq -c | sort -rn | wc -l >> b_output.txt
    printf "\nTop 10 of requests:" >> b_output.txt
    cat $1 | awk {'print $7'} | sort | uniq -c | sort -rn | head -n 10 | awk {'print "Url:",$2,"\nRequests:",$1'} >> b_output.txt
    printf "\nTotal number of requests by method:" >> b_output.txt
    cat $1 | awk {'print $6'} | grep -Eo "(GET$|POST$|HEAD$|OPTIONS$|PUT$|PATCH$|DELETE$|TRACE$|CONNECT$)" | sort | uniq -c | sort -rn | awk {'print "Method:",$2,"\nRequests:",$1'} >> b_output.txt
    printf "\nTop 5 largest requests with client error:" >> b_output.txt
    cat $1 | awk '$9 ~ /4[0-9][0-9]/' | awk {'print $1,$7,$9,$10'} | sort -r -k4 | head -5 | awk {'print "Url:",$2,"\nStatuscode:", $3,"\nSize:",$4,"\nIP:",$1'} >> b_output.txt
    printf "\nTop 5 users by the number of requests that ended with a server error:" >> b_output.txt
    cat $1 | awk '$9 ~ /5[0-9][0-9]/' | awk {'print $1'} | uniq -c| sort -rn | head -5 | awk {'print "IP:",$2,"\nRequests:",$1'} >> b_output.txt
else
    echo "Missing logfile"
    exit 1
fi