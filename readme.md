🏓 AI Pong: Controle por Gestos com YOLO e Pygame

Uma recriação do clássico jogo Pong onde o teclado foi substituído pelas suas próprias mãos. Este projeto utiliza Visão Computacional com um modelo YOLO treinado para rastrear pontos chave (keypoints) das mãos em tempo real via webcam, mapeando esses movimentos para controlar as raquetes no jogo.

## 🚀 Funcionalidades

* **Controle Corporal em Tempo Real:** Jogue usando a altura das suas mãos na frente da webcam.
* **Detecção Inteligente Esquerda/Direita (L/R):** O sistema identifica automaticamente qual mão está na esquerda e qual está na direita da tela para atribuir aos jogadores 1 e 2.
* **Janela de Debug com OpenCV:** Uma janela secundária exibe o feed da webcam com anotações do YOLO, bounding boxes, marcações "Hand L / Hand R" e a porcentagem da altura ($Y$) em tempo real.
* **Física Fluida:** Detecção de colisão aprimorada no Pygame para evitar bugs quando a bola bate na quina das raquetes.

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **Pygame:** Para a renderização do jogo, física da bola e sistema de pontuação.
* **OpenCV (`cv2`):** Para captura de vídeo da webcam e renderização da janela de anotações (debug).
* **Ultralytics (YOLO):** Para a inferência do modelo de detecção/pose das mãos.

## 📦 Como Instalar e Rodar

1. Clone este repositório:
   ```bash
   git clone https://github.com/DanEstren/pingpong-python
   cd pingpong-python
   
Crie um ambiente virtual (recomendado usar Anaconda ou venv) e instale as dependências:

2. Crie um ambiente virtual e instale as dependências

(Recomendado usar venv ou Anaconda)


pip install pygame opencv-python ultralytics


3. Execute o jogo

python pingpong.py


🧠 Como Funciona a Integração?

O projeto desacopla o sistema de input tradicional do Pygame. Em vez de ler eventos de teclado para calcular a velocidade da raquete, o loop principal lê um frame da webcam, passa pelo modelo YOLO, extrai as coordenadas $Y$ dos centros das mãos e faz uma conversão de escala proporcional (regra de três) entre a resolução da webcam e a resolução da tela do jogo (600x400). As variáveis de posição das raquetes são atualizadas em tempo real antes de cada renderização de frame.

🤝 Contribuição

Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias para a física do jogo ou modelos de detecção mais precisos!

Referencia

https://gist.github.com/vinothpandian/4337527

Dataset
https://www.kaggle.com/datasets/nomihsa965/hand-detection-dataset-vocyolo-format?resource=download

Como treinar está no trainer.py, é necessário extrair, e tirar da pasta yolo os labels.txt e colocar na pasta labels