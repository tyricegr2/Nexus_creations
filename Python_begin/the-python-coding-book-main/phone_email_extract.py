# Get the text off the clip board (ctrl-A ?)
# Find all phone numbers and email addresses in the text
# Paste them onto the clipboard

# Use pyperclip module to copy and paste strings
# Create 2 regexes, one for matching phone numbers and the other matching email addresses
# Find all matches, not just the first match, of both regexes
# Neatly format the matched strings into a single string to paste
# Display some kind of message if no matches were found in the text

# Step 1: Create a Regex for Phone numbers

import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?               # area code can be in parentheses or without
    (\s|-|\.)?                      # separator can be a space, hyphen, or period
    (\d{3})                         # first 3 digits
    (\s|-|\.)                       # separator
    (\d{4})                         # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension: any number of spaces, with ext, x, or ext. followed by 2 to 5 digits
    )''', re.VERBOSE)

# TODO: Step 2: Create email regex.
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+           # username
    @                           # @ symbol
    [a-zA-Z0-9.-]+              # domain name
    (\.[a-zA-Z]{2,4})           # dot-something or top level domain
    )''',re.VERBOSE)


# TODO: Step 3: Find matches in clipboard text.
text = str(pyperclip.paste()) # will get a string value of the text on the clipboard
matches = [] #Store matches in a list variable named matches
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]]) #Area code, first 3 digits, last 4 digits
    if groups[8] != '':
        phoneNum += ' x' + groups[8] # the extension if it is not empty
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0]) #Group 0 matches the entire regular expression so the group at index 0 of tuple is the one we are interested in

# TODO: Step 4: Copy results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
