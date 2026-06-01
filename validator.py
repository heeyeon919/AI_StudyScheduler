# validator.py
# 사용자가 입력한 값이 올바른 범위, 허용된 값, 계산 가능한 상태인지 검사하는 역할

from datetime import date
from constants import (
    ALLOWED_COURSE_CATEGORY,
    ALLOWED_SUBJECT_TYPE,
    ALLOWED_TARGET_GRADE,
    ALLOWED_PREFERRED_STUDY_TIME
)


# =========================================
# Course Category Validation
# =========================================
def validate_course_category(course_category):

    return course_category in ALLOWED_COURSE_CATEGORY


# =========================================
# Subject Type Validation
# =========================================

def validate_subject_type(subject_type):

    return subject_type in ALLOWED_SUBJECT_TYPE


# =========================================
# Target Grade Validation
# =========================================

def validate_target_grade(target_grade):

    return target_grade in ALLOWED_TARGET_GRADE


# =========================================
# Preferred Study Time Validation
# =========================================

def validate_preferred_study_time(preferred_study_time):

    return preferred_study_time in ALLOWED_PREFERRED_STUDY_TIME


# =========================================
# Understanding Rate Validation
# Range : 0.0 ~ 1.0
# =========================================

def validate_understanding_rate(understanding_rate):
    return 0.0 <= understanding_rate <= 1.0


# =========================================
# Chapter Validation
# completed <= total
# =========================================

def validate_chapters(total_chapters, completed_chapters):

    return (
        total_chapters > 0 and
        0 <= completed_chapters <= total_chapters
    )


# =========================================
# Exam Weight Validation
# midterm + final == 1
# =========================================

def validate_exam_weight(midterm_weight, final_weight):

    return (
        0 <= midterm_weight <= 1
        and
        0 <= final_weight <= 1
        and
        abs(
            (midterm_weight + final_weight) - 1.0
        ) < 1e-6
    )


# =========================================
# Daily Available Hours Validation
# =========================================

def validate_daily_available_hours(hours):

    return 0 < hours <= 24


# =========================================
# Actual Completed Ratio Validation
# =========================================

def validate_actual_completed_ratio(ratio):

    if ratio is None:
        return True

    return 0 <= ratio <= 2.0

# =========================================
# Schedule Start Date Validation
# 오늘 이상이어야 함
# =========================================
def validate_schedule_start_date(schedule_start_date):

    return schedule_start_date >= date.today()

# =========================================
# UserConfig Object Validation
# 사용자 기본 설정 전체 검증
# =========================================
def validate_user_config(user_config):

    return (
        validate_daily_available_hours(
            user_config.daily_available_hours
        )
        and validate_preferred_study_time(
            user_config.preferred_study_time
        )
        and validate_schedule_start_date(
            user_config.schedule_start_date
        )
    )

# =========================================
# Exam Date Validation
# 시험 날짜는 오늘 이후
# =========================================
def validate_exam_date(exam_date):

    return exam_date > date.today()

# =========================================
# Last Studied Date Validation
# 마지막 공부 날짜는 오늘 이하 + 시험일 이하
# =========================================
def validate_last_studied_date(
    last_studied_date,
    exam_date
):

    return (
        last_studied_date <= date.today()
        and
        last_studied_date <= exam_date
    )

# =========================================
# Subject Object Validation
# Subject 전체 데이터 검증
# =========================================
def validate_subject(subject):
    
    return (
        validate_course_category(subject.course_category)
        and validate_subject_type(subject.subject_type)
        and validate_target_grade(subject.target_grade)
        and validate_understanding_rate(subject.understanding_rate)
        and validate_chapters(
            subject.total_chapters,
            subject.completed_chapters
        )
        and validate_exam_weight(
            subject.midterm_weight,
            subject.final_weight
        )
        and validate_exam_date(
            subject.exam_date
        )

        and validate_last_studied_date(
            subject.last_studied_date,
            subject.exam_date
        )
    )