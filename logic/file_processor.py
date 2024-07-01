import csv
import datetime

from logic.constants import LINE_SPACER
from logic.performance_logger import log_performance
from logic.valid_email_counter import valid_email_counter
from logic.web_processor import process_websites




def file_processor(file_name,file_path, workers):
    print(LINE_SPACER)
    print(f"Processing {file_name}")
    print(f"{LINE_SPACER}\n")
    start_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    clean_csv_header(file_path)
    process_websites(file_path,workers)
    end_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    emails_found = valid_email_counter(file_path)
    log_performance(file_name, emails_found, workers, start_time, end_time)
    
    
def clean_csv_header(file_path):
    # Read the header of the CSV file
    # Read the content of the file
    with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        content = list(reader)

    # Update the header
    content[0] = [column.strip() for column in content[0]]

    # Write the updated content back to the file
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(content)