import re
import tkinter
from tkinter import filedialog

match = re.search(r'portal', 'GeeksforGeeks: A computer science \
				portal for geeks')
print(match)
print(match.group())

print('Start Index:', match.start())
print('End Index:', match.end())

