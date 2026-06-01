# logic2_understanding.py
# 이해 부족도 계산
# 이해도 낮을수록 이해 부족도 높음 

from models import Subject

def calculate_logic2_understanding(
    subject: Subject
):
    # 이해 부족도 계산 (lack_of_understanding = 1 - understanding_rate)
    lack_of_understanding = (
        1.0 - subject.understanding_rate
    )

    # Subject 객체에 저장
    subject.lack_of_understanding = (
        lack_of_understanding
    )

    return subject
