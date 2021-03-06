# Namuwikitext

Wikitext format Korean corpus

나무위키의 덤프 데이터를 바탕을 제작한 wikitext 형식의 텍스트 파일입니다. 학습 및 평가를 위하여 위키페이지 별로 train (99%), dev (0.5%), test (0.5%) 로 나뉘어져있습니다.

Corpus size
- train: 31235096 lines (500104 docs, 4.6G)
- dev: 153605 lines (2525 docs, 23M)
- test: 160233 lines (2527 docs, 24M)

To fetch data, run below script. Then three corpus, train / dev / test files are downloaded at `./data/`

```
python fetch.py
```

This corpus is licensed with `CC BY-NC-SA 2.0 KR` which Namuwiki is licensed. For detail, visit https://creativecommons.org/licenses/by-nc-sa/2.0/kr/

## Fetch and load using [Korpora](https://github.com/ko-nlp/Korpora)

Korpora is Korean Corpora Archives, implemented based on Python. We provide the fetch / load function at `Korpora`

이 코퍼스는 [`Korpora`](https://github.com/ko-nlp/Korpora) 프로젝트에서 사용할 수 있습니다.

```python
from Korpora import Korpora

namuwikitext = Korpora.load('namuwikitext')

# or
Korpora.fetch('namuwikitext')
```

## License

["CC BY-NC-SA 2.0 KR](https://creativecommons.org/licenses/by-nc-sa/2.0/kr/") which [Namuwiki dump dataset](https://namu.wiki/w/%EB%82%98%EB%AC%B4%EC%9C%84%ED%82%A4:%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4%20%EB%8D%A4%ED%94%84) is licensed

