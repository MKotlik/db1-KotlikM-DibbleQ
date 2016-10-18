#SQLite Assignment 2
#Team: The Rainbow Keys
#Quinn Dibble, Misha Kotlik
#SoftDev, Pd. 9

import sqlite3

def main():
    write_averages(generate_averages(get_student_data()))

#get_student_data()
#Retrieves student grade data from database
#Returns csv list, 1st el - name, 2nd el - mark
def get_student_data():
    #Facilitate database interaction
    conn = sqlite3.connect("discobandit.db")
    cur = conn.cursor()

    #Retrieve data from tables
    #cur.execute(".mode csv")
    #cur.execute(".headers off")
    query = "SELECT name, mark FROM students, classes WHERE students.id == classes.id"
    cur.execute(query)
    data_list = cur.fetchall()
    conn.close #close resources

    return data_list #return data

#generate_averages()
#Calculates and returns a dict of student averages
def generate_averages(grade_list):
    student_dict = {}
    
    for entry in grade_list:
        #Add student, initial class count, and grade to dict if new
        if entry[0] not in student_dict:
            student_dict[entry[0]] = [1, entry[1]]
        #Increment class count and sum grades if student already in dict
        else:
            student_dict[entry[0]][0] += 1
            student_dict[entry[0]][1] += entry[1]
            
    #Replace [count, grade sum] list with student averages
    for key in student_dict:
        student_dict[key] = student_dict[key][1] / student_dict[key][0]
        
    return student_dict
                
#write_averages()
#Takes student averages in dict and writes to SQLite table
def write_averages(student_dict):
    #Facilitate database interaction
    conn = sqlite3.connect("discobandit.db")
    cur = conn.cursor()

    #Create new averages table
    query = "CREATE TABLE averages(name TEXT, average INTEGER)"
    cur.execute(query)

    #enter student data into averages table
    for key in student_dict:
        query = "INSERT INTO averages VALUES (?, ?)"
        values = (key, student_dict[key])
        cur.execute(query, values)

    #Commit changes and close
    conn.commit()
    conn.close()
    
#RUN
main()
