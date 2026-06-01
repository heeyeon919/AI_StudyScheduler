# main.py

from input_handler import (
    get_user_config,
    get_subjects
)

from logic.logic1_urgency import calculate_logic1_urgency
from logic.logic2_understanding import calculate_logic2_understanding
from logic.logic3_progress import calculate_logic3_progress
from logic.logic4_importance import calculate_logic4_importance
from logic.logic5_retention import calculate_logic5_retention_risk
from logic.logic6_priority import calculate_logic6_priority_score
from logic.logic7_time_progress import calculate_logic7_time_progress
from logic.logic8_daily_schedule import calculate_logic8_daily_schedule
from logic.logic9_review import calculate_logic9_review
from logic.logic10_risk_analysis import calculate_logic10_risk_analysis

def main():
    print("===== AI 학습 스케줄러 =====")

    # 사용자 설정 입력
    user_config = get_user_config()
    if user_config is None:
        print("사용자 설정 입력 실패")
        return

    print("\n[사용자 설정 완료]")
    print(f"하루 공부 가능 시간: {user_config.daily_available_hours}시간")
    print(f"스케줄 시작 날짜: {user_config.schedule_start_date}")
    print(f"선호 공부 시간대: {user_config.preferred_study_time}\n\n")

    # 과목 입력
    subjects = get_subjects()
    if not subjects:
        print("입력된 과목이 없습니다.")
        return

    # Logic 1 ~ 5
    for subject in subjects:

        calculate_logic1_urgency(
            subject,
            user_config.schedule_start_date
        )

        calculate_logic2_understanding(
            subject
        )

        calculate_logic3_progress(
            subject
        )

        calculate_logic4_importance(
            subject
        )

        calculate_logic5_retention_risk(
            subject,
            user_config.schedule_start_date
        )

    # Logic 6
    calculate_logic6_priority_score(
        subjects
    )

    # Logic 7
    calculate_logic7_time_progress(
        subjects,
        user_config.daily_available_hours
    )

    # ----------------------------------------------------
    # Logic 8: 전체 스케줄 생성 및 과목 배분
    # ----------------------------------------------------
    scheduled_subjects = calculate_logic8_daily_schedule(
        subjects,
        user_config.preferred_study_time,
        user_config.daily_available_hours
    )

    print("\n" + "="*40)
    print(" 오늘 생성된 AI 최적 학습 스케줄 ")
    print("="*40)
    for idx, subj in enumerate(scheduled_subjects, start=1):
        print(
            f"\n순위 {idx}. "
            f"[{subj.subject_name}] "
            f"(우선순위 점수: {round(subj.priority_score, 2)})"
        )

        print(f"  - 과목 유형: {subj.subject_type} | 목표 학점: {subj.target_grade}")
        if subj.daily_schedule:
            for item in subj.daily_schedule:

                print(
                    f"  - 권장 공부 시간: "
                    f"{round(item['allocated_time'], 2)}시간"
                )

                print(
                    f"  - 오늘 목표 진도: "
                    f"{round(item['planned_progress'], 2)} 챕터"
                )

                print(
                    f"  - 스케줄링 스타일: "
                    f"{item['session_style']}"
                )

                if item["assigned_time_zone"] == "오늘 배정 불가":

                    print(
                        "  - 오늘 배정 불가 "
                        "(하루 공부 가능 시간 초과)"
                    )

                elif item["assigned_time_zone"] == "선호 시간대 초과":

                    print(
                        f"  - 실제 학습 시간: "
                        f"{item['start_time']} ~ {item['end_time']}"
                    )

                    print(
                        "  - 선호 시간대 초과"
                    )

                else:

                    print(
                        f"  - 실제 학습 시간: "
                        f"{item['start_time']} ~ {item['end_time']}"
                    )
        else:
            print("  - 오늘 배정된 스케줄이 없습니다.")

    # ----------------------------------------------------
    # Logic 9: 망각곡선 기반 복습 추천 출력
    # ----------------------------------------------------
    print("\n" + "="*40)
    print(" 오늘 자 망각곡선 기반 복습 추천 목록 ")
    print("="*40)
    recommendation_count = 0
    for subj in scheduled_subjects:
        calculate_logic9_review(subj)
        if subj.review_status == "복습 추천":
            recommendation_count += 1
            print(
                f"  ★ [복습 추천] "
                f"{subj.subject_name} "
                f"(복습 점수: {round(subj.review_score, 2)})"
            )

    if recommendation_count == 0:
        print("  - 오늘 꼭 복습해야 하는 고위험 과목이 없습니다. 진도 학습에 집중하세요!")

    # ----------------------------------------------------
    # Logic 10: 실제 수행 기록 입력 및 위험 분석
    # ----------------------------------------------------
    print("\n" + "="*40)
    print(" 오늘 자 학습 수행 기록 입력 및 위험도 분석 ")
    print("="*40)
    print("오늘 각 과목별 실제 공부한 진도(챕터)를 입력해 주세요.")
    
    for subj in scheduled_subjects:
        if not subj.daily_schedule:
            continue
            
        planned_p = (
            subj.daily_schedule[0]['planned_progress']
        )

        print(
            f"\n▶ 과목명: {subj.subject_name} "
            f" (목표 진도: {round(planned_p, 2)} 챕터)"
        )
        
        while True:
            try:
                actual_p = float(input(f"   실제 완료한 챕터 수를 입력하세요: "))
                if actual_p >= 0:
                    break
                print("   0 이상의 숫자를 입력해야 합니다.")
            except ValueError:
                print("   올바른 숫자를 입력해 주세요.")
                
        # 위험 분석 함수 호출
        calculate_logic10_risk_analysis(
            subj,
            actual_p
        )
        
        # 분석 결과 출력
        print(
            f"   [분석 결과] 실제 수행률: "
            f"{round(subj.actual_completed_ratio * 100, 1)}%"
        )
        if subj.risk_status == "SAFE":
            print("   💚 상태: SAFE (계획대로 아주 잘하고 있습니다!)")
        elif subj.risk_status == "WARNING":
            print("   💛 상태: WARNING (진도가 조금 밀렸으니 주의하세요.)")
        elif subj.risk_status == "DANGER":
            print("   🚨 상태: DANGER (진도가 많이 밀렸습니다!)")
            print("   ⚠️ 알림: 다음 일정 생성 시 [재스케줄링(Reschedule)]이 실행됩니다.")

#?
    print("\n" + "=" * 40)
    print(" 최종 학습 결과 ")
    print("=" * 40)

    for subject in scheduled_subjects:

        print(f"\n[{subject.subject_name}]")

        print(
            f"우선순위 점수: "
            f"{round(subject.priority_score,2)}"
        )

        print(
            f"추천 공부 시간: "
            f"{round(subject.recommended_study_time,2)}시간"
        )

        print(
            f"복습 상태: "
            f"{subject.review_status}"
        )

        print(
            f"위험 상태: "
            f"{subject.risk_status}"
        )

        print(
            f"재스케줄 필요 여부: "
            f"{'필요' if subject.reschedule_required else '불필요'}"
        )

    print("\n===== 시스템을 종료합니다. 수고하셨습니다! =====")

if __name__ == "__main__":
    main()