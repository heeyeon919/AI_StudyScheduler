# logic4_importance.py
# 중요도 계산

from models import Subject
from constants import (
    CATEGORY_WEIGHT,
    GRADE_WEIGHT
)


def calculate_logic4_importance(
    subject: Subject
):

    # 시험 비중 점수 계산 (exam_weight = (midterm_weight * 0.4) + (final_weight * 0.6))
    exam_weight = (
        (subject.midterm_weight * 0.4)
        + (subject.final_weight * 0.6)
    )

    # 과목 유형 가중치
    category_weight = CATEGORY_WEIGHT[
        subject.course_category
    ]

    # 목표 학점 가중치
    grade_weight = GRADE_WEIGHT[
        subject.target_grade
    ]

    # 중요도 계산 (importance_score = (category_weight * 0.4) + (grade_weight * 0.4) + (exam_weight * 0.2))
    importance_score = (
        (category_weight * 0.4)
        + (grade_weight * 0.4)
        + (exam_weight * 0.2)
    )

    # Subject 객체에 저장
    subject.importance_score = (
        importance_score
    )

    return subject