#db1 SQLite assignment
#Team: The Rainbow Keys
#Quinn Dibble, Misha Kotlik
#SoftDev, Pd. 9

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

#Main program function
def main():
	#Create & fill students table
	enter_students("data\peeps.csv")
	
	#Create & fill courses table
	#enter_courses("data\courses.csv")
		
def enter_students(filename):
	#Open csv file for reading
	csvFile = open(filename)
	csvDict = csv.DictReader(csvFile)
	
	#Prepare databse for entry
	f="discobandit.db" #db filename
	db = sqlite3.connect(f) #open if f exists, otherwise create
	cur = db.cursor() #facilitate db ops
	
	#Create students table
	query = "CREATE TABLE students (name TEXT, age INTEGER, id INTEGER)"
	cur.execute(query)
	
	#Enter student data into table from csvDict
	for entry in csvDict:
		query = "INSERT INTO students VALUES (?,?,?)"
		#? marks are replaced by corresponding tuple values
		#Helps safeguard against SQL injections?
		values = (entry['name'], entry['age'], entry['id'])
		cur.execute(query, values)
	
	#Commit & close resources
	db.commit()
	db.close()
	csvFile.close()
	

#def enter_courses(csvDict):

#USE QUERY BELOW FOR FILLING COURSES TABLE
#FOLLOW FUNCTION FORMAT OF ENTER_STUDENTS FUNCTION ABOVE

#q = "CREATE TABLE courses (code TEXT, id INTEGER, mark INTEGER)"

#RUN
main()
