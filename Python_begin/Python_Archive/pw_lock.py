#! Passwword copied to user password field to not be memorized (insecure) #!
PASSWORDS = {'email': 'F7mindlalkxhfgihdightd',
             'blog': 'VmAlvjdnfieighgl;ajdfjd',
             'luggage': '12345'}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python pw_lock.py [account] - copy account password')
    sys.exit()
account = sys.argv[1] # first command line arg is the account name

if account in PASSWORDS:
        pyperclip.copy(PASSWORDS[account])
        print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account anmed ' + account)
