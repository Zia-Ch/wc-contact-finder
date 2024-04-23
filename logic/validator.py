import re
import dns.resolver

def validate_email(email):
    # Check email syntax using regular expression
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_pattern, email):
        return False#, "Invalid email syntax"

    # Extract domain from email address
    _, domain = email.split('@')

    # Check domain MX records
    try:
        mx_records = dns.resolver.resolve(domain, 'MX')
        if mx_records:
            return True #, "Valid email"
        else:
            return False#, "No MX records found"
    except dns.resolver.NoAnswer:
        return False#, "No MX records found"
    except dns.resolver.NXDOMAIN:
        return False #, "Domain does not exist"
    except dns.resolver.NoNameservers:
        return False #, "No nameservers found for the domain"