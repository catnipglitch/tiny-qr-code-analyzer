class QRCodeAnalyzer:
    def __init__(self):
        pass

    @staticmethod
    def from_image(image_path):
        from PIL import Image
        from pyzbar.pyzbar import decode

        image = Image.open(image_path)
        decoded_objects = decode(image)
        if decoded_objects:
            return decoded_objects[0].data.decode('utf-8')
        return None

    @staticmethod
    def from_clipboard():
        import pyperclip
        return pyperclip.paste()

    @staticmethod
    def from_webcam():
        import cv2
        from pyzbar.pyzbar import decode

        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            decoded_objects = decode(frame)
            for obj in decoded_objects:
                cap.release()
                return obj.data.decode('utf-8')
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        return None