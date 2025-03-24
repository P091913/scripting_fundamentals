import re

# define the regex pattern for an email
email_pattern = r"[a-zA-Z0-9-._]+@[a-zA-Z-]+\.[a-zA-Z]{2,}"
# email_pattern = r"\S+@\S"


def main():
    # accept list back from read_extract
    emails = read_extract()

    # passing an argument
    write_emails(emails)


def read_extract():
    # open up the extract file
    # r - read
    # w - write
    # a - append
    with open("extract_text.txt", "r") as file:
        # findall() - take all of the content from your file
        # find every you had, it'll put it into a list be default
        # using findall() eliminates the need to loop through line by line
        text_content = file.read()
        # list comes back from our findall
        emails = re.findall(email_pattern, text_content)
    # return list to where my function call originated from
    return emails

def write_emails(emails):
    # opening output file in write mode
    output_file = open("emails.txt", "w")

    for email in emails:
        output_file.write(f"Email: {email}\n" )


# entry point to our logic
main()


# regex patter to pull names that are 4 letters
#name_pattern = r"^[a-zA-Z]{4}$"
##with open("names.txt", "r") as file:
#    for line in file:
#        if re.match(name_pattern, line):
#            print(line)
