import pytest
from main import Schedule, SalaryCalculator


@pytest.mark.parametrize(
    "schedule, expected",
    [
        (Schedule('MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00'), 215),
        (Schedule('MO10:00-12:00,TH12:00-14:00,SU20:00-21:00'), 85)
    ]
)
def test_calculate_salary(schedule, expected):
    salary_calculator = SalaryCalculator()    
    assert salary_calculator.calculate_salary(schedule) == expected
    