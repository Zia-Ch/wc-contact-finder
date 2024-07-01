import os
import datetime
from logic.constants import LINE_SPACER
from logic.file_processor import file_processor
from logic.out_put_files_merger import merge_csv_files
from logic.scraper_welcome import message

def privacy_validator():
    print(LINE_SPACER)
    print("For your IP protection")
    print(f"{LINE_SPACER}\n")
    user_input = input("Are you using VPN/Proxies or RDP? (y/n): ").lower()
    return user_input


def files_lopper(csv_files, processing_batch_no, directory, workers):
    print(LINE_SPACER)
    print(f"Processing {processing_batch_no} started!\n")
    for csv_file in csv_files:
        file_path = os.path.join(directory, csv_file)
        file_processor(csv_file, file_path,  workers)
    
    print(f"{LINE_SPACER}\n")
    print(f"Processing {processing_batch_no} completed!")
    print(f"{LINE_SPACER}\n")    
    

# Main function
def main():
    print(message)
    
    directory = "./data"
    output_final_dir = r"D:/freelance/clients/Concept Estimate - Naveed/leads/final-leads"
    output_raw_dir = r"D:/freelance/clients/Concept Estimate - Naveed/leads/raw-leads"
     
    while True:
        user_input = privacy_validator()
        if user_input == "y":
            
            csv_files = [file for file in os.listdir(directory) if file.endswith('.csv')]
            files_lopper(csv_files, "Batch 1", directory, 20)
            files_lopper(csv_files, "Batch 2", directory, 10)
            break
        
        elif user_input == "n":
            print(LINE_SPACER)
            print("Quitting the program!")
            print("Please use VPN/Proxies or RDP for your IP protection.")
            print(f"{LINE_SPACER}\n")
            break
        else:
            print("Invalid input! Please enter 'y' or 'n'")
    
    print(f"{LINE_SPACER}")
    print("All processing completed!")
    print(f"{LINE_SPACER}\n")
  
    
    
    print(LINE_SPACER)
    print(f"Merging all files into one file...")
    print(f"{LINE_SPACER}\n")
    merge_csv_files(directory, output_final_dir, output_raw_dir)

if __name__ == "__main__":
    main()