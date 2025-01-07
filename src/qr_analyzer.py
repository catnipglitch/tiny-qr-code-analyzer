from PIL import Image
from pyzbar.pyzbar import decode

class QRCodeAnalyzer:
    """
    QRコードの解析を行うクラス。
    """

    def __init__(self):
        """
        コンストラクタ（現在は何も初期化しない）。
        """
        pass

    @staticmethod
    def from_image(image_source):
        """
        画像ファイルまたはバイトデータからQRコードを解析する静的メソッド。

        :param image_source: 画像ファイルのパスまたはバイトデータ
        :return: デコードされたQRコードデータ（文字列）またはNone
        """
        try:
            if isinstance(image_source, str):
                image = Image.open(image_source)
            else:
                image = Image.open(image_source)
            decoded_objects = decode(image)
            if decoded_objects:
                return decoded_objects[0].data.decode('utf-8')
        except Exception as e:
            print(f"画像の読み込みに失敗しました: {e}")
        return None

    @staticmethod
    def from_clipboard():
        """
        クリップボードから取得したテキストを返す静的メソッド。

        :return: クリップボード内のテキスト（文字列）
        """
        import pyperclip
        return pyperclip.paste()

    @staticmethod
    def from_webcam():
        """
        ウェブカメラでキャプチャした映像からQRコードを解析する静的メソッド。

        :return: デコードされたQRコードデータ（文字列）またはNone
        """
        import cv2
        from pyzbar.pyzbar import decode

        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            if not ret:  # 映像が取得できなかった場合
                break
            decoded_objects = decode(frame)
            for obj in decoded_objects:
                cap.release()
                return obj.data.decode('utf-8')  # 最初に見つかったQRコードを返す
            if cv2.waitKey(1) & 0xFF == ord('q'):  # 'q'キーで終了
                break
        cap.release()
        return None

