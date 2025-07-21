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

query_create_subject = 'INSERT INTO subjets (title) VALUES (%s)'
subjects = ['music', 'cookie']
subject_ids = []

for subject in subjects:
    cursor.execute(query_create_subject, (subject,))
    subject_ids.append(cursor.lastrowid)
db.commit()

query_create_lesson = 'INSERT INTO lessons (title, subject_id) VALUES (%s, %s)'
lessons = [('Rock', subject_ids[0]), ('Rep', subject_ids[1])]
lesson_ids = []

for title, subject_id in lessons:
    cursor.execute(query_create_lesson, (title, subject_id))
    lesson_ids.append(cursor.lastrowid)
db.commit()

lesson_id_1 = lesson_ids[0]
lesson_id_2 = lesson_ids[1]

query_create_marks = 'INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)'
values_create_marks = [
    (5, lesson_id_1, student_id),
    (5, lesson_id_2, student_id)
]
cursor.executemany(query_create_marks, values_create_marks)
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
