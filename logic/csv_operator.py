import csv


def read_csv(file_path):
    """Reads the CSV file and returns a list of dictionaries containing company information."""
    data = []
    with open(file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def write_csv(file_path, data):
    """Writes the updated data with contact emails back to the CSV file."""
    headers = data[0].keys() if data else []
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)