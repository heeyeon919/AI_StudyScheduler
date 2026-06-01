# logic8_daily_schedule.py
# 전체 스케줄 생성

from models import Subject
from typing import List
from constants import PREFERRED_TIME_ZONE
from datetime import datetime, timedelta


SESSION_STYLE_MAP = {
    "MEMORIZATION": "짧고 반복적인 세션",
    "PROBLEM_SOLVING": "긴 집중 블록",
    "PROJECT": "장기 분산 블록"
}


def calculate_logic8_daily_schedule(
    subjects: List[Subject],
    preferred_study_time: str,
    daily_available_hours: float
):

    # 과목이 없는 경우
    if len(subjects) == 0:
        return subjects

    # 우선순위 기준 내림차순 정렬
    sorted_subjects = sorted(
        subjects,
        key=lambda subject: subject.priority_score,
        reverse=True
    )

    # 선호 시간대
    preferred_time_zone = (
        PREFERRED_TIME_ZONE[
            preferred_study_time
        ]
    )

    start_str, end_str = ( 
        preferred_time_zone.split(" ~ ") 
    )

    base_date = datetime.today().date()

    current_time = datetime.combine(
        base_date,
        datetime.strptime(start_str, "%H:%M").time()
    )

    daily_end = (
        current_time
        + timedelta(hours=daily_available_hours)
    )
    
    # NIGHT는 다음날 05:00으로 처리 
    if preferred_study_time == "NIGHT": 
        preferred_end = datetime.combine(
            base_date + timedelta(days=1),
            datetime.strptime("05:00", "%H:%M").time()
        )
    
    else: 
        preferred_end = datetime.combine(
            base_date,
            datetime.strptime(end_str, "%H:%M").time()
        )

    # 스케줄 생성
    for subject in sorted_subjects:

        # 추천 공부 시간이 없는 경우
        if (
            subject.recommended_study_time is None
            or
            subject.recommended_study_time <= 0
        ):

            subject.daily_schedule = []
            continue

        # 과목 유형별 공부 스타일
        session_style = SESSION_STYLE_MAP.get(
            subject.subject_type,
            "일반 학습 블록"
        )

        study_minutes = int(
            subject.recommended_study_time * 60
        )

        start_time = current_time

        end_time = (
            current_time
            + timedelta(minutes=study_minutes)
        )

        # 선호 시간대 내부인지 검사
        if start_time >= daily_end:

            assigned_time_zone = (
                "오늘 배정 불가"
            )

            start_time_str = None
            end_time_str = None
        
        #선호 시간대 내부
        elif end_time <= preferred_end:

            assigned_time_zone = (
                preferred_time_zone
            )

            start_time_str = (
                start_time.strftime("%H:%M")
            )

            end_time_str = (
                end_time.strftime("%H:%M")
            )
            
        else:

            assigned_time_zone = (
                "선호 시간대 초과"
            )   

            start_time_str = (
                start_time.strftime("%H:%M")
            )

            end_time_str = (
                end_time.strftime("%H:%M")
            )


        # daily_schedule 생성
        subject.daily_schedule = [
            {
                "task_name":
                    f"{subject.subject_name} 학습",

                "allocated_time":
                    subject.recommended_study_time,

                "planned_progress":
                    subject.planned_progress,

                "session_style":
                    session_style,

                "assigned_time_zone":
                    assigned_time_zone,
                
                "start_time":
                    start_time_str,

                "end_time":
                    end_time_str
            }
        ]

        if assigned_time_zone != "오늘 배정 불가":
            current_time = end_time
 
    return sorted_subjects