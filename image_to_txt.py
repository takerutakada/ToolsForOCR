from PIL.Image import open
from tkinter import Tk, filedialog
from sys import exit
from pyperclip import copy
from pyocr import tesseract, get_available_tools
from pyocr.builders import TextBuilder

OS = 'Win'
LANG = 'jpn'

def image_to_txt(os, lang):
    root = Tk()
    root.lower()
    root.withdraw()
    if os  == 'Win':
        tesseract.TESSERACT_CMD = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    tools = get_available_tools()
    if len(tools) == 0:
        print("No OCR tool found")
        exit(1)
    tool = tools[0]
    print("Will use tool '%s'" % (tool.get_name()))

    langs = tool.get_available_languages()
    print("Available languages: %s" % ", ".join(langs))
    print("Will use lang '%s'" % (lang))

    f = filedialog.askopenfilename()
    root.deiconify()
    root.withdraw()
    if not f:
        print('canceled.')
        exit(1)
    print(f)

    txt = tool.image_to_string(open(f), lang=lang, builder=TextBuilder())
    # txt is a Python string
    print(f'{"-"*50}\n{txt}\n{"-"*50}')
    copy(txt)
    print('copied to clipboard.')

if __name__ == '__main__':
    image_to_txt(OS,LANG)