import re

# Task 1: Email Extractor

def extract_emails(filename): # Function  to extract all emails in a given txt file
    file = open(filename) # open file to read its contents
    emails = re.findall(r"[a-zA-Z0-9._-]+@[\w-]+\.[\w.-]+", file.read()) # regex to find email addresses
    file.close() # close file after finding all emails

    return emails

# Testing
path = "contacts.txt"
print(extract_emails(path))