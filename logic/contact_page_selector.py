from fake_useragent import UserAgent
import re
import requests
from bs4 import BeautifulSoup
from logic.exception_logger import log_exception

def find_contact_page(domain):
    """Finds the contact page URL for a given domain using various methods."""
    headers = {'User-Agent': UserAgent().random}
    
    # List of common contact page names
    common_patterns = ['contact', 'contact-us', 'contactus','about','about-us']
    
    
    
    # If not found, try sitemap.xml and robots.txt
    sitemap_url = f'http://{domain}/sitemap.xml'
    robots_url = f'http://{domain}/robots.txt'
    
    contact_url = None
    
    # Check if sitemap exists and contains contact page URL
    try:
        sitemap_response = requests.get(sitemap_url, headers=headers, timeout=(5, 10))
        sitemap_response.raise_for_status()
        if sitemap_response.status_code == 200:
            soup = BeautifulSoup(sitemap_response.text, 'xml')
            contact_urls = [loc.text for loc in soup.find_all('loc') if 'contact' in loc.text]
            if contact_urls:
                contact_url = contact_urls[0]
    except Exception as e:
        log_exception(e, "find_contact_page", "Error accessing sitemap", domain)
    
    # Check robots.txt for contact page URL
    try:
        robots_response = requests.get(robots_url, headers=headers, timeout=(5, 10))
        robots_response.raise_for_status()
        if robots_response.status_code == 200:
            if 'contact' in robots_response.text:
                contact_path = re.search(r'(?<=Contact:\s)(.*)', robots_response.text)
                if contact_path:
                    contact_url = f'http://{domain}/{contact_path.group(0)}'
    except Exception as e:
        log_exception(e, "find_contact_page", "Error accessing robots.txt", domain)
    
    # Try common contact page names
    for page_name in common_patterns:
        contact_url = f'http://{domain}/{page_name}'
        try:
            response = requests.get(contact_url, headers=headers, timeout=(5, 10))
            response.raise_for_status()
            if response.status_code == 200:
                return contact_url
        except Exception as e:
            log_exception(e, "find_contact_page", f"Error accessing {contact_url}", domain)
    contact_url = f'http://{domain}/'
    return contact_url