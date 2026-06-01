
📂 AI_Study_Scheduler/
│
├── main.py   (프로그램 실행 및 Logic 1~10 흐름 제어)
├── constants.py  (가중치, 임계값 등 공통 상수 관리)
├── models.py (UserConfig, Subject 데이터 구조 정의)
├── input_handler.py (사용자 입력 처리 및 객체 생성)
├──validator.py (입력값 검증)
│
├── logic/
│   ├── logic1_urgency.py  (시험 긴급도 계산)
│   ├── logic2_understanding.py  (이해 부족도 계산)
│   ├── logic3_progress.py (남은 공부량 및 진도율 계산)
│   ├── logic4_importance.py (과목 중요도 계산)
│   ├── logic5_retention.py (망각곡선 기반 복습 필요도 계산)
│   ├── logic6_priority.py (최종 우선순위 산출)
│   ├── logic7_time_progress.py (공부 시간 및 목표 진도 배분)
│   ├── logic8_daily_schedule.py (일일 학습 스케줄 생성)
│   ├── logic9_review.py (복습 추천 여부 판단)
│   └── logic10_risk_analysis.py (학습 위험도 분석 및 재스케줄 판단)
└── __pycache__/   ( Python 실행 시 자동 생성)
