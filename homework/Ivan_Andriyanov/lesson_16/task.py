import csv
from pathlib import Path
import mysql.connector as mysql
import os
from dotenv import load_dotenv

load_dotenv()

base_path = Path(__file__).parents[2]
file = base_path / 'eugene_okulik' / 'Lesson_16' / 'data.csv'

with open(file, 'r') as data_file:
    file_data = csv.DictReader(data_file)
    cvs_set = set((row['Name'], row['last']) for row in file_data)

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=int(os.getenv('DB_PORT')),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor(dictionary=True)
cursor.execute("SELECT * FROM students")
db_data = cursor.fetchall()

db_set = set((student['name'], student['second_name']) for student in db_data)

missing = cvs_set - db_set
print('\n❌ В базе данных нет:')
for name, last in missing:
    print(f'{name} {last}')
