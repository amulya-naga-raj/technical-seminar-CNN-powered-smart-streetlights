import cv2

def preprocess_image(img_path):
    img = cv2.imread(img_path)
    img_resized = cv2.resize(img, (64, 64))
    img_normalized = img_resized / 255.0
    return img_normalized
