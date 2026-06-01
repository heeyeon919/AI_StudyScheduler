# input_handler.py
# 사용자에게 입력 받기 -> validator 검사 -> UserConfig / Subject 객체 생성
# -> 반환하는 역할

from datetime import datetime, date
from constants import (
    ALLOWED_TARGET_GRADE,
    ALLOWED_COURSE_CATEGORY,
    ALLOWED_SUBJECT_TYPE,
    ALLOWED_PREFERRED_STUDY_TIME
)
from models import UserConfig, Subject

from validator import (
    validate_understanding_rate,
    validate_user_config,
    validate_subject,
    validate_exam_weight,
    validate_daily_available_hours,
    validate_exam_date,
    validate_chapters,
    validate_last_studied_date,
    validate_schedule_start_date
)

# 사용자 기본 설정 입력 함수
def get_user_config():

    # 하루 공부 가능 시간 입력
    while True:
        try:
            daily_available_hours = float(
                input("하루 공부 가능 시간을 입력하세요 (0~24): ")
            )

            if validate_daily_available_hours(
                daily_available_hours
            ):
                break
            
            print("0~24 사이 값을 입력해야 합니다.")

        except ValueError:
            print("숫자를 입력해야 합니다.")

    # 스케줄 시작 날짜 입력
    while True:
        try:
            schedule_start_date = datetime.strptime(
                input("스케줄 시작 날짜 입력 (YYYY-MM-DD): "),
                "%Y-%m-%d"
            ).date()

            if validate_schedule_start_date(
                schedule_start_date
            ):
                break

            print("스케줄 시작 날짜는 오늘부터여야 합니다.")


        except ValueError:
            print("날짜 형식이 올바르지 않습니다.")

    # 선호 공부 시간대 입력
    while True:

        preferred_study_time = input(
            "선호 공부 시간대 입력 "
            "(MORNING / AFTERNOON / EVENING / NIGHT): "
        ).strip().upper()

        if preferred_study_time in ALLOWED_PREFERRED_STUDY_TIME:
            break

        print("올바른 시간대를 입력해야 합니다.")

    # 객체 생성
    user_config = UserConfig(
        daily_available_hours=daily_available_hours,
        schedule_start_date=schedule_start_date,
        preferred_study_time=preferred_study_time
    )

    # 최종 검증
    if not validate_user_config(user_config):
        print("잘못된 사용자 설정입니다.")
        return None

    return user_config

#과목 하나 입력받는 함수
def get_subject():
    while True:

        subject_name = input(
            "과목명 입력: "
        ).strip()

        if subject_name:
            break

        print("과목명을 입력해야 합니다.")

    while True:
        try:
            exam_date = datetime.strptime(
                input("시험 날짜 입력 (YYYY-MM-DD): "),
                "%Y-%m-%d"
            ).date()
            
            if validate_exam_date(exam_date):
                break
            
            print("시험 날짜는 오늘 이후여야 합니다.")


        except ValueError:
            print("날짜 형식이 올바르지 않습니다.")

    while True:
        course_category = input(
            "과목 유형 입력 (MAJOR_REQUIRED / MAJOR_ELECTIVE / GENERAL): "
        ).strip().upper()

        if course_category in ALLOWED_COURSE_CATEGORY:
            break

        print("올바른 과목 유형을 입력해야 합니다.")

    while True:
        subject_type = input(
            "과목 성격 입력 (MEMORIZATION / PROBLEM_SOLVING / PROJECT): "
        ).strip().upper()

        if subject_type in ALLOWED_SUBJECT_TYPE:
            break

        print("올바른 과목 성격을 입력해야 합니다.")
    
    while True:
        try:
            total_chapters = float(
                input("총 챕터 수 입력: ")
            )

            if total_chapters > 0:
                break

            print("총 챕터 수는 0보다 커야 합니다.")

        except ValueError:
            print("숫자를 입력해야 합니다.")
        
    while True:
        try:
            completed_chapters = float(
                input("완료 챕터 수 입력: ")
            )

            if validate_chapters(
                total_chapters,
                completed_chapters
            ):
                break
            
            print("완료 챕터 수는 0 이상 총 챕터 이하이어야 합니다.")

        except ValueError:
            print("숫자를 입력해야 합니다.")

    while True:
        try:
            understanding_rate = float(
                input("이해도 입력 (0~1): ")
            )

            if validate_understanding_rate(understanding_rate):
                break

            print("0~1 사이 값을 입력해야 합니다.")

        except ValueError:
            print("숫자를 입력해야 합니다.")
            

    while True:

        target_grade = input(
            "목표 학점 입력 (A+/A0/A- ~ F): "
        ).strip().upper()

        if target_grade in ALLOWED_TARGET_GRADE:
            break

        print("올바른 목표 학점을 입력해야 합니다.")
    
    while True:
        try:
            last_studied_date = datetime.strptime(
                input("마지막 공부 날짜 입력 (YYYY-MM-DD): "),
                "%Y-%m-%d"
            ).date()

            if validate_last_studied_date(
                last_studied_date,
                exam_date
            ):
                break

            print(
                "마지막 공부 날짜는 오늘 이하이며 "
                "시험 날짜 이전이어야 합니다."
            )

        except ValueError:
            print("날짜 형식이 올바르지 않습니다.")

    while True:

        try:
            midterm_weight = float(
                input("중간 비중 입력 (예: 0.4): ")
            )

            final_weight = float(
                input("기말 비중 입력 (예: 0.6): ")
            )

            if not (0 <= midterm_weight <= 1):
                print("중간 비중은 0~1 사이여야 합니다.")
                continue

            if not (0 <= final_weight <= 1):
                print("기말 비중은 0~1 사이여야 합니다.")
                continue

            if not validate_exam_weight(
                midterm_weight,
                final_weight
            ):
                print("중간/기말 비중 합은 1.0이어야 합니다.")
                continue

            break

        except ValueError:
            print("숫자를 입력해야 합니다.")


    subject = Subject(
        subject_name=subject_name,
        exam_date=exam_date,
        course_category=course_category,
        subject_type=subject_type,
        total_chapters=total_chapters,
        completed_chapters=completed_chapters,
        understanding_rate=understanding_rate,
        target_grade=target_grade,
        last_studied_date=last_studied_date,
        midterm_weight=midterm_weight,
        final_weight=final_weight
    )    

    # 최종 안전 검증
    if not validate_subject(subject):
        print("잘못된 과목 데이터입니다.")
        return None
    
    return subject


#여러 과목 입력 함수
def get_subjects():

    subjects = []

    while True:

        subject = get_subject()

        if subject is not None:
            subjects.append(subject)

        while True:

            more = input(
                "과목을 추가로 입력하시겠습니까? (Y/N): "
            ).strip().upper()

            if more == "Y":

                print("\n")
                break

            elif more == "N":

                print("\n")

                if len(subjects) > 0:
                    return subjects

                print("최소 1개 과목은 입력해야 합니다.")
                break

            else:
                print("\n")
                print("Y 또는 N만 입력 가능합니다.")