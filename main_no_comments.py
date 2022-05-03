from config import file

class TimeRange:    
    day = ''
    start_time = ''
    end_time= ''
    hours = []

    def __init__(self, time_range):
        self.hours = []
        self.day = time_range[:2]
        self.start_time = time_range[2:7]
        self.end_time = time_range[8:]

        if len(time_range) > 1:          
            for hour in range (int(self.start_time[:2]), int(self.end_time[:2])):                
                self.hours.append(str(hour))
        

class Schedule:    
    time_ranges = []
    
    def __init__(self, schedule):
        self.time_ranges = []
        time_ranges = schedule.split(',')

        for time_range in time_ranges:
            new_time_range = TimeRange(time_range)
            self.time_ranges.append(new_time_range)


class Employee:    
    def __init__(self, name, schedule) -> None:
        self.name = name
        self.schedule = schedule


class FileParser:    
    rows = []
            
    def __init__(self, file) -> None:
        self.data_file = file

    def _load_rows(self):
        with open(self.data_file) as f:
            self.rows = f.readlines()
    
    def get_employees(self):
        data = []
        self._load_rows()
        for row in self.rows:            
            name = row.split('=')[0]
            schedule = row.split('=')[1]
            employee_schedule = Schedule(schedule)
            employee = Employee(name, employee_schedule)
            data.append(employee)
        return data     


class SalaryCalculator:    
    sat_sun = {'SA', 'SU'}
    first_turn_hours = {'0','1','2','3','4','5','6','7','8'}
    second_turn_hours = {'9','10','11','12','13','14','15','16','17'}
    salary_matrix = {'special': {'first_turn':30, 'second_turn':20, 'third_turn':25},
    'normal': {'first_turn':25, 'second_turn':15, 'third_turn':20}}    
    
    def calculate_salary(self, schedule):
        salary = 0
        turn = ''

        for time_range in schedule.time_ranges:
            if time_range.day in self.sat_sun:
                day_type = 'special'
            else:
                day_type = 'normal'
            for hour in time_range.hours:
                if hour in self.first_turn_hours:
                    turn = 'first_turn'
                elif hour in self.second_turn_hours:
                    turn = 'second_turn'
                else:
                    turn = 'third_turn'
                
                if turn:                    
                    salary += self.salary_matrix[day_type][turn]
            
        return salary



if __name__=='__main__':
        
    fp = FileParser(file)
    salary_calculator = SalaryCalculator()

    employees = fp.get_employees()
    for employee in employees:
        salary = salary_calculator.calculate_salary(employee.schedule)
        print(f'The amount to pay {employee.name.upper()} is: {salary} USD'), employee.name, salary