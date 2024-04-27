from logic.csv_operator import read_csv


def valid_email_counter(csv_file):
    """ Given a CSV file, return the number of rows with valid emails."""
    data = read_csv(csv_file)
    
    processed_rows = 0
    
    counter = 0
    for row in enumerate(data, 1):
        processed_rows += 1
        is_email_valid = row[1]['Valid Email']
        if is_email_valid == "True":
            counter += 1
    return counter        
