import csv
import json
import os


def read_json(json_file_path: str) -> None:
    with open(json_file_path, "r", encoding='utf-8') as file:
        return json.load(file)


def csv_to_json(csv_file_path: str, model_name: str) -> None:
    # read csv file
    with open(csv_file_path, encoding='utf-8') as csvf:
        # load csv file data using csv library's dictionary reader
        reader = csv.reader(csvf)
        header_row = []
        entries = []
        for row in reader:
            if not header_row:
                header_row = row
                continue
            pk = row[0]
            fields = {}
            for i in range(len(row) - 1):
                active_field = row[i + 1]
                if active_field.isdigit():
                    try:
                        new_number = int(active_field)
                    except ValueError:
                        new_number = float(active_field)
                    fields[header_row[i + 1]] = new_number
                else:
                    fields[header_row[i + 1]] = active_field.strip()

            row_dict = {}
            row_dict["pk"] = int(pk)
            row_dict["model"] = model_name
            row_dict["fields"] = fields
            entries.append(row_dict)
    json_file_path = csv_file_path.replace('.csv','.json')
    # convert python jsonArray to JSON String and write to file
    with open(json_file_path, 'w', encoding='utf-8') as jsonf:
        json_string = json.dumps(entries, indent=4, ensure_ascii=False)
        jsonf.write(json_string)

csv_to_json('addandcategory\\fixtures\categories.csv', 'categories.categories')
csv_to_json('addandcategory\\fixtures\\ads.csv', 'adverb.ads')
