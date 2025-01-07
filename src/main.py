import tkinter as tk
from tkinter import filedialog, messagebox
from qr_analyzer import QRCodeAnalyzer
import pyperclip

class QRCodeAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QRコード解析アプリ")
        
        self.analyzer = QRCodeAnalyzer()
        
        self.result_text = tk.StringVar()
        
        self.create_widgets()
        
    def create_widgets(self):
        tk.Label(self.root, text="画像ファイルのパス:").pack()
        self.image_path_entry = tk.Entry(self.root, width=50)
        self.image_path_entry.pack()
        tk.Button(self.root, text="ファイル選択", command=self.select_file).pack()
        
        tk.Button(self.root, text="クリップボードから解析", command=self.analyze_from_clipboard).pack()
        tk.Button(self.root, text="WEBカメラから解析", command=self.analyze_from_webcam).pack()
        
        self.result_label = tk.Label(self.root, textvariable=self.result_text, wraplength=400)
        self.result_label.pack()
        
        self.copy_button = tk.Button(self.root, text="クリップボードにコピー", command=self.copy_to_clipboard, state=tk.DISABLED)
        self.copy_button.pack()
        
        tk.Button(self.root, text="リセット", command=self.reset).pack()
        
    def select_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image_path_entry.delete(0, tk.END)
            self.image_path_entry.insert(0, file_path)
            self.analyze_from_image(file_path)
    
    def analyze_from_image(self, image_path):
        result = self.analyzer.from_image(image_path)
        self.display_result(result)
    
    def analyze_from_clipboard(self):
        result = self.analyzer.from_clipboard()
        self.display_result(result)
    
    def analyze_from_webcam(self):
        result = self.analyzer.from_webcam()
        self.display_result(result)
    
    def display_result(self, result):
        self.result_text.set(result)
        self.copy_button.config(state=tk.NORMAL)
    
    def copy_to_clipboard(self):
        pyperclip.copy(self.result_text.get())
        messagebox.showinfo("情報", "結果をクリップボードにコピーしました。")
    
    def reset(self):
        self.image_path_entry.delete(0, tk.END)
        self.result_text.set("")
        self.copy_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeAnalyzerApp(root)
    root.mainloop()