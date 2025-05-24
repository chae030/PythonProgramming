import socket
import numpy as np
import tensorflow as tf
from display_network_tf2 import Display

# 모델 로딩
MODEL_PATH = "models/mario_rnn_tf2_last.h5"
model = tf.keras.models.load_model(MODEL_PATH)

# Lua 기준 헤더 정보 (첫 줄: 32, 7, 4, 3)
header = ["32", "7", "4", "3"]
input_width = int(header[0])
input_height = int(header[1])
extra_inputs = int(header[2])
output_size = int(header[3])
input_dim = model.input_shape[-1]  # 248 expected

# Display 초기화
display = Display(input_width, input_height)

# 서버 설정
HOST = socket.gethostname()
PORT = 2222

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)
print(f"✅ 서버 실행 중: {HOST}:{PORT}")

try:
    while True:
        print("🎮 클라이언트 접속 대기 중...")
        clientsocket, address = server.accept()
        print(f"🔗 클라이언트 접속됨: {address}")

        try:
            # Lua 초기 헤더 응답 (필수)
            clientsocket.send((str(len(header)) + "\n").encode())
            for h in header:
                clientsocket.send((h + "\n").encode())

            while True:
                screen = ""
                while not screen.endswith("\n"):
                    chunk = clientsocket.recv(2048).decode('ascii')
                    if not chunk:
                        raise ConnectionError("클라이언트 연결 종료됨")
                    screen += chunk

                screen = screen.strip()
                values = screen.split(" ")

                if len(values) < input_dim:
                    print(f"❌ 입력 벡터 크기 부족: {len(values)} vs 기대값 {input_dim}")
                    clientsocket.send(b"close\n")
                    break
                elif len(values) > input_dim:
                    print(f"📥 입력 벡터 길이: {len(values)} (기대: {input_dim})")
                    print("⚠️ 초과 입력 감지 → 잘라서 처리.")
                    values = values[:input_dim]

                # 예측
                x_input = np.array(values, dtype=float).reshape(1, 1, input_dim)
                prediction = model.predict(x_input, verbose=0)[0]

                print("🔮 예측 결과:", prediction)

                # 시각화
                try:
                    display.update(list(map(float, values)), prediction)
                except Exception as e:
                    print("⚠️ 시각화 예외:", e)
                    break

                # 버튼 결과 전송
                buttons = ["1" if np.random.rand() < p else "0" for p in prediction]
                result = " ".join(buttons) + "\n"
                clientsocket.send(result.encode())

        except Exception as e:
            print("⚠️ 예외 발생:", e)
            try:
                clientsocket.send(b"close\n")
            except:
                pass
            clientsocket.close()

finally:
    server.close()
