# logic9_review.py
# 복습 추천 생성

from models import Subject
from constants import REVIEW_THRESHOLD


def calculate_logic9_review(
    subject: Subject
):

    # 복습 점수 계산
    review_score = (
        subject.retention_risk
        * subject.priority_score
    )

    # Subject 객체에 저장
    subject.review_score = (
        review_score
    )

    # 복습 여부 판단 (REVIEW_THRESHOLD = 0.5)
    if review_score >= REVIEW_THRESHOLD:

        review_status = "복습 추천"

    else:

        review_status = "우선 순위 낮음"

    # Subject 객체에 저장
    subject.review_status = (
        review_status
    )

    return subject