import csv
import datetime
import os

from logic.constants import LINE_SPACER


def get_output_file_name(output_dir):
    file_name_by_date = datetime.datetime.now().strftime("%Y-%m-%d")
    
    file_number = 1
    output_file = os.path.join(output_dir, f"{file_name_by_date}.csv")
    
    while True:
        if os.path.exists(output_file):
            output_file = os.path.join(output_dir, f"{file_name_by_date}_{file_number}.csv")
            file_number += 1
        else:
            break
    
    return output_file

def merge_csv_files(data_dir, output_final_dir, output_raw_dir):
    
    output_final_file = get_output_file_name(output_final_dir)
    output_raw_file = get_output_file_name(output_raw_dir)
    
    
    
    # List all CSV files in the data directory
    csv_files = [file for file in os.listdir(data_dir) if file.endswith('.csv')]   
    
    # Open the output final file in write mode
    with open(output_final_file, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)

        # Flag to indicate whether to write the header
        write_header = True

        # Iterate through each CSV file
        for csv_file in csv_files:
            # Open the current CSV file
            with open(os.path.join(data_dir, csv_file), 'r', newline='', encoding='utf-8') as infile:
                reader = csv.reader(infile)

                # Skip the header if not the first file
                if not write_header:
                    next(reader)

                # Write each row to the output file
                for row in reader:
                    is_email_valid = row[6]
                    if is_email_valid == "True" or is_email_valid == "Valid Email":
                        writer.writerow(row)
                # After the first file, set the write_header flag to False
                write_header = False

    with open(output_raw_file, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)

        # Flag to indicate whether to write the header
        write_header = True

        # Iterate through each CSV file
        for csv_file in csv_files:
            # Open the current CSV file
            with open(os.path.join(data_dir, csv_file), 'r', newline='', encoding='utf-8') as infile:
                reader = csv.reader(infile)

                # Skip the header if not the first file
                if not write_header:
                    next(reader)

                # Write each row to the output file
                for row in reader:
                    writer.writerow(row)
                # After the first file, set the write_header flag to False
                write_header = False

    print(LINE_SPACER)
    print(f'Merged {len(csv_files)} CSV files into {output_final_dir} &\n {output_raw_dir} successfully.')
    print(f"{LINE_SPACER}\n")