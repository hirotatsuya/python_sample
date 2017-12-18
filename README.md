# python_sample

## Requirements
- python 3.6.2
- pyenv 1.1.3
- pip 9.0.1
- pipenv 9.0.0

## First
- pipenvのインストール

```
pip install pipenv
```

- yarnのインストール

```
npm i -g yarn
```

## Setup
- `Pipfile`によりpythonのパッケージのインストール

```
pip install
```

- `package.json`によりnodeのパッケージのインストール

```
yarn
```

## Usage(python)
- pythonコードの実行

```
python (file_name).py
```

## Usage(pyenv)
- インストール可能なパッケージ一覧の取得

```
pyenv install -list
```

```
pyenv install -l
```

- パッケージのインストール

```
pyenv install (package_name)
```

- pyenvによりインストール済みのパッケージ一覧の取得

```
pyenv versions
```

- グローバル環境のpythonのバージョンを切り替える

```
pyenv global (version)
```

- ローカル環境(特定のディレクトリ内のみ)のpythonのバージョンを切り替える

```
pyenv local (version)
```

- pythonの格納場所の確認

```
pyenv which (target)
```

```
which (target)
```

## Usage(pip)
- pipのバージョン確認

```
pip --version
```

- helpの表示

```
pip help
```

- Python Package Index(pypi)にあるpythonのパッケージを検索する

```
pip search (target)
```

- パッケージをインストールする

```
pip install (target)
```

- インストール済みのパッケージ一覧の表示

```
pip list
```

- パッケージをアンインストールする

```
pip uninstall (target)
```

## Usage(pipenv)
- パッケージのインストール

```
pipenv install (package)
```

- 開発環境のみにパッケージをインストール

```
pipenv install --dev (package)
```

- 仮想環境でpythonの実行

```
pipenv run python (file_name).py
```
