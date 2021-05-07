import webbrowser as wb
import os
cwd = os.getcwd()
wb.open('file://' + cwd + '/index.html')
