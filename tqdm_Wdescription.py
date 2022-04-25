from tqdm import tqdm
import time

def tqdm_Wdescription(loop1, loop2):
    '''
    tqdmを二重ループで使用し、両ループでset_descriptionを適用する
    '''

    with tqdm(total = len(loop1)) as Pbar:
        for s1 in loop1:
            Pbar.set_description(s1)
            with tqdm(total = len(loop2), leave=False) as pbar:
                for s2 in loop2:
                    pbar.set_description(s2)
                    pbar.update(1)
                    time.sleep(1)
            Pbar.update(1)

if __name__ == '__main__':
    Samples = ['A', 'B', 'C']
    samples = ['a', 'b', 'c']
    tqdm_Wdescription(Samples, samples)
