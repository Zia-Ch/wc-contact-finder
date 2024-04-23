import re
from logic.csv_operator import read_csv, write_csv
from logic.exception_logger import log_exception
from logic.contact_page_selector import find_contact_page
from logic.contact_info_extractor import find_contact_email
from logic.validator import validate_email




def extract_domain_link(url):
    """Extracts domain or subdomain links from full links."""
    # Using regular expression to extract domain/subdomain from full link
    match = re.search(r'(?<=://)([\w\.-]+)', url)
    if match:
        domain = match.group()
        # Remove 'www' subdomain from domain
        if domain.startswith('www.'):
            domain = domain.replace('www.', '')
        return domain
    return url


def process_websites(csv_file):
    """Processes the websites in the CSV file to find and add contact emails."""
    data = read_csv(csv_file)
    total_rows = len(data)
    processed_rows = 0
    
    for row_num, row in enumerate(data, 1):
        processed_rows += 1
        print(f"Processing row {processed_rows} of {total_rows}...")
        try:
            website_url = row.get('Website')
            if not website_url:
                print("Website link is empty. Skipping...")
                continue
            
            isEmailAlreadyPresent = row.get('Email')
            if isEmailAlreadyPresent:
                print("Email already present. checking its validity...")
                isEmailAlreadyValidated = row.get('Valid Email')
                if isEmailAlreadyValidated:
                    print("Email is already validated. Skipping...")
                    continue
                else :
                    print("Email is not validated. Validating...")
                    row['Valid Email'] = validate_email(isEmailAlreadyPresent)
                    continue
            
            domain = extract_domain_link(website_url)
            contact_url = find_contact_page(domain)
            if contact_url:
                email = find_contact_email(contact_url)
                if email:
                    row['Email'] = email
                    row['Valid Email'] = validate_email(email) 
                else: 
                    row['Email' ] ='Email not found'
                
            else:
                row['Email'] = 'Contact page not found'
        except Exception as e:
            log_exception(e, "process_websites", f"Error processing row {row_num}", "")
    
        write_csv(csv_file, data)