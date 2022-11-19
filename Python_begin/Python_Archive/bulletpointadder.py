#Adds wiki bullet points to the start

import pyperclip
text = pyperclip.paste()

lines = text.split('\n')
for i in range(len(lines)):     #loop through all indexes in the lines list
    lines[i] = '* ' + lines[i]  # add a star to each string in lines list
text = '\n'.join(lines)
pyperclip.copy(text)
