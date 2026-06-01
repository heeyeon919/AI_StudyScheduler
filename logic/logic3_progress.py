# logic3_progress.py
# 남은 공부량 및 진도율 계산

from models import Subject


def calculate_logic3_progress(
    subject: Subject
):

    # 남은 챕터(범위) 계산 (remaining_chapters = total_chapters - completed_chapters)
    remaining_chapters = (
        subject.total_chapters
        - subject.completed_chapters
    )

    # 현재 진도율 계산 (progress_rate = completed_chapters / total_chapters)
    progress_rate = (
        subject.completed_chapters
        / subject.total_chapters
    )

    # Subject 객체에 저장
    subject.remaining_chapters = (
        remaining_chapters
    )

    subject.progress_rate = (
        progress_rate
    )

    return subject