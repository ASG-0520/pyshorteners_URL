import pyshorteners
"""Укорачивает длинные ссылки"""
s = pyshorteners.Shortener()
print("\n" + s.tinyurl.short(input("Enter URL: "))+"\n")

input("Press any key to continue.")

