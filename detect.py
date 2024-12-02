import cv2
from yolov8 import YOLO
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', type=str, default='best.pt', help='Eğitilen model dosyası')
    parser.add_argument('--source', type=str, default='test_image.jpg', help='Test edilecek resim veya video yolu')
    return parser.parse_args()

def main():
    args = parse_args()
    model = YOLO(args.weights)
    image_path = args.source
    image = cv2.imread(image_path)
    results = model.predict(image)
    results.show()

    results.save('output.jpg')

if __name__ == "__main__":
    main()
