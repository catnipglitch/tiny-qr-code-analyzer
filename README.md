# QR Code Analyzer

このプロジェクトは、画像ファイル、クリップボード、またはWEBカメラからQRコードを解析し、その結果を表示するデスクトップアプリケーションです。Tkinterを使用してGUIを構築しています。

## 機能

- 画像ファイルのパスを指定してQRコードを解析
- クリップボードからQRコードを解析
- WEBカメラを使用してQRコードを解析
- 解析結果をウィンドウ上に表示
- 解析結果をクリップボードにコピーする機能
- 入力内容をリセットする機能

## ファイル構成

```
qr-code-analyzer
├── src
│   ├── main.py          # アプリケーションのエントリーポイント
│   ├── qr_analyzer.py   # QRコード解析機能
│   └── utils.py         # 補助的な関数
├── requirements.txt      # プロジェクトの依存関係
└── README.md             # プロジェクトの説明
```

## 使用方法

1. 必要なライブラリをインストールします。
   ```
   pip install -r requirements.txt
   ```

2. アプリケーションを起動します。
   ```
   python src/main.py
   ```

3. GUIからQRコードを解析するための入力を行います。

## 依存関係

- opencv-python
- pyzbar
- Pillow
- tkinter

このプロジェクトは、QRコードの解析を簡単に行えるツールを提供します。