
# Text Cleaner

## 概要 / Overview

日本語：
Text Cleanerは、テキストの行末の空白や連続する空行を整理するPython製コマンドラインツールです。
重複した行の削除や空行の削除にも対応しています。

English:
Text Cleaner is a Python command-line tool that cleans trailing whitespace and repeated blank lines.
It also supports removing duplicate lines and empty lines.

## 機能 / Features

- 行末の空白を削除 / Remove trailing whitespace
- 連続する空行を整理 / Remove repeated blank lines
- 重複した行を削除 / Remove duplicate lines
- 空行をすべて削除 / Remove all empty lines
- 標準入力と標準出力に対応 / Supports standard input and output

## 使用方法 / Usage

### 通常のテキスト整理

```bash
echo "Hello   " | python3 text_cleaner.py
```

### 重複行の削除

```bash
printf "Apple\nBanana\nApple\n" | python3 text_cleaner.py -r
```

### 空行の削除

```bash
printf "Apple\n\nBanana\n" | python3 text_cleaner.py -e
```

### ヘルプ

```bash
python3 text_cleaner.py -h
```

## テスト / Tests

```bash
./test.bash
```

## ライセンス / License

MIT License
