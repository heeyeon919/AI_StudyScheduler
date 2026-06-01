# logic10_risk_analysis.py
# 위험 분석 및 재스케줄링 판단

from models import Subject
from constants import (
    SAFE_THRESHOLD,
    RISK_THRESHOLD
)


def calculate_logic10_risk_analysis(
    subject: Subject,
    actual_progress: float
):

    # planned_progress가 없는 경우 대비(ZeroDivisionError 방지)
    if (
        subject.planned_progress is None
        or
        subject.planned_progress <= 0
    ):

        planned_progress = 1.0

    else:

        planned_progress = (
            subject.planned_progress
        )

    # 실제 수행률 계산
    actual_completed_ratio = (
        actual_progress
        / planned_progress
    )

    # 수행률 최대 2.0 제한
    actual_completed_ratio = min(
        actual_completed_ratio,
        2.0
    )

    # Subject 객체에 저장
    subject.actual_completed_ratio = (
        actual_completed_ratio
    )

    # 위험 상태 분석
    if actual_completed_ratio >= SAFE_THRESHOLD:

        risk_status = "SAFE"
        reschedule_required = False

    elif actual_completed_ratio >= RISK_THRESHOLD:

        risk_status = "WARNING"
        reschedule_required = False

    else:

        risk_status = "DANGER"
        reschedule_required = True

    # Subject 객체에 저장
    subject.risk_status = (
        risk_status
    )

    subject.reschedule_required = (
        reschedule_required
    )

    return subject