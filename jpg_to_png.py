from PIL import Image
from glob import glob

def jpg_to_png(BASE_DIR):
    '''
    指定フォルダ内のjpgファイルをpngファイルに変換する
    '''
    
    files = glob(BASE_DIR + '/*.jpg')
    for n, file in enumerate(files):
        imagefile = Image.open(file)
        imagefile.save(BASE_DIR + '/' + str(n).zfill(4) + '.png')

if __name__ == '__main__':
    jpg_to_png('path/to/directory')
