import csv
from pathlib import Path
import mysql.connector as mysql
import os
from dotenv import load_dotenv

load_dotenv()

base_path = Path(__file__).parents[2]
file = base_path / 'eugene_okulik' / 'Lesson_16' / 'hw_data' / 'data.csv'


with open(file, 'r') as data_file:
    file_data = csv.DictReader(data_file)
    csv_set = set(
        (
            row['name'],
            row['second_name'],
            row['group_title'],
            row['book_title'],
            row['subject_title'],
            row['lesson_title'],
            row['mark_value']
        )
        for row in file_data
    )

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=int(os.getenv('DB_PORT')),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor(dictionary=True)

query = """
    SELECT s.name, s.second_name,
           g.title AS group_title,
           b.title AS book_title,
           subj.title AS subject_title,
           l.title AS lesson_title,
           CAST(m.value AS CHAR) AS mark_value
    FROM students s
    JOIN `groups` g ON s.group_id = g.id
    LEFT JOIN books b ON b.taken_by_student_id = s.id
    JOIN marks m ON m.student_id = s.id
    JOIN lessons l ON m.lesson_id = l.id
    JOIN subjets subj ON l.subject_id = subj.id
"""

cursor.execute(query)
db_data = cursor.fetchall()

db_set = set(
    (
        row['name'],
        row['second_name'],
        row['group_title'],
        row['book_title'],
        row['subject_title'],
        row['lesson_title'],
        row['mark_value']
    )
    for row in db_data
)

missing = csv_set - db_set
available = csv_set & db_set


print('\n✅ В БД найдены строки из csv файла:')
for name, second_name, group, book, subject, lesson, value in available:
    print(f"Студент: {name} {second_name}, группа: {group}, книга: {book},"
          f" предмет: '{subject}', урок: '{lesson}', оценка: {value}")

print('\n❌ В БД нет следующих строк из csv файла:')
for name, second_name, group, book, subject, lesson, value in missing:
    print(f"{name} {second_name}, группа: {group}, книга: '{book}', предмет:"
          f" '{subject}', урок: '{lesson}', оценка: {value}")

cursor.close()
db.close()
