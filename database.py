import mysql.connector

# Function to create the database and table
def create_database_and_table():
    # Connect to MySQL (change the parameters accordingly)
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",

    )

    cursor = connection.cursor()

    # Create the database if it doesn't exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS school")
    cursor.execute("USE school")

    # Create the students table if it doesn't exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        student_id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(255),
        last_name VARCHAR(255),
        age INT,
        grade FLOAT
    )
    """)

    connection.commit()
    connection.close()

# Function to connect to the MySQL database
def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="school"
    )

# Function to insert a new student record
def insert_student_record(first_name, last_name, age, grade):
    connection = connect_to_database()
    cursor = connection.cursor()

    # Insert the new student record
    insert_query = "INSERT INTO students (first_name, last_name, age, grade) VALUES (%s, %s, %s, %s)"
    data = (first_name, last_name, age, grade)
    cursor.execute(insert_query, data)

    connection.commit()
    connection.close()

# Function to update the grade of a student with a given first name
def update_student_grade(first_name, new_grade):
    connection = connect_to_database()
    cursor = connection.cursor()

    # Update the grade of the student
    update_query = "UPDATE students SET grade = %s WHERE first_name = %s"
    data = (new_grade, first_name)
    cursor.execute(update_query, data)

    connection.commit()
    connection.close()

# Function to delete a student with a given last name
def delete_student_by_last_name(last_name):
    connection = connect_to_database()
    cursor = connection.cursor()

    # Delete the student by last name
    delete_query = "DELETE FROM students WHERE last_name = %s"
    data = (last_name,)
    cursor.execute(delete_query, data)

    connection.commit()
    connection.close()

# Function to fetch and display all student records
def fetch_and_display_students():
    connection = connect_to_database()
    cursor = connection.cursor()

    # Fetch all student records
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    # Display student records
    for student in students:
        print("Student ID:", student[0])
        print("First Name:", student[1])
        print("Last Name:", student[2])
        print("Age:", student[3])
        print("Grade:", student[4])
        print()

    connection.close()

# Main program
if __name__ == "__main__":
    create_database_and_table()
    insert_student_record("Alice", "Smith", 18, 95.5)
    update_student_grade("Alice", 97.0)
   # delete_student_by_last_name("Smith")
    fetch_and_display_students()
