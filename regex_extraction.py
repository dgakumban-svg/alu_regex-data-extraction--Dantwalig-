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

# 2. URL REGEX
url_pattern = r'https?://[A-Za-z0-9.-]+(?:/[^\s]*)?'
urls = re.findall(url_pattern, text)
print("URLs found:", urls)

# 3. PHONE NUMBER REGEX
phone_pattern = r'(\(\d{3}\)\s?\d{3}[-.]\d{4}|\d{3}[-.]\d{3}[-.]\d{4})'
phones = re.findall(phone_pattern, text)
print("Phone numbers found:", phones)

# 4. CREDIT CARD REGEX
credit_card_pattern = r'\b(?:\d{4}[- ]?){3}\d{4}\b'
credit_cards = re.findall(credit_card_pattern, text)
print("Credit cards found:", credit_cards)