from ultralytics import YOLO

def main():
    model = YOLO("yolo26n.pt")
    results = model.train(
        data="hand-keypoints.yaml",
        epochs=100,
        imgsz=640
    )

if __name__ == "__main__":
    main()