def copy_to_clipboard(text):
    """
    テキストをクリップボードにコピーする関数。

    :param text: コピーするテキスト（文字列）
    """
    import pyperclip
    pyperclip.copy(text)

def reset_fields(*fields):
    """
    指定された入力フィールドをリセットする関数。

    :param fields: リセットするフィールドの可変引数リスト
    """
    for field in fields:
        field.delete(0, 'end')  # 入力フィールドをクリア
        field.insert(0, '')     # 空文字列にリセット

def show_messagebox(message):
    """
    情報メッセージを表示するためのメッセージボックスを表示する関数。

    :param message: 表示するメッセージ（文字列）
    """
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()  # ルートウィンドウを非表示にする
    messagebox.showinfo("Information", message)
    root.destroy()    # メッセージ表示後、ルートウィンドウを破棄
