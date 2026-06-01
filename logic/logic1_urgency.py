# logic1_urgency.py
# 시험 긴급도 계산

from datetime import date
from models import Subject

def calculate_logic1_urgency(
    subject: Subject, 
    schedule_start_date: date
):
    # 시험까지 남은 날짜 계산 (days_left = exam_date - schedule_start_date)
    days_left = (
        subject.exam_date - schedule_start_date
    ).days
    
    # 음수 방지
    days_left = max(days_left, 0)

    # 긴급도 계산 (urgency_score = 1/ (days_left + 1))
    urgency_score = 1 / (days_left + 1)
    
    # Subject 객체에 저장
    subject.days_left = days_left
    subject.urgency_score = urgency_score

    return subject