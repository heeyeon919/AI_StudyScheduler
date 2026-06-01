# models.py
# 데이터 구조 정의하는 역할

from dataclasses import dataclass
from datetime import date
from typing import Optional, List, Dict, Union

@dataclass
class UserConfig:
    daily_available_hours: float
    schedule_start_date: date
    preferred_study_time: str


@dataclass
class Subject:
    subject_name: str
    exam_date: date

    course_category: str
    subject_type: str

    total_chapters: float
    completed_chapters: float

    understanding_rate: float
    target_grade: str

    last_studied_date: date

    midterm_weight: float
    final_weight: float
    
    #Subject 내부 계산용 필드
    urgency_score: Optional[float] = None # Logic1 출력 데이터
    days_left: Optional[int] = None # Logic1 출력 데이터

    lack_of_understanding: Optional[float] = None # Logic2 출력 데이터
    
    remaining_chapters: Optional[float] = None # Logic3 출력 데이터
    progress_rate: Optional[float] = None # Logic3 출력 데이터
    # completed_chapters / total_chapters

    importance_score: Optional[float] = None # Logic4 출력 데이터
    
    retention_risk: Optional[float] = None # Logic5 출력 데이터
    
    remaining_ratio: Optional[float] = None # Logic6 사용 데이터 
    # remaining_chapters / total_chapters
    
    raw_score: Optional[float] = None # Logic6 내부 계산용 데이터
    priority_score: Optional[float] = None # Logic6 출력 데이터
   
    planned_progress: Optional[float] = None # Logic7 출력 데이터
    recommended_study_time: Optional[float] = None # Logic7 출력 데이터

    daily_schedule: Optional[List[Dict[str, Union[str, float]]]] = None # Logic8 출력 데이터
    
    review_score: Optional[float] = None # Logic9 출력 데이터
    review_status: Optional[str] = None # Logic9 출력 데이터

    actual_completed_ratio: Optional[float] = None # Logic10 출력 데이터
    # actual_progress / planned_progress
    risk_status: Optional[str] = None              # Logic10 출력 데이터
    reschedule_required: Optional[bool] = None     # Logic10 출력 데이터
    
