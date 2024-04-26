from concurrent.futures import ThreadPoolExecutor

from logic.csv_operator import read_csv, write_csv
from logic.row_processor import process_row




def process_websites(csv_file, workers):
    """Processes the websites in the CSV file to find and add contact emails."""
    data = read_csv(csv_file)
    
    print(f"Processing {len(data)} rows with {workers} workers...\n")
    with ThreadPoolExecutor(max_workers=workers) as executor:
        # Submit tasks for processing each row using map
        processed_data = executor.map(process_row, data, [csv_file] * len(data))
        
    # Convert the map object to a list    
    final_data = list(processed_data)
    # Write the updated data back to the CSV file
    write_csv(csv_file, final_data)