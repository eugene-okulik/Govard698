from pathlib import Path
from datetime import datetime
from datetime import timedelta
import re

project_root = Path(__file__).parents[2]
data_path = project_root / 'eugene_okulik' / 'hw_13' / 'data.txt'


def read_file():
    with open(data_path, 'r') as file_data:
        read_file = file_data.readlines()
        for line in read_file:
            yield line


def extract_datetime_from_line(line):
    match = re.search(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+", line)
    if match:
        date_str = match.group()
        return datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")
    return None


def change_stings():
    for line in read_file():
        clean_line = line.lstrip()

        if clean_line.startswith('1'):
            format_date = extract_datetime_from_line(line)
            if format_date:
                new_date = format_date + timedelta(days=7)
                print(
                    f"📅 Старая дата: {format_date}\n"
                    f"✅ Новая дата (на 7 днейпозже): {new_date}"
                )

        if clean_line.startswith('2'):
            format_day = extract_datetime_from_line(line)
            if format_day:
                day_name = format_day.strftime("%A")
                print(f'Вывели название дня недели:✅ {day_name}')

        if clean_line.startswith('3'):
            format_day = extract_datetime_from_line(line)
            if format_day:
                now_date = datetime.now()
                result = now_date - format_day
                print(f'{result.days} день назад была эта дата')


change_stings()
