# Goggle sport scraping

Scrapt data to get result of rugby game

## Getting started

- Clone repo
- Create venv environment \
    Linux
    ```Bash
    python3 -m venv env
    source env/bin/activate
    ```

    Windows
    ```Bash
    python3 -m venv env
    env\Scripts\activate
    ```

- Install dependencies
    ```
    pip install -r requirements.txt
    ```

- Add .env file at root (ask for the file at someone who have it)

- Change language depending on your browser language in sport-scapper/extractData

## Build the library
regenerate requirements.txt if you added package
```
pip freeze > requirements.txt
```

install following package to build it
```
pip install wheel setuptools
```

build the library
```
python setup.py bdist_wheel
```

## Install it else where
```
pip install /path/to/wheelfile.whl
```
