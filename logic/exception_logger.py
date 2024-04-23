import csv
import datetime


def log_exception(exception, function_name, message, domain):
    """Logs the exception with relevant details."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('logs.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([message, function_name, timestamp, domain, str(exception)])
