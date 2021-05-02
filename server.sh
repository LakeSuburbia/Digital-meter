#!/bin/bash

DJANGODIR='/root/Digital-meter/interface' 
PID=$(screen -ls | grep 'server' | cut -d"." -f1)

if [ $# != 1 ]; then
	echo 'server [start|stop|migrate|status]'
	exit
fi

if [ "$1" = "start" ]; then
       if [ -z $PID ]; then
	       echo 'creating a server instance'
	       screen -dmS server
	       screen -S server -X stuff 'python3 '$DJANGODIR'/manage.py runserver 0.0.0.0:8000
	       '
	       exit
       else
	       echo 'a running server instance has been detected with pid'$PID
	       screen -S server -X stuff 'python3 '$DJANGODIR'/manage.py runserver 0.0.0.0:8000
	       '
	       exit
       fi
elif [ "$1" = "stop" ]; then
	if [ -z $PID ]; then
		echo 'the server is already offline!'
		exit
	else
		kill $PID
		echo 'the server instance on PID'$PID' has been terminated'
		exit
	fi
elif [ "$1" = "status" ]; then
	if [ -z $PID ]; then
		echo '
		[OFFLINE]
		'
		exit
	else
		echo '
		[ONLINE]
		PID'$PID'

		[MIGRATION STATUS]
		'
		python3 $DJANGODIR/manage.py showmigrations
		echo '
		'
		exit
	fi
elif [ "$1" = "migrate" ]; then
	echo '[ MIGRATION STATUS ]'
	python3 $DJANGODIR/manage.py showmigrations
	read -p 'do you want to proceed? [y/n] ' ANSWER
	case $ANSWER in
		[Yy]* )
			python3 $DJANGODIR/manage.py makemigrations
			python3 $DJANGODIR/manage.py migrate
			echo 'migration complete'
			exit;;
		* )
			exit;;
	esac
else
	echo 'server [start|stop|migrate|status]'
	exit
fi
