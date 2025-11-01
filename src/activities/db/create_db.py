import pandas as pd
from pathlib import Path
import sqlite3



def create_db(sql_path, db_path):

    connection = sqlite3.connect(db_path)  # Create a connection to the database using sqlite3
    cursor = connection.cursor()  # Create a cursor object to execute SQL commands
    cursor.execute('PRAGMA foreign_keys = ON;')  # Enable foreign key constraints for sqlite

    # Define the SQL INSERT query
    insert_sql = 'INSERT INTO student (student_name, student_email) VALUES ("Harpreet", "harpreet@school.com")'

    cursor.execute(insert_sql)  # Execute the insert query 
    connection.commit()  # Commit the changes
    connection.close()  # Close the connection

def delete_rows(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
    table_names = [row[0] for row in cur.fetchall()]
    for table_name in table_names:
      
        cur.execute(f"DELETE FROM {table_name}")
    conn.commit()
    conn.close()

def insert_db(db_path):
        # Use a single connection and cursor
    with sqlite3.connect(db_path) as conn:
        # Load data
        data_path = Path(__file__).parent.parent.joinpath("data", "student_data.csv")
        df = pd.read_csv(data_path)

        # Extract unique student and teacher data
        student_data = df[['student_name', 'student_email']].drop_duplicates().values.tolist()
        teacher_data = df[['teacher_name', 'teacher_email']].drop_duplicates().values.tolist()

        # SQL statements
        student_sql = 'INSERT OR IGNORE INTO student (student_name, student_email) VALUES (?, ?)'
        teacher_sql = 'INSERT OR IGNORE INTO teacher (teacher_name, teacher_email) VALUES (?, ?)'
        enrollment_insert_sql = """
            INSERT INTO enrollment (student_id, course_id, teacher_id)
            VALUES 
            (
                (SELECT student_id FROM student WHERE student_email = ?),
                (SELECT course_id FROM course WHERE course_name = ? AND course_code = ?),
                (SELECT teacher_id FROM teacher WHERE teacher_email = ?)
            )
        """
        cur = conn.cursor()
        cur.execute('PRAGMA foreign_keys = ON;')
        # Insert students and teachers
        cur.executemany(student_sql, student_data)
        cur.executemany(teacher_sql, teacher_data)

        
        # Insert enrollments
        for _, row in df.iterrows():
            
            enrollment_insert_sql = """
                         INSERT INTO enrollment (student_id, course_id, teacher_id)
                         VALUES ((SELECT student_id FROM student WHERE student_email = ?), \
                                 (SELECT course_id FROM course WHERE course_name = ? AND course_code = ?), \
                                 (SELECT teacher_id FROM teacher WHERE teacher_email = ?)) \
                         """
        for _, row in df.iterrows():
            cur.execute(
                enrollment_insert_sql,
                (
                    row['student_email'],
                    row['course_name'],
                    row['course_code'],
                    row['teacher_email'],
                )
            )

    conn.commit()
    conn.close()



def main():
    sql_path = Path(__file__).parent.parent.joinpath("starter", "student_schema.sql")
    db = Path(__file__).parent.parent.joinpath("data", "sample.db")
    #create_db(sql_path, db)
    delete_rows(db)
    insert_db(db)

if __name__ == "__main__":
    main()