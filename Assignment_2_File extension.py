# -*- coding: utf-8 -*-
"""
Created on Tue May 30 20:20:17 2023

@author: Arya
"""

print('Enter file name: ',end='')
file_name=input()
ext=file_name.split('.')[-1]
print('File extension: ',end='')
if ext=='py':
    print('Python')
elif ext=='txt':
    print('Text')
elif ext=='png':
    print('High Quality Image')
elif ext=='jpg':
    print('Compressed Image')
elif ext=='html':
    print('HTML document')
elif ext=='docx':
    print('Microsoft Word document')
elif ext=='doc':
    print('Word Processing document format')
elif ext=='pdf':
    print('Portable Document Format')
elif ext=='pptx':
    print('PowerPoint Presentation	')
elif ext=='mp3':
    print(' MP3 audio file')
else:
    print('Other extension')
    
    