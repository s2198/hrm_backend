from datetime import datetime

def calculate_annual_leave(employee):
    today = datetime.today().date()
    start_date = employee.start_date
    if start_date > today:
        return 0

    # 근무 연수 계산
    days_worked = (today - start_date).days
    years_worked = days_worked // 365

    if years_worked < 1:
        # 1년 미만 직원의 근무 휴가 계산
        months_worked = days_worked // 30
        return months_worked
    else:
        # 1년 이상 근로자의 연차휴가 계산
        base_leave = 15
        additional_leave = (years_worked // 2)
        return base_leave + additional_leave