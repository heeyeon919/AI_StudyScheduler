# logic7_time_progress.py
# 과목별 공부 시간 배분 및 오늘 목표 진도 계산

from models import Subject
from typing import List


def calculate_logic7_time_progress(
    subjects: List[Subject],
    daily_available_hours: float
):
     # 과목이 없는 경우
    if len(subjects) == 0:
        return subjects
    
    # 전체 우선순위 합
    total_priority_sum = sum(
        subject.priority_score
        for subject in subjects
        if subject.priority_score is not None
    )

    #과목별 계산
    for subject in subjects:

        # 1. 추천 공부 시간 계산
        if total_priority_sum == 0:

            recommended_study_time = 0.0

        else:

            recommended_study_time = (
                (subject.priority_score / total_priority_sum)
                * daily_available_hours
            )

        # Subject 객체에 저장 (내부 저장은 원본 값 유지)
        subject.recommended_study_time = (
            recommended_study_time
        )

        # 2. 목표 진도 계산
        if subject.days_left <= 0:

            planned_progress = (
                subject.remaining_chapters
            )

        else:

            planned_progress = (
                (
                    subject.remaining_chapters
                    / subject.days_left
                )
                * (1 + subject.priority_score)
            )

            #최소 진도 보정
            planned_progress = max(
                0.5,
                planned_progress
            )

        # Subject 객체에 저장 (내부 저장은 원본 값 유지)
        subject.planned_progress = (
            planned_progress
        )

    return subjects


#내부 저장 시에는 원본 값 그대로 유지하고, 출력할 때만 반올림할 예정
#print(round(subject.recommended_study_time, 2))
#print(round(subject.planned_progress, 2))