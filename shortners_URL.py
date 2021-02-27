import pyshorteners
import pyperclip

""" A simple URL shortening. """
print('The shortened link is copied!')
buf = pyperclip.paste()
s = pyshorteners.Shortener()
pyperclip.copy(s.tinyurl.short(buf))


