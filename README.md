# Namuwikitext

Wikitext format Korean corpus

나무위키의 덤프 데이터를 바탕을 제작한 wikitext 형식의 텍스트 파일입니다. 학습 및 평가를 위하여 위키페이지 별로 train (99%), dev (0.5%), test (0.5%) 로 나뉘어져있습니다.

Corpus size
- train: 38278040 lines (500104 docs, 5.3G)
- dev: 197723 lines (2525 docs, 28M)
- test: 193614 lines (2525 docs, 29M)

To fetch data, run below script. Then three corpus, train / dev / test files are downloaded at `./data/`

```
python fetch.py
```

This corpus is licensed with `CC BY-NC-SA 2.0 KR` which Namuwiki is licensed. For detail, visit https://creativecommons.org/licenses/by-nc-sa/2.0/kr/

## Fetch and load using [Korpora](https://github.com/ko-nlp/Korpora)

Korpora is Korean Corpora Archives, implemented based on Python. We will provide the fetch / load function at `Korpora`

이 코퍼스는 [`Korpora`](https://github.com/ko-nlp/Korpora) 프로젝트에서 사용할 수 있도록 작업 중입니다.

(Soon)
```
from Korpora import Korpora

namuwikitext = Korpora.load('namuwikitext')

# or
Korpora.fetch('namuwikitext')
```
