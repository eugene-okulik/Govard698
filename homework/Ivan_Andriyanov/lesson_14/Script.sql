INSERT INTO students (name, second_name) VALUES ('Ivan', 'Andriyanov')

INSERT  INTO books (title, taken_by_student_id) VALUES  ('war and peace', 20838)

INSERT  INTO books (title, taken_by_student_id) VALUES  ('Naruuutooo', 20838)

INSERT INTO `groups` (title, start_date, end_date) VALUES  ('Super_puper', 'May 2025', 'Sent 2025') 

UPDATE students SET group_id = 5452 WHERE id = 20838

INSERT INTO subjets (title) VALUES ('music'), ('cookie')

INSERT INTO lessons (title, subject_id) VALUES ('Rock', 11567), ('Rep', 11568)

INSERT INTO marks (value, lesson_id, student_id) VALUES (5, 11592, 20838), (5, 11593, 20838)


SELECT value from marks m JOIN students s ON m.student_id = s.id WHERE s.id = '20838'


SELECT title from books b JOIN students s ON s.id = b.taken_by_student_id Where s.id = '20838'

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
WHERE s.id = '20838';
