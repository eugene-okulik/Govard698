import argparse, os

parser = argparse.ArgumentParser(description="Поиск текста в файлах")
parser.add_argument("log_dir", help="путь к папке с логами")
parser.add_argument("--text", required=True, help="Текст для поиска")

args = parser.parse_args()
log_dir = args.log_dir

for file_name in os.listdir(log_dir):
    file_path = os.path.join(log_dir, file_name)
    if os.path.isfile(file_path):
        print('file find:', file_path)

        # читаем файл построчно и ищем совпадения
        with open(file_path, 'r', encoding="utf-8", errors="ignore") as f:
            for line_number, line in enumerate(f, start=1):
                if args.text in line:
                    words = line.strip().split()
                    for idx, word in enumerate(words):
                        if args.text in word:
                            start = max(0, idx - 5)
                            end = min(len(words), idx + 6)
                            snippet = " ".join(words[start:end])
                            print(f'[{file_name}] строка {line_number}: {snippet}')
print("holder: ", args.log_dir)
print("Что ищем: ", args.text)
