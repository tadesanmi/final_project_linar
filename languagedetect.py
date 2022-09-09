# A program which detect the type of language spoken
from langdetect import detect
text = input("Enter any text in any language: ")
print(detect(text))
