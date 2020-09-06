import os
import zipfile
from tqdm import tqdm
from urllib import request


data_root = os.path.abspath(os.path.dirname(__file__))
data_root = os.path.abspath(os.path.join(data_root, '../data/'))
if not os.path.exists(data_root):
    os.makedirs(data_root)

local_zips = {
    'train': f'{data_root}/namuwikitext_20200302.train.zip',
    'dev': f'{data_root}/namuwikitext_20200302.dev.zip',
    'test': f'{data_root}/namuwikitext_20200302.test.zip'
}

local_texts = {
    'train': f'{data_root}/namuwikitext_20200302.train.txt',
    'dev': f'{data_root}/namuwikitext_20200302.dev.txt',
    'test': f'{data_root}/namuwikitext_20200302.test.txt'
}

NAMUWIKITEXT_URLS = {
    'train': 'https://korpora-archive.s3.ap-northeast-2.amazonaws.com/namuwikitext/namuwikitext_20200302.train.zip',
    'dev': 'https://korpora-archive.s3.ap-northeast-2.amazonaws.com/namuwikitext/namuwikitext_20200302.dev.zip',
    'test': 'https://korpora-archive.s3.ap-northeast-2.amazonaws.com/namuwikitext/namuwikitext_20200302.test.zip'
}


def fetch_all():
    for data_name in ['train', 'dev', 'test']:
        fetch(data_name)


def fetch(data_name):
    if data_name not in ['train', 'dev', 'test']:
        raise ValueError('Check `data_name` is one of ["train", "dev", "test"]')
    if os.path.exists(local_texts[data_name]):
        return True
    zippath = local_zips[data_name]
    if not os.path.exists(zippath):
        download(NAMUWIKITEXT_URLS[data_name], zippath, data_name)
        with zipfile.ZipFile(zippath, 'r') as zip_ref:
            zip_ref.extractall(data_root)
        print(f'unzip {data_name}')


def download(url, local_path, corpus_name):
    filename = os.path.basename(local_path)
    with tqdm(unit='B', unit_scale=True, miniters=1, desc=f'[{corpus_name}] download {filename}') as t:
        request.urlretrieve(url, filename=local_path, reporthook=_reporthook(t))


def _reporthook(t):
    """ ``reporthook`` to use with ``urllib.request`` that prints the process of the download.
    Uses ``tqdm`` for progress bar.
    **Reference:**
    https://github.com/tqdm/tqdm
    Args:
        t (tqdm.tqdm) Progress bar.
    Example:
        >>> with tqdm(unit='B', unit_scale=True, miniters=1, desc=filename) as t:  # doctest: +SKIP
        ...   urllib.request.urlretrieve(file_url, filename=full_path, reporthook=reporthook(t))
    """
    last_b = [0]

    def inner(b=1, bsize=1, tsize=None):
        """
        Args:
            b (int, optional): Number of blocks just transferred [default: 1].
            bsize (int, optional): Size of each block (in tqdm units) [default: 1].
            tsize (int, optional): Total size (in tqdm units). If [default: None] remains unchanged.
        """
        if tsize is not None:
            t.total = tsize
        t.update((b - last_b[0]) * bsize)
        last_b[0] = b

    return inner
