import os
os.path.join('usr', 'bin', 'spam')

myFiles = ['accounts.txt', 'details.csv', 'invite.docx']

for filename in myFiles:
    print(os.path.join('C:\\Users\\tmanX',filename))

print(os.getcwd())