import json
import os
import re
from glob import glob
from tqdm import tqdm


doublespace_pattern = re.compile('\s+')
doubleline_pattern = re.compile('\n{2,}')


def split(s, begin_marker, end_marker):
    b = s.index(begin_marker)
    e = s.index(end_marker, b)
    prefix = s[:b]
    suffix = s[e + len(end_marker):]
    sub = s[b + len(begin_marker) : e]
    return prefix, sub, suffix


def detach_links(s):
    while '[[' in s and ']]' in s:
        prefix, sub, suffix = split(s, '[[', ']]')
        if sub[:2] == '파일':
            sub = ''
        if '|' in sub:
            sub = sub.split('|', 1)[-1]
        s = f'{prefix}{sub}{suffix}'
    return s


def detach_markers(s, begin_marker, end_marker):
    while (begin_marker in s) and (end_marker in s[s.index(begin_marker) + len(begin_marker):]):
        prefix, sub, suffix = split(s, begin_marker, end_marker)
        s = f'{prefix}{sub}{suffix}'
    return s


def remove_markers(s, begin_marker, end_marker):
    while (begin_marker in s) and (end_marker in s[s.index(begin_marker) + len(begin_marker):]):
        prefix, sub, suffix = split(s, begin_marker, end_marker)
        s = f'{prefix} {suffix}'
    return s

def space_markers(s, begin_marker, end_marker):
    s = s.replace(begin_marker, f' {begin_marker} ')
    s = s.replace(end_marker, f' {end_marker} ')
    return s


def normalize(s):
    s = detach_links(s)
    s = detach_markers(s, "'''", "'''")
    s = detach_markers(s, '[*', ']')
    s = detach_markers(s, "''", "''")
    s = detach_markers(s, '｢', '｣')
#     s = detach_markers(s, '[include(틀:상세 내용, 문서명=', ')]')
#     s = detach_markers(s, '[include(틀:상세 내용', ')]')
    s = detach_markers(s, '~~', '~~')
    s = remove_markers(s, '{{{', '}}}')
    s = remove_markers(s, '<', '>')
    s = remove_markers(s, '||', '||')
    s = remove_markers(s, '--', '--')
    s = remove_markers(s, '[include(틀', ')]')
    s = remove_markers(s, '[Include(틀', ')]')
    s = remove_markers(s, '[youtube', ']')
    s = remove_markers(s, '[Youtube', ']')
    s = remove_markers(s, '[br', ']')    
    s = remove_markers(s, '[ruby', ']')
    s = remove_markers(s, '[nicovideo', ']')
    s = space_markers(s, '(', ')')
    s = s.replace('[각주]', ' ')
    s = s.replace('( )', '')

    lines = [postprocess_each_line(line) for line in s.split('\n') if line.strip()]
    if lines[-1][:3] == '분류:':
        lines = lines[:-1]
    lines = [line for line in lines if line]
    if not lines:
        return ''
    s = '\n'.join(lines)
    if lines[0][:9] == '#redirect':
        return ''
    s = doubleline_pattern.sub('\n\n', s).strip()
    if s[0] == '=':
        s = f' {s}'
    return s


def postprocess_each_line(s):
    s = s.strip()
    if not s:
        return s
    if s[0] == '=' and s[-1] == '=':
        s = s.replace('=', ' =')
    else:
        s = s.replace('=', ' = ')
    while s and s[0] in '>▶*★☆-+':
        s = s[1:].strip()
    if s[:3] == '{{{':
        s = s[3:].strip()
    if s[-3:] == '}}}':
        s = s[:-3].strip()
    if s[-3:] == "'''":
        s = s[:-3].strip()
    if s[-2:] == '||':
        s = s[:-2].strip()
    s = doublespace_pattern.sub(' ', s)
    if s[:2] == ' =' and s[-2:] == ' =':
        s = f'\n{s}\n'
    elif s[:2] == '= ' and s[-2:] == ' =':
        s = f'\n {s}\n'
    return s


def get_wikitext_from(json_data):
    title = json_data['title']
    text = json_data['text']
    if '==' not in text:
        text = normalize(text)
    else:        
        text = normalize(text[text.index('=='):]) 
    wikitext = f' = {title} =\n\n{text}'
    has_text = len(text) > 0
    return wikitext, has_text


def check_dir(path):
    dirname = os.path.abspath(os.path.dirname(path))
    if not os.path.exists(dirname):
        os.makedirs(dirname)


## SCRIPTS ##
data_root = os.path.abspath('./data/')
text_root = os.path.abspath('./text/')
paths = glob(f'{data_root}/*/*.json')
print(f'Found {len(paths)} json files')

for inpath in tqdm(paths, desc='Extract wikitext', total=len(paths)):
    with open(inpath) as f:
        data = json.load(f)
    wikitext, has_text = get_wikitext_from(data)
    if not has_text:
        continue
    outpath = inpath.replace(data_root, text_root)[:-4] + 'txt'
    check_dir(outpath)
    with open(outpath, 'w', encoding='utf-8') as f:
        f.write(wikitext)
