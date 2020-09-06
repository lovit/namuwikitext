import json
import os
import numpy as np
from glob import glob
from tqdm import tqdm


def split_namuwiki(namuwiki_dump_path, data_root):
    with open(namuwiki_dump_path, 'rb') as f:
        namuwiki = json.load(f)

    print(f'Found {len(namuwiki)} items')  # 752884

    def get_path(index): 
        suffix = '{:07}'.format(index)[-3:] 
        path = f'{data_root}/{suffix}/{index}.json'
        return path

    def check_dir(path):
        dirname = os.path.abspath(os.path.dirname(path))
        if not os.path.exists(dirname):
            os.makedirs(dirname)

    iterator = tqdm(namuwiki, desc='split namuwiki')
    for index, item in enumerate(iterator):
        path = get_path(index)
        check_dir(path)
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(item, f, ensure_ascii=False, indent=2, sort_keys=True)


namuwiki_dump_path = './dump/namuwiki200302.json'
data_root = './data/'
