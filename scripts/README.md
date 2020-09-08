## Scripts for making namuwikitext

Check `namuwiki_dump_path` and `data_root` in `split_dump_to_json_files.py` which are dump data file path and root directory of result json files.

```
python split_dump_to_json_files.py
```

In `data_root`

```
├── 000
|    ├── ...
|    ├── 97000.json
|    ├── 98000.json
|    └── 99000.json
├── ...
├── 998
└── 999
```

To extract multiline (wikitext format) text, run following script. Check `data_root` and `text_root` in `extract_wikitext_from_json.py`.

```
python extract_wikitext_from_json.py
```

Snapshot of `text_root`. Redirected pages are removed

```
├── 000
|    ├── ...
|    ├── 97000.txt
|    ├── 98000.txt
|    └── 99000.txt
├── ...
├── 998
└── 999
```

Run below script to make `train`, `dev`, `test` dataset. Check `n_train`, `n_dev`, and `n_test` in `concatenate.py`

```
python concatenate.py
```
