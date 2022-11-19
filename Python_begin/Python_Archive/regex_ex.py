import re

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

print('313-505-5652 is a phone number:')
print(isPhoneNumber('313-505-5652'))
print('Itachi Uchiha is a phone number:')
print(isPhoneNumber('Itachi Uchiha'))

message = 'Call me at 313-505-5652 tomorrow, or else call 313-863-4230 if you really want'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 313-532-2133')
print('Phone number is: ' + mo.group())

heroRegex = re.compile(r'Batman|Robin')
mo1 = heroRegex.search('The Batman and Robin')
print(mo1.group())

mo2 = heroRegex.search('Robin and the Batman')
print(mo2.group())

batRegex = re.compile(r'Bat(wo)?man') #(wo)? means wo is optional when searching
mo3 = batRegex.search('The advencures of Batwoman and Batman')
print(mo3.group())

batRegex2 = re.compile(r'Ba(wo)*man') #(wo)* means wo can be matched zero or more
#(wo)+ would match one or more so at least one must be present

vowelRegex = re.compile(r'[aeiouAEIOU]') #Make own Character class
print(vowelRegex.findall('RoboCop eats baby food. Baby Food.'))

consonantRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')) #Negative character class. So anything but aeiouAEIOU. (NO vowels)

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)') # '.*' uses greedy mode always trying to match as much as text as possible
# '.*?' will use nongreedy
mo4 = nameRegex.search('First Name: Nirvana Last Name: Fury')
print(mo4.group(1))
print(mo4.group(2))

robocop = re.compile(r'robocop',re.I) #Case insensitive
print(robocop.search('RoboCop is part man, part machine, all cop').group())
roboCOp = re.compile(r'robocop', re.IGNORECASE)
print(robocop.search('ROBOCOP is part man, part machine, all cop').group())

agentRegex = re.compile(r'Agent \w+')
print(agentRegex.sub('Carter', 'Agent Regex gave the secret documents to Agent Simpson'))

agentNamesRegex = re.compile(r'Agent (\w)\w*')
print(agentNamesRegex.sub(r'\1****', 'Agent Cody told Agent Martial that Agent Nirvana knew Agent Fury was a double Agent'))

phoneInfoRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              #area code
    (\s|-|\.)?                      #seperator
    \d{3}                           #first 3 digits
    (\s|-|\.)                       #Seperator
    \d{4}                           #last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?   #extension
    )''',re.VERBOSE) # ''' creates a multiline string and verbose allows you to ignore whitespace and comments

someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE) #Writing comments in reg expression and ignoring capitalization 
# and have the dot character match all characters
 
