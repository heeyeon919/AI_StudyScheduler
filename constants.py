# constants.py
# 프로젝트 전체에서 공통으로 사용하는 가중치, enum, 기준값 저장하는 역할

# =========================================
# Course Category Weight
# Logic4 : importance_score calculation
# =========================================

CATEGORY_WEIGHT = {
    "MAJOR_REQUIRED": 1.5,
    "MAJOR_ELECTIVE": 1.2,
    "GENERAL": 1.0
}


# =========================================
# Grade Weight
# Logic4 : importance_score calculation
# =========================================

GRADE_WEIGHT = {
    "A+": 1.5,
    "A0": 1.4,
    "A-": 1.3,

    "B+": 1.2,
    "B0": 1.1,
    "B-": 1.0,

    "C+": 0.9,
    "C0": 0.8,
    "C-": 0.7,

    "D+": 0.6,
    "D0": 0.5,
    "D-": 0.4,

    "F": 0.0
}


# =========================================
# 과목 유형별 망각 계수
# Logic5 : forgetting curve calculation 
# 값이 작을수록 더 빨리 잊음
# =========================================

SUBJECT_TYPE_MEMORY_FACTOR = {
    "MEMORIZATION": 3,
    "PROBLEM_SOLVING": 5,
    "PROJECT": 7
}


# =========================================
# Review Threshold
# Logic9 : review recommendation
# If review_score >= REVIEW_THRESHOLD
# → review recommended
# =========================================

REVIEW_THRESHOLD = 0.5


# =========================================
# Risk Threshold(위험도 판단 기준)
# Logic10 : risk analysis
# If actual_completed_ratio < RISK_THRESHOLD
# → reschedule required

# actual_completed_ratio >= SAFE_THRESHOLD
# → SAFE

# RISK_THRESHOLD <= actual_completed_ratio < SAFE_THRESHOLD
# → WARNING

# actual_completed_ratio < RISK_THRESHOLD
# → DANGER + reschedule required

# =========================================

SAFE_THRESHOLD = 0.9
RISK_THRESHOLD = 0.6



# validator.py에서 입력 검사용으로 사용하기 위해서 ALLOWED_* 만듦
# =========================================
# Allowed Preferred Study Time
# =========================================

ALLOWED_PREFERRED_STUDY_TIME = [
    "MORNING",
    "AFTERNOON",
    "EVENING",
    "NIGHT"
]

# =========================================
# 시간대 설정 범위
# =========================================

PREFERRED_TIME_ZONE = {
    "MORNING": "06:00 ~ 12:00",
    "AFTERNOON": "12:00 ~ 18:00",
    "EVENING": "18:00 ~ 22:00",
    "NIGHT": "22:00 ~ 05:00"
}

# =========================================
# Allowed Course Category
# =========================================

ALLOWED_COURSE_CATEGORY = [
    "MAJOR_REQUIRED",
    "MAJOR_ELECTIVE",
    "GENERAL"
]


# =========================================
# Allowed Subject Type
# =========================================

ALLOWED_SUBJECT_TYPE = [
    "MEMORIZATION",
    "PROBLEM_SOLVING",
    "PROJECT"
]


# =========================================
# Allowed Target Grade
# =========================================

ALLOWED_TARGET_GRADE = [
    "A+",
    "A0",
    "A-",

    "B+",
    "B0",
    "B-",

    "C+",
    "C0",
    "C-",

    "D+",
    "D0",
    "D-",

    "F"
]