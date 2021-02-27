import pyshorteners
import pyperclip

""" A simple URL shortening. """

buf = pyperclip.paste()
s = pyshorteners.Shortener()
pyperclip.copy(s.tinyurl.short(buf))

input("The shortened link is copied, press any key to continue.")
