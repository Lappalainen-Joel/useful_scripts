#!/bin/sh
#
#	Check a list of domains, print out expires -row, and domain-name.
#	Works with 5.2.11 version of whois.
#
#	Author: Joel Lappalainen

domains="example.com example2.org"

for domain in $domains
do
	who_dom=`whois $domain`
	echo "Domain: $domain"
	if [ `echo $who_dom | grep -c "not found"` -gt 0 ]; then
		echo "Domain not found"
	else
		echo -n "	Expires: "
		echo $who_dom | cut -c77- | awk '{print $4}'
	fi
done