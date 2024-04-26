import re
from logic.contact_info_extractor import find_contact_email
from logic.contact_page_selector import find_contact_page
from logic.exception_logger import log_exception
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


def process_row(row,csv_file):
    website_url = row.get('Website')
    print(f"processing this website: {website_url}")
    if not website_url:
        print("Website link is empty. Skipping...")
        return row  # Return the original row for writing back to CSV
            
    try:
        isEmailAlreadyPresent = row.get('Email')
        if isEmailAlreadyPresent and isEmailAlreadyPresent != "Email not found":
            print(f"Email is already present: {isEmailAlreadyPresent}")
            isEmailAlreadyValidated = row.get('Valid Email')
            if isEmailAlreadyValidated: 
                print(f"Email is already validated. Skipping row...")
                return row  # Return the original row for writing back to CSV
            else:
                print("Email is not validated. Validating...")
                row['Valid Email'] = validate_email(isEmailAlreadyPresent)
                return row  # Return the modified row for writing back to CSV

        domain = extract_domain_link(website_url)
        contact_url = find_contact_page(domain)
        if contact_url:
            email = find_contact_email(contact_url)
            if email:
                row['Email'] = email
                row['Valid Email'] = validate_email(email)
            else:
                row['Email'] = 'Email not found'
        else:
            row['Email'] = 'Contact page not found'
    except Exception as e:
        # Log the error with details about the row and processing step
        log_exception(e, "process_row", f"Error processing row with website: {website_url}", "")
    return row