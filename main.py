import os
from logic.web_processor import process_websites
from logic.scraper_welcome import message

# Main function
def main():
    print(message)
    
    directory = "./data"
    
    csv_files = [file for file in os.listdir(directory) if file.endswith('.csv')]
    
    for csv_file in csv_files:
        print(f"Processing {csv_file}")
        file_path = os.path.join(directory, csv_file)
        process_websites(file_path)
    
    
    

    
    

if __name__ == "__main__":
    main()