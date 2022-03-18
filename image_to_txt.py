from PIL.Image import open
from tkinter import Tk, simpledialog, filedialog
from tkinter.messagebox import showinfo
from sys import exit
from pyperclip import copy
from pyocr import tesseract, get_available_tools
from pyocr.builders import TextBuilder

# Run with Windows→'Win'/Linux→'Lin'
OS = 'Win'

def image_to_txt(os):
    '''
    Converting strings in an image to text
    '''
    
    root = Tk()
    root.lower()
    root.withdraw()
    if os  == 'Win':
        # Choose your full-path of tesseract.exe
        tesseract.TESSERACT_CMD = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    tools = get_available_tools()
    if len(tools) == 0:
        print("No OCR tool found")
        exit(1)
    tool = tools[0]
    print("Will use tool '%s'" % (tool.get_name()))

    langs_idx = simpledialog.askinteger('言語選択','英語→0\n日本語（横書き）→1\n日本語（縦書き）→2')
    langs = tool.get_available_languages()
    print("Available languages: %s" % ", ".join(langs))
    print("Will use lang '%s'" % (langs[int(langs_idx)]))

    f = filedialog.askopenfilename()
    root.deiconify()
    root.withdraw()
    if not f:
        print('canceled.')
        exit(1)
    print(f)

    txt = tool.image_to_string(open(f), lang=langs[int(langs_idx)], builder=TextBuilder())
    copy(txt)
    print(f'{"-"*50}\n{txt}\n{"-"*50}')
    print('copied to clipboard.')
    showinfo('テキスト抽出結果', f'以下のテキストをクリップボードにコピーしました：\n{txt}')

if __name__ == '__main__':
    image_to_txt(OS)
