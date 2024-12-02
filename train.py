import torch
from yolov8 import YOLO
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=str, default='stop_sign.yaml', help='Veri seti dosyası')
    parser.add_argument('--cfg', type=str, default='yolov8.cfg', help='YOLOv8 yapılandırma dosyası')
    parser.add_argument('--weights', type=str, default='yolov8.weights', help='Önceden eğitilmiş ağırlık dosyası')
    parser.add_argument('--batch-size', type=int, default=16, help='Batch boyutu')
    parser.add_argument('--epochs', type=int, default=50, help='Eğitim epoch sayısı')
    return parser.parse_args()

def main():
    args = parse_args()
    model = YOLO(args.cfg)
    model.load_weights(args.weights)
    data = args.data
    model.train(data=data, batch_size=args.batch_size, epochs=args.epochs)

if __name__ == "__main__":
    main()
