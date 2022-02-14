from shutil import copytree
from glob import glob
from PIL import Image

def resize(RESIZE, FROM_DIR):
    '''
    指定ディレクトリ内のpngファイルをリサイズする
    '''
    to_dir = FROM_DIR + '_resize' + str(RESIZE)
    files = glob(to_dir + '/**/*.png', recursive=True)

    copytree(FROM_DIR, to_dir)
    for n,f in enumerate(files):
        img = Image.open(f)
        img_resize = img.resize((RESIZE,RESIZE))
        img_resize.save(f)
        print(f, f'{n}/{len(files)}')

if __name__ == '__main__':
    resize(100, 'path/to/directory')