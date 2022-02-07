from glob import glob
from os import rename

def decompress(base_dir, ext):
    '''
    指定ディレクトリ内のすべてのサブディレクトリ内にある指定拡張子ファイルを指定ディレクトリに移動する
    '''

    for i, d in enumerate(glob(f'{base_dir}/*')):
        for j, file in enumerate(glob(f'{d}/*')):
            rename(file, f'{base_dir}/{i}_{j}.{ext}')

if __name__ == '__main__':
    decompress('path/to/directory', 'png')