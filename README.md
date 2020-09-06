# Namuwikitext

Wikitext format Korean corpus

Corpus size
- train: 38278040 lines (5.3G)
- dev: 197723 lines (28M)
- test: 193614 lines (29M)

To fetch data, run below script. Then three corpus, train / dev / test files are downloaded at `./data/`

```
python fetch.py
```

This corpus is licensed with `CC BY-NC-SA 2.0 KR` which Namuwiki is licensed. For detail, visit https://creativecommons.org/licenses/by-nc-sa/2.0/kr/

## Fetch and load using [Korpora](https://github.com/ko-nlp/Korpora)

Korpora is Korean Corpora Archives, implemented based on Python. We will provide the fetch / load function at `Korpora`

(Soon)
```
from Korpora import Korpora

namuwikitext = Korpora.load('namuwikitext')

# or
Korpora.fetch('namuwikitext')
```
