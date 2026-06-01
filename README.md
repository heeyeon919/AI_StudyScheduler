## 🗓️ HAPS : Inteligent Scheduler

Hybrid AI Personalized Scheduler

## 🗓️ 데이터 구조 및 로직 정리

* 아래의 데이터 구조 및 로직 정리 파일을 바탕으로 코딩을 진행하였음. <br/>

[데이터 구조 및 로직 정리_20201012 조희연.pdf](https://github.com/user-attachments/files/28455468/_20201012.pdf)


## 📂 파일 구조

📂 AI_Study_Scheduler/ <br/>
│<br/>
├── main.py   (프로그램 실행 및 Logic 1~10 흐름 제어)<br/>
│<br/>
├── constants.py  (가중치, 임계값 등 공통 상수 관리)<br/>
├── models.py (UserConfig, Subject 데이터 구조 정의)<br/>
├── input_handler.py (사용자 입력 처리 및 객체 생성)<br/>
├── validator.py (입력값 검증)<br/>
│<br/>
├── logic/ <br/>
│   ├── logic1_urgency.py  (시험 긴급도 계산)<br/>
│   ├── logic2_understanding.py  (이해 부족도 계산)<br/>
│   ├── logic3_progress.py (남은 공부량 및 진도율 계산)<br/>
│   ├── logic4_importance.py (과목 중요도 계산)<br/>
│   ├── logic5_retention.py (망각곡선 기반 복습 필요도 계산)<br/>
│   ├── logic6_priority.py (최종 우선순위 산출)<br/>
│   ├── logic7_time_progress.py (공부 시간 및 목표 진도 배분)<br/>
│   ├── logic8_daily_schedule.py (일일 학습 스케줄 생성)<br/>
│   ├── logic9_review.py (복습 추천 여부 판단)<br/>
│   └── logic10_risk_analysis.py (학습 위험도 분석 및 재스케줄 판단)<br/>
│<br/>
└── __pycache__/   ( Python 실행 시 자동 생성)<br/>

## 🗓️ 로직 실행 흐름

입력 <br/>
 ↓<br/>
Logic1~5<br/>
 ↓<br/>
Logic6<br/>
 ↓<br/>
Logic7<br/>
 ↓<br/>
Logic8<br/>
 ↓<br/>
Logic9<br/>
 ↓<br/>
Logic10<br/>
 ↓<br/>
출력<br/>
