# 起動方法
Docker+Poetry+Djangoにて起動
(WSL2でも起動可)

以下のコマンドでサーバーを起動
```
bash bin/build.sh
bash bin/run.sh
```

`http://127.0.0.1:8888`で接続可能

# ノートブックの起動の仕方
※初期はnotebookライブラリを追加する必要あり
```
poetry config virtualenvs.in-project true
```

Open Command palette (shift + ctrl + p)

Select "Jupyter: Select Interpreter to Start Jupyter Server"

Select ".venv"

VScodeのRootを作業ディレクトリ直下にしないと.venvが表示されないバグ有
(表示されない場合は`/root/.cache/`直下にあるvenvを手動で選択しても可)