#!/usr/bin/python
#test postgres connection
import psycopg2

conn = psycopg2.connect("\
	dbname='media_data'\
	user='zaphod'\
	host='picl-pidrive'\
	password='zaphod'\
");

curs = conn.cursor()
try:
    curs.execute("CREATE TABLE t_media_data (media_id INTEGER PRIMARY KEY, media_title VARCHAR(250), media_date date)")
    print "Success!"
except:
    print "whoops, hang on.."
    conn.rollback()
    curs.execute("DROP TABLE t_media_data")
    curs.execute("CREATE TABLE t_media_data (media_id INTEGER PRIMARY KEY, media_title VARCHAR(250), media_date date)")
    print "Success!!"
conn.commit()
