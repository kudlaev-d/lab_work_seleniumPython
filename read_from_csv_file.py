import csv
from typing import Dict

def read_from_csv_file(file_name: str) -> Dict:

    with open(file_name) as csv_file:
        # Инициализируем объект класса DictReader, передаем параметр quoting
        # для преобразования полей без кавычек во float
        csv_reader = csv.DictReader(csv_file, quoting=csv.QUOTE_NONNUMERIC)
        for row in csv_reader:
            dict_csv: Dict = row

        return dict_csv
