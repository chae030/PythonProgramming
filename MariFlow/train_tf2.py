import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import os

# 여러 파일에서 데이터를 로드하고 병합
def load_multiple_files(paths):
    all_X, all_y = [], []
    input_size, output_size = None, None

    for path in paths:
        print(f"📂 로딩 중: {path}")
        with open(path, "r") as f:
            lines = [line.strip() for line in f if line.strip() and not line.startswith("#")]

        header = lines[0].split()
        input_width = int(header[0])
        input_height = int(header[1])
        extra_inputs = int(header[2])
        output_size_curr = int(header[3])

        input_size_curr = input_width * input_height + extra_inputs
        if input_size is None:
            input_size, output_size = input_size_curr, output_size_curr
            print(f"🧠 입력 크기: {input_size}, 출력 크기: {output_size}")
        else:
            assert input_size == input_size_curr, f"⚠️ Input size mismatch in {path}"
            assert output_size == output_size_curr, f"⚠️ Output size mismatch in {path}"

        samples = []
        i = 1
        while i < len(lines):
            if lines[i].lower().startswith("session"):
                i += 1
                continue

            screen = []
            while len(screen) < input_size:
                screen += [float(v) for v in lines[i].split()]
                i += 1

            buttons = [float(v) for v in lines[i].split()]
            i += 1

            if len(screen) == input_size and len(buttons) == output_size:
                samples.append((screen, buttons))

        print(f"✅ {path}에서 {len(samples)}개 샘플 로드 완료")

        X = [s[0] for s in samples]
        y = [s[1] for s in samples]
        all_X.extend(X)
        all_y.extend(y)

    return np.array(all_X), np.array(all_y), input_size, output_size

# 모델 정의
def build_model(input_dim, output_dim):
    print(f"📐 모델 생성 중: 입력 {input_dim} → 출력 {output_dim}")
    model = Sequential([
        tf.keras.layers.Input(shape=(1, input_dim)),
        LSTM(64),
        Dense(output_dim, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy')
    model.summary()
    return model

# 학습 함수
def train():
    data_dir = "data"
    filenames = [
        "TiltedFixed.txt",
        "TiltedFixed2.txt",
        "TiltedFixed3.txt",
        "TiltedFixed4.txt"
    ]
    paths = [os.path.join(data_dir, name) for name in filenames]

    print("🚀 데이터 로드 시작")
    X, y, input_size, output_size = load_multiple_files(paths)
    print(f"📊 전체 샘플 수: {X.shape[0]}")
    print(f"X shape: {X.shape}, y shape: {y.shape}")

    # ✅ y 값 확인 및 정규화
    print(f"✅ y 값 범위: min={np.min(y)}, max={np.max(y)}")
    if np.min(y) < 0 or np.max(y) > 1:
        print("⚠️ y 값이 0~1 범위 밖에 있음 → 정규화 수행")
        y = np.clip(y, 0, 1)  # 또는 필요한 경우 이진화: (y > 0.5).astype(float)


    X = X.reshape((X.shape[0], 1, input_size))  # LSTM 입력

    print("🛠️ 모델 빌드 및 학습 시작")
    model = build_model(input_size, output_size)
    model.fit(X, y, epochs=100, batch_size=16)
    
    model.save("models/mario_rnn_tf2_last.h5")
    print("✅ 모델이 저장되었습니다: models/mario_rnn_tf2_last.h5")

# 메인 실행
if __name__ == "__main__":
    train()
