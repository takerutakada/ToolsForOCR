from glob import glob
from os import rename

def decompress(BASE_DIR, ext):
    '''
    指定ディレクトリ内のすべてのサブディレクトリ内にある指定拡張子ファイルを指定ディレクトリに移動する
    '''

    for i, d in enumerate(glob(f'{BASE_DIR}/*')):
        for j, file in enumerate(glob(f'{d}/*')):
            rename(file, f'{BASE_DIR}/{i}_{j}.{ext}')

if __name__ == '__main__':
    decompress('path/to/directory', 'png')