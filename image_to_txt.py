from PIL.Image import open
from sys import exit
from pyperclip import copy
from pyocr import tesseract, get_available_tools
from pyocr.builders import TextBuilder

OS = 'Lin'
LANG = 'jpn'

def image_to_txt(os, lang):
    if os  == 'Win':
        tesseract.TESSERACT_CMD = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    tools = get_available_tools()
    if len(tools) == 0:
        print("No OCR tool found")
        exit(1)
    # The tools are returned in the recommended order of usage
    tool = tools[0]
    print("Will use tool '%s'" % (tool.get_name()))
    # Ex: Will use tool 'libtesseract'

    langs = tool.get_available_languages()
    print("Available languages: %s" % ", ".join(langs))
    print("Will use lang '%s'" % (lang))
    # Ex: Will use lang 'fra'
    # Note that languages are NOT sorted in any way. Please refer
    # to the system locale settings for the default language
    # to use.

    txt = tool.image_to_string(open('test.png'), lang=lang, builder=TextBuilder())
    # txt is a Python string
    print(f'{"-"*50}\n{txt}\n{"-"*50}')
    copy(txt)
    print('copied to clipboard.')

if __name__ == '__main__':
    image_to_txt(OS,LANG)