# This program open all links copied to clipboard in a browser in separate tabs.
# Pass a command line argument where the argument should specify the separator between links. By default,
# separator = new line

import webbrowser
import sys
import pyperclip

sep = "\n"
browser = webbrowser.get()

if len(sys.argv) == 2:
    sep = sys.argv[1]


is_first_link = True

# Separate all links
clipBoard = pyperclip.paste()
linkList = clipBoard.split(sep)

for x in linkList:
    x = x.strip()

    if (x != ""):
        print(x)
        if is_first_link:
            is_first_link = False
            browser.open_new(x)
        else:
            browser.open_new_tab(x)
