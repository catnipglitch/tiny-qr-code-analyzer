import tkinter as tk
from tkinter import filedialog, messagebox
from qr_analyzer import QRCodeAnalyzer
import pyperclip

class QRCodeAnalyzerApp:
    """
    QRコードを解析するGUIアプリケーションクラス。
    """

    def __init__(self, root):
        """
        アプリケーションの初期設定を行う。

        :param root: Tkinterのルートウィンドウ
        """
        self.root = root
        self.root.title("QRコード解析アプリ")
        
        # QRCodeAnalyzerのインスタンスを作成
        self.analyzer = QRCodeAnalyzer()
        
        # 結果表示用の文字列変数を定義
        self.result_text = tk.StringVar()
        
        # ウィジェットを作成
        self.create_widgets()

    def create_widgets(self):
        """
        アプリケーションで使用するウィジェットを作成および配置する。
        """
        tk.Label(self.root, text="画像ファイルのパス:").pack()
        self.image_path_entry = tk.Entry(self.root, width=50)
        self.image_path_entry.pack()
        tk.Button(self.root, text="ファイル選択", command=self.select_file).pack()
        
        tk.Button(self.root, text="クリップボードから解析", command=self.analyze_from_clipboard).pack()
        tk.Button(self.root, text="WEBカメラから解析", command=self.analyze_from_webcam).pack()
        
        self.result_label = tk.Label(self.root, textvariable=self.result_text, wraplength=400)
        self.result_label.pack()
        
        # コピー機能のボタン、デフォルトでは無効化
        self.copy_button = tk.Button(self.root, text="クリップボードにコピー", command=self.copy_to_clipboard, state=tk.DISABLED)
        self.copy_button.pack()
        
        # リセットボタンを作成
        tk.Button(self.root, text="リセット", command=self.reset).pack()

    def select_file(self):
        """
        ファイルダイアログを開いて、選択したファイルパスをエントリーに表示し、画像を解析する。
        """
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image_path_entry.delete(0, tk.END)
            self.image_path_entry.insert(0, file_path)
            self.analyze_from_image(file_path)

    def analyze_from_image(self, image_path):
        """
        画像ファイルからQRコードを解析して結果を表示する。

        :param image_path: 解析する画像のパス
        """
        result = self.analyzer.from_image(image_path)
        self.display_result(result)

    def analyze_from_clipboard(self):
        """
        クリップボード上のデータを解析して結果を表示する。
        """
        result = self.analyzer.from_clipboard()
        self.display_result(result)

    def analyze_from_webcam(self):
        """
        ウェブカメラを使用してQRコードを解析し、結果を表示する。
        """
        result = self.analyzer.from_webcam()
        self.display_result(result)

    def display_result(self, result):
        """
        解析結果をラベルに表示し、コピー機能を有効化する。

        :param result: 解析された結果（文字列）
        """
        self.result_text.set(result)
        self.copy_button.config(state=tk.NORMAL)

    def copy_to_clipboard(self):
        """
        表示されている結果をクリップボードにコピーする。
        """
        pyperclip.copy(self.result_text.get())
        messagebox.showinfo("情報", "結果をクリップボードにコピーしました。")

    def reset(self):
        """
        入力フィールドと結果表示をリセットする。
        """
        self.image_path_entry.delete(0, tk.END)
        self.result_text.set("")
        self.copy_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    # アプリケーションを開始するためのエントリーポイント
    root = tk.Tk()
    app = QRCodeAnalyzerApp(root)
    root.mainloop()
