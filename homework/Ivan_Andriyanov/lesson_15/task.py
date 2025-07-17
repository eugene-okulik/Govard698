import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

query_create_student = 'INSERT INTO students (name, second_name) VALUES (%s, %s)'
values_create_student = ('Ivan', 'Andriyanov')
cursor.execute(query_create_student, values_create_student)
db.commit()
student_id = cursor.lastrowid

query_create_books = 'INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)'
values_create_books = [
    ('war and peace', student_id),
    ('Naruuutooo', student_id)
]
cursor.executemany(query_create_books, values_create_books)
db.commit()

query_create_groups = 'INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)'
values_create_groups = ('Super_puper', 'May 2025', 'Sept 2025')
cursor.execute(query_create_groups, values_create_groups)
db.commit()
group_id = cursor.lastrowid

query_add_student_for_group = 'UPDATE students SET group_id = %s WHERE id = %s'
values_add_group = (group_id, student_id)
cursor.execute(query_add_student_for_group, values_add_group)
db.commit()


query_create_subject_1 = 'INSERT INTO subjets (title) VALUES (%s)'
cursor.execute(query_create_subject_1, ('music',))
db.commit()
subject_id_1 = cursor.lastrowid

query_create_subject_2 = 'INSERT INTO subjets (title) VALUES (%s)'
cursor.execute(query_create_subject_2, ('cookie',))
db.commit()
subject_id_2 = cursor.lastrowid

query_create_lesson_1 = 'INSERT INTO lessons (title, subject_id) VALUES (%s, %s)'
cursor.execute(query_create_lesson_1, ('Rock', subject_id_1))
db.commit()
lesson_id_1 = cursor.lastrowid

query_create_lesson_2 = 'INSERT INTO lessons (title, subject_id) VALUES (%s, %s)'
cursor.execute(query_create_lesson_2, ('Rep', subject_id_2))
db.commit()
lesson_id_2 = cursor.lastrowid

query_create_mark_1 = 'INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)'
cursor.execute(query_create_mark_1, (5, lesson_id_1, student_id))
db.commit()

query_create_mark_2 = 'INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)'
cursor.execute(query_create_mark_2, (5, lesson_id_2, student_id))
db.commit()


cursor.execute('SELECT value FROM marks WHERE student_id = %s', (student_id,))
cursor.fetchall()

cursor.execute('SELECT title FROM books WHERE taken_by_student_id = %s', (student_id,))
cursor.fetchall()

query_full = '''
SELECT
  g.title AS group_title,
  b.title AS book_title,
  m.value AS mark,
  l.title AS lesson_title,
  sub.title AS subject_title
FROM students s
JOIN `groups` g ON s.group_id = g.id
JOIN books b ON b.taken_by_student_id = s.id
JOIN marks m ON m.student_id = s.id
JOIN lessons l ON l.id = m.lesson_id
JOIN subjets sub ON l.subject_id = sub.id
WHERE s.id = %s
'''
cursor.execute(query_full, (student_id,))
print(cursor.fetchone())
