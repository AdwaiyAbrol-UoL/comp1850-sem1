# Week 1.3, Session 2: Email Extractor

raw_emails = ["UserA@gmail.com", "admin@site.com", "usera@gmail.com", "UserB@yahoo.com", "admin@site.com"]
valid_emails = {email.lower() for email in raw_emails if "@" in email}
print(valid_emails)

#Optional - consider the case where some of the emails are not valid (i.e., without the @ in the email address).