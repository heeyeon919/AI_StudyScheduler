# logic5_retention.py
# 복습 필요도 계산 (망각곡선 기반)

import math
from datetime import date

from models import Subject
from constants import (
    SUBJECT_TYPE_MEMORY_FACTOR
)


def calculate_logic5_retention_risk(
    subject: Subject,
    schedule_start_date: date
):

    # 마지막 학습 이후 경과일 계산 (elapsed_days = schedule_start_date - last_studied_date)
    elapsed_days = (
        schedule_start_date
        - subject.last_studied_date
    ).days

    # 음수 방지
    elapsed_days = max(elapsed_days, 0)

    # 과목 유형별 기억 유지 계수 (S값)
    memory_factor = (
        SUBJECT_TYPE_MEMORY_FACTOR[
            subject.subject_type
        ]
    )

    # 망각 위험도 계산 (retention_risk = 1 - e^(-t/S))
    retention_risk = ( 
        1.0
        - math.exp(
            -elapsed_days / memory_factor
        )
    )

    # Subject 객체에 저장
    subject.retention_risk = (
        retention_risk
    )

    return subject