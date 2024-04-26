import os
from logic.web_processor import process_websites
from logic.scraper_welcome import message

# Main function
def main():
    print(message)
    
    directory = "./data"
    
    csv_files = [file for file in os.listdir(directory) if file.endswith('.csv')]
    
    for csv_file in csv_files:
        print(f"===================================================\n")
        print(f"Processing {csv_file} \n")
        print(f"===================================================\n")
        file_path = os.path.join(directory, csv_file)
        process_websites(file_path,15)
    
    print(f"===================================================\n")
    print(f"Processing 1 completed! \n")
    print(f"===================================================\n\n")
    #TODO: save performance results to a new csv file
    
    print(f"Starting Processing 2\n")
    
    for csv_file in csv_files:
        print(f"===================================================\n")
        print(f"Processing {csv_file} \n")
        print(f"===================================================\n")
        file_path = os.path.join(directory, csv_file)
        process_websites(file_path,10)
        
    print(f"===================================================\n")
    print(f"Processing 2 completed! \n")
    print(f"===================================================\n")
    

    
    

if __name__ == "__main__":
    main()