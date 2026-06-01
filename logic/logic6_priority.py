# logic6_priority.py
# 최종 우선순위 계산

from models import Subject
from typing import List


def calculate_logic6_priority_score(
    subjects: List[Subject]
):
    # 과목이 없는 경우
    if len(subjects) == 0:
        return subjects

    # 1. raw_score 계산
    for subject in subjects:

        # remaining_chapters가 없는 경우 계산
        if subject.remaining_chapters is None:

            subject.remaining_chapters = (
                subject.total_chapters
                - subject.completed_chapters
            )

        # 남은 진도 비율 계산
        remaining_ratio = (
            subject.remaining_chapters
            / subject.total_chapters
        )

        # Subject 객체에 저장
        subject.remaining_ratio = (
            remaining_ratio
        )

        # raw_score 계산
        raw_score = (
            (subject.urgency_score * 0.3)
            + (subject.importance_score * 0.3)
            + (subject.lack_of_understanding * 0.2)
            + (remaining_ratio * 0.2)
        )

        # Subject 객체에 저장
        subject.raw_score = raw_score

    # 2. Min-Max 정규화 준비
    raw_score_list = [
        subject.raw_score
        for subject in subjects
    ]

    max_raw = max(raw_score_list)
    min_raw = min(raw_score_list)

    # 3. priority_score 계산
    for subject in subjects:

        # 모든 과목 점수가 같은 경우
        if max_raw == min_raw:

            priority_score = 1.0

        else:

            priority_score = (
                (subject.raw_score - min_raw)
                / (max_raw - min_raw)
            )

        # Subject 객체에 저장
        subject.priority_score = (
            priority_score
        )

    return subjects