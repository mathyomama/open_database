#!/bin/bash


USERNAME="admin"
PASSWORD="password"
EMAIL_ADDRESS="mathyomama@gmail.com"
DATABASE=open.db

if [ -e "$DATABASE" ]; then
	rm "$DATABASE"
fi

expect <<-CONTENTS
	spawn python manage.py syncdb
	expect "Would you like to create one now? (yes/no):" {send "yes\r"}
	expect "Username (leave blank to use \'$USER\'):" {send "$USERNAME\r"}
	expect "Email address:" {send "$EMAIL_ADDRESS\r"}
	expect "Password:" {send "$PASSWORD\r"}
	expect "Password (again):" {send "$PASSWORD\r"}
	expect "fixture(s)" {exit}
CONTENTS

python populate.py

echo
