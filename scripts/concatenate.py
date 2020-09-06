import numpy as np
from glob import glob
from tqdm import tqdm


text_root = '../../text/'
namuwikidata_root = '../data/'

paths = sorted(glob(f'{text_root}/*/*.txt'))
print(f'Found {len(paths)} multiline texts')

n = len(paths)
np.random.seed(0)
indices = np.random.permutation(n)
n_train = int(0.99 * n)
n_dev = int(0.005 * n)
n_test = int(0.005 * n)
train_indices = indices[:n_train]
dev_indices = indices[n_train: n_train + n_dev]
test_indices = indices[n_train + n_dev:]

filename_paths = [
    (f'{namuwikidata_root}/namuwikitext_20200302.train', [paths[i] for i in train_indices]),
    (f'{namuwikidata_root}/namuwikitext_20200302.dev', [paths[i] for i in dev_indices]),
    (f'{namuwikidata_root}/namuwikitext_20200302.test', [paths[i] for i in test_indices]),
]


def concatenate(outpath, inpaths):
    with open(outpath, 'w', encoding='utf-8') as fo:
        for inpath in tqdm(inpaths, desc='concatenate', total=len(inpaths)):
            with open(inpath, encoding='utf-8') as f:
                inputs = f.read()
            fo.write(inputs)
            fo.write('\n')


for outpath, inpaths in filename_paths:
    concatenate(outpath, inpaths)
    print(f'saved at {outpath}')
