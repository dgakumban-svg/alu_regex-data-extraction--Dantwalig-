import re
# Sample text
text = """
Emails: user@example.com, firstname.lastname@company.co.uk
Websites: https://www.example.com, http://sub.example.org/page
Phones: (123) 456-7890, 123-456-7890, 123.456.7890
Credit cards: 1234-5678-9012-3456, 1234 5678 9012 3456
Prices: $19.99, $1,234.56
"""

# 1. EMAIL REGEX
email_patern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
emails = re.findall(email_patern, text)
print("Emails found:", emails)