import cv2
from ultralytics import YOLO

# carregar modelo treinado
model = YOLO("models/handsmodel.pt")  # ajuste o caminho se necessário

# abrir webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # rodar inferência
    results = model(frame)

    # desenhar resultado
    annotated_frame = results[0].plot()

    # mostrar na tela
    cv2.imshow("YOLO Pose - Webcam", annotated_frame)

    # sair com tecla q
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()