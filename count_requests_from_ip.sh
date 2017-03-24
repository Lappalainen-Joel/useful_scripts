#!/bin/sh
#
#   Calculate amount of requests from singular ip address on minute level, by using apache2 log.
#   Should be semi-universal, if log row contains IP address and date, and
#   date is on format "24/Mar/2017:08:38:15".
#
#	Author: Joel Lappalainen
#

# Variables
	ip="89\.27\.64\.5"
	log="other_vhosts_access.log"
	years="2017"
	months="Mar"
	days="24"
	hours="08"

	#Tens of minutes
	tenminutes="0 1 2 3 4 5"

	# Singular minutes
	singminutes="0 1 2 3 4 5 6 7 8 9"

# No need to touch this, carry on.
	biggest=0

# 6 levels of for-loops. Amazing.
	for year in $years
	do
		for month in $months
		do
			for day in $days
			do
				for hour in $hours
				do
					for tenmin in $tenminutes
					do
						for singmin in $singminutes
						do
								current=`grep $ip $log | grep "$day/$month/$year:$hour:$tenmin$singmin" | wc -l`
								echo "Statistics for $hour:$tenmin$singmin/$day/$month/$year" $current
								if [ $biggest -lt $current ];then
									biggest=$current
								fi
						done
					done
				done
			done
		done
	done

# Let's echo biggest request value
	echo "Biggest value is:" $biggest
