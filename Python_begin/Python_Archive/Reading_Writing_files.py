Python 3.7.8 (tags/v3.7.8:4b47a5b6ba, Jun 28 2020, 07:55:33) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import os
>>> os.getcwd()
'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python37_86'
>>> os.chdir('C:\\Users
	 
SyntaxError: EOL while scanning string literal
>>> os.chdir('C:\\Users\\Tyrice Grice Jr\\Desktop\\Python_begin')
>>> os.getcwd()
'C:\\Users\\Tyrice Grice Jr\\Desktop\\Python_begin'
>>> os.makedirs('C:\\Users\\Tyrice Grice Jr\\Desktop\\Python_begin\food')
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    os.makedirs('C:\\Users\\Tyrice Grice Jr\\Desktop\\Python_begin\food')
  File "C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_86\lib\os.py", line 223, in makedirs
    mkdir(name, mode)
OSError: [WinError 123] The filename, directory name, or volume label syntax is incorrect: 'C:\\Users\\Tyrice Grice Jr\\Desktop\\Python_begin\x0cood'
>>> os.makedirs('C:\\Users\\Tyrice Grice Jr\\Desktop\\Python_begin\\food')
>>> os.makedirs('C:\\Users\\Tyrice Grice Jr\\Desktop\\Python_begin\\bs.py')
>>> os.makedirs('C:\\Users\\Tyrice Grice Jr\\Desktop\\Python_begin\\bull')
>>> os.path.isabs(path)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    os.path.isabs(path)
NameError: name 'path' is not defined
>>> os.path.isabs('.')
False
>>> os.path.abspath(bull)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    os.path.abspath(bull)
NameError: name 'bull' is not defined
>>> os.path.abspath('bull')
'C:\\Users\\Tyrice Grice Jr\\Desktop\\Python_begin\\bull'
>>> os.path.isabs('bull')
False
>>> os.path.abspath('.
		
SyntaxError: EOL while scanning string literal
>>> os.path.abspath('.\\bull')
'C:\\Users\\Tyrice Grice Jr\\Desktop\\Python_begin\\bull'
>>> os.path.isabs('bull')
False
>>> os.path.relpath('C: \\Windows', 'C:\\')
'Users\\Tyrice Grice Jr\\Desktop\\Python_begin\\ \\Windows'
>>> os.getcwd()
'C:\\Users\\Tyrice Grice Jr\\Desktop\\Python_begin'
>>> os.path.dirname(path)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    os.path.dirname(path)
NameError: name 'path' is not defined
>>> path = C:\\Users\\Tyrice Grice Jr\\Desktop\\Python_begin
SyntaxError: invalid syntax
>>> path = 'C:\\Users\\Tyrice Grice Jr\\Desktop\\Python_begin'
>>> os.path.basename(path)
'Python_begin'
>>> os.path.dirname(path)
'C:\\Users\\Tyrice Grice Jr\\Desktop'
>>> os.path.split()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    os.path.split()
TypeError: split() missing 1 required positional argument: 'p'
>>> 
>>> os.path.getsize('C:\\Users\\Tyrice Grice Jr\\Desktop\\Python_begin')
4096
>>> totalSize = 0
>>> for filename in os.listdir('C:\\Users\\Tyrice Grice Jr'):
	totalSize = totalSize + os.path.getsize(os.path.join('C:\\Users\\Tyrice Grice Jr', filename))

	
>>> print(totalSize)
12189716
>>> os.getcwd()
'C:\\Users\\Tyrice Grice Jr\\Desktop\\Python_begin'
>>> os.path.exists('C:\\Users\\Tyrice Grice Jr\\Desktop\\Greatness')
False
>>> os.path.exists('C:\\Users\\Tyrice Grice Jr\\
	       
SyntaxError: EOL while scanning string literal
>>> os.path.exists('C:\\Users\\Tyrice Grice Jr')
True
>>> os.path.isdir('C:\\Users\\Tyrice Grice Jr')
True
>>> os.path.isfile('C:\\Users\\Tyrice Grice Jr')
False
>>> os.getcwd()
'C:\\Users\\Tyrice Grice Jr\\Desktop\\Python_begin'
>>> os.path.isfile('C:\\Users\\Tyrice Grice Jr\\Desktop\\Python_begin')
False
>>> os.path.isfile('C:\\Users\\Tyrice Grice Jr\\Desktop\\Python_begin\\Reading_Writing_files')
False
>>> os.path.isfile('C:\\Users\\Tyrice Grice Jr\\Desktop\\Python_begin\\Reading_Writing_files.py')
True
>>> os.path.exists('D:\\') #Checks to see if there is a DVD or Drive
False
>>> os.listdir('C:\\Users\\Tyrice Grice Jr\\Desktop\\Python_begin')
['bull', 'bulletpointadder.py', 'file_ex.py', 'phone_email_extract.py', 'pw_lock.py', 'Reading_Writing_files.py', 'regex_ex.py', 'strong_pw_det.py', 'tic-tac-toe.py']
>>> helloFile = open('C:\\Users\\Tyrice Grice Jr\\Desktop\\Python_begin\\hello_nirvana.txt')
>>> helloContent = helloFile.read()
>>> helloContent
'Hello Nirvana, how is everything with you?'
>>> Rage27 = open('rage.txt')
>>> Rage27.readlines()
['Do Not go gentle into that good night\n', 'Old age should burn and rave at the close of day\n', 'Rage, Rage against the dying of the light\n', 'Though Wise men at their end know dark is right\n', 'Their words had forked no lighting they \n', 'Do not go gentle into that good night\n', 'Good men, the last wave by crying how bright\n', 'Their frail deeds might have danced in a green bay\n', '\n', 'Rage, rage against the dying of the light']
>>> rage27
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    rage27
NameError: name 'rage27' is not defined
>>> Rage27
<_io.TextIOWrapper name='rage.txt' mode='r' encoding='cp1252'>
>>> Rage27.open()
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    Rage27.open()
AttributeError: '_io.TextIOWrapper' object has no attribute 'open'
>>> open('rage.txt')
<_io.TextIOWrapper name='rage.txt' mode='r' encoding='cp1252'>
>>> os.getcwd()
'C:\\Users\\Tyrice Grice Jr\\Desktop\\Python_begin'
>>> os.startfile('C:\\Users\\Tyrice Grice Jr\\Desktop\\Python_begin\\rage.txt')
>>> os.startfile('C:\\Users\\Tyrice Grice Jr\\Desktop\\Python_begin\\rage.txt')_
SyntaxError: invalid syntax
>>> os.startfile('C:\\Users\\Tyrice Grice Jr\\Desktop\\Python_begin\\rage.txt')
>>> os.startfile('C:\\Program Files(x86)\\Google\\Chrome\\Application\\chrome')
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    os.startfile('C:\\Program Files(x86)\\Google\\Chrome\\Application\\chrome')
FileNotFoundError: [WinError 2] The system cannot find the file specified: 'C:\\Program Files(x86)\\Google\\Chrome\\Application\\chrome'
>>> os.startfile('C:\\Program Files\\Google\\Chrome\\Application\\chrome')
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    os.startfile('C:\\Program Files\\Google\\Chrome\\Application\\chrome')
FileNotFoundError: [WinError 2] The system cannot find the file specified: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome'
>>> os.startfile('C:\\Program Files(x86)\\Google\\Chrome\\Application\\chrome.exe')
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    os.startfile('C:\\Program Files(x86)\\Google\\Chrome\\Application\\chrome.exe')
FileNotFoundError: [WinError 2] The system cannot find the file specified: 'C:\\Program Files(x86)\\Google\\Chrome\\Application\\chrome.exe'
>>> google
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    google
NameError: name 'google' is not defined
>>> chrome
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    chrome
NameError: name 'chrome' is not defined
>>> import webbrowser
>>> webbrowser.get('C:\\Program Files(x86)\\Google\\Chrome\\Application\\chrome.exe').open(url)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    webbrowser.get('C:\\Program Files(x86)\\Google\\Chrome\\Application\\chrome.exe').open(url)
  File "C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_86\lib\webbrowser.py", line 65, in get
    raise Error("could not locate runnable browser")
webbrowser.Error: could not locate runnable browser
>>> webbrowser.get('C:\\Program Files(x86)\\Google\\Chrome\\Application\\chrome.exe %$').open(url)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    webbrowser.get('C:\\Program Files(x86)\\Google\\Chrome\\Application\\chrome.exe %$').open(url)
  File "C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_86\lib\webbrowser.py", line 65, in get
    raise Error("could not locate runnable browser")
webbrowser.Error: could not locate runnable browser
>>> webbrowser.open_new_tab('http:\\www.google.com')
True
>>> 