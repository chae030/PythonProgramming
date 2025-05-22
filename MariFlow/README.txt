[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/5RZmMF-I)
# MariFlow 재현 프로젝트

MariFlow 재현 프로젝트에 환영합니다! Seth Bling의 [MariFlow 영상](https://youtu.be/Ipi40cb_RsI)에서 아이디어를 얻어, 여러분은 Python을 사용해 *Mario Kart*를 자율적으로 플레이하는 순환 신경망(RNN) 시스템을 재현해 봅시다. 이 프로젝트는 Python 프로그래밍, 머신 러닝, 게임 자동화를 결합한 것으로, 여러분의 실력을 한 단계 끌어올리기에 완벽합니다.

## 프로젝트 개요
- **목표**: Python 기반 RNN을 구축하여 *Mario Kart* 에뮬레이터를 제어하고, 인간의 플레이를 모방해 트랙을 주행하도록 훈련시키기.
- **참고**: SethBling의 [MariFlow 영상](https://youtu.be/Ipi40cb_RsI)을 시청해 원본을 확인하세요.
- **참여**:
  - B 이상을 목표로 하는 고학년 학생들에게는 필수.
- **성적 기준 (고학년 학생)**:
  - **최대 B**: 환경 설정 완료 (에뮬레이터 + Python 연동).
  - **최대 A**: *Mario Kart*에서 주행 가능한 RNN 모델 훈련.
- **발표**: 5~10분 분량으로 작업물을 시연하고 코드를 설명.
- **LLM 사용**: AI 도구(예: Grok) 사용 가능, 단 모든 코드를 완전히 이해하고 설명할 수 있어야 함.

## 주요 단계

### 1. 환경 설정 (최대 성적: B)
- **목표**: Python으로 *Mario Kart*를 에뮬레이터에서 제어하기.
- **과제**:
  1. Python (3.8 이상), TensorFlow 또는 PyTorch, 필요 라이브러리 설치.
  2. 에뮬레이터(예: BizHawk, RetroArch)와 합법적으로 구한 *Mario Kart* ROM 설정.
  3. 기본 입력(예: 가속, 조향)을 보내고 게임 상태(예: 화면 픽셀)를 읽는 스크립트 작성.
- **결과물**: 최소 10초 동안 Mario를 움직이는 Python 스크립트.
- **팁**: 간단한 입력 시뮬레이션(예: `pyautogui`)으로 시작한 뒤 에뮬레이터 API로 전환.

### 2. 모델 훈련 (최대 성적: A)
- **목표**: 자율 주행을 위한 RNN 훈련.
- **과제**:
  1. 10~15분 분량의 본인 *Mario Kart* 플레이 데이터(입력 + 화면 상태) 녹화.
  2. 게임 상태에서 행동을 예측하는 RNN(예: LSTM) 구축.
  3. 데이터를 사용해 모델 훈련.
  4. 에뮬레이터에서 테스트하고 필요 시 조정.
- **결과물**: 트랙에서 Mario를 주행시키는 모델 (충돌해도 괜찮음, 움직이기만 하면 됨!).
- **팁**: 입력/출력을 단순화(예: 좌, 우, 직진 3가지 행동)해 관리 용이하게.

### 자원자용 과제
- **과제**: 기본 *Mario Kart* 입력(예: 가속 + 무작위 조향)을 자동화하는 간단한 스크립트 작성.
- **결과물**: Mario가 30초 동안 움직이는 스크립트.

## 요구 사항
- **도구**:
  - Python 3.8 이상
  - TensorFlow 또는 PyTorch (RNN용)
  - 에뮬레이터: BizHawk, RetroArch 등
  - *Mario Kart* ROM (합법적 소스)
  - 선택: `pyautogui`, `gym-retro`, 또는 에뮬레이터 전용 라이브러리
- **기간**:
  - 고학년 학생: 05/19 월 ~ 23 금 주간
- **제출**: 코드, 데모 영상(또는 실시간 데모), 발표 자료.

## 시작하기
1. [SethBling의 MariFlow 영상](https://youtu.be/Ipi40cb_RsI)을 보고 아이디어 이해.
1. Python과 선택한 ML 프레임워크 설치.
1. 에뮬레이터를 설정하고 기본 입출력을 스크립트로 테스트.
1. 플레이 데이터를 수집하고 RNN 구축 시작.

## 참고 자료
- [SethBling의 MariFlow 영상](https://youtu.be/Ipi40cb_RsI) – 원본 프로젝트 설명.
- [TensorFlow LSTM 튜토리얼](https://www.tensorflow.org/tutorials/structured_data/time_series) – RNN 기초.
- [PyTorch RNN 문서](https://pytorch.org/docs/stable/nn.html#recurrent-layers) – 대체 프레임워크 가이드.
- [BizHawk 에뮬레이터](http://tasvideos.org/BizHawk.html) – 에뮬레이터 설정 및 스크립팅 정보.
- GitHub: `MarI/O` 저장소(예: `pakoito/MarI-O`) 검색해 에뮬레이터 연동 아이디어 참고.

## 발표 가이드라인
- **시간**: 5~10분.
- **내용**: 데모 시연, 코드 설명, 접근 방식 설명.
- **질의응답**: 코드의 모든 행 설명 준비—특히 LLM 사용 시 주의!

## 팁
- 시작은 작게: 한 트랙과 기본 행동으로 테스트.
- 조기 디버깅: 에뮬레이터와 Python 연결을 훈련 전에 확인.
- 코드 문서화: 발표 시 도움이 됨.

행운을 빌며, Mario를 AI로 즐겁게 달리게 해보세요!

(위 문서 작성은 Grok3 의 도움을 받았음을 밝혀 둡니다.)
