import csv
import os


def log_performance(file_name, no_of_emails, workers, start_time, end_time ):
    """Logs the exception with relevant details."""
    headers = ['File Name', 'No of Emails', 'Workers', 'Start Time', 'End Time']
    #read file to check if it has headers
    if not os.path.exists('./logs/performance.csv'):
        with open('./logs/performance.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            
    
    with open('./logs/performance.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([file_name, no_of_emails, workers, start_time, end_time])