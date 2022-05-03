from config import file

class TimeRange:
    '''
    TimeRange Class:
        Properties:
            day (str): A day in format "MO, TU, WE, TH, FR, SA, SU"
            start_time (str): A string indicating the start_time of the TimeRange Object
            end_time (str): A string indicationg the end_time of the TimeRange Object
            hours (list): A list containing the hours between start_time and end_time
        Methods:
            __init__(self, time_range): When the class is instantiated this method load the 
            TimeRange data from a string like this: "TU12:00-13:00"
                Params:
                    time_range (str) <required>: A string in a format like this "WE06:00-15:00"
    '''
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
    '''
    Schedule Class:
        Properties:
            time_ranges (list): A list containing a collection of TimeRange Objects            
        Methods:
            __init__(self, schedule): When the class is instantiated this method load the 
            Schedule data from a string like this: "MO10:00-12:00,TH12:00-14:00,SU20:00-21:00",
            then, splits the string in time_ranges and instantiate as many TimeRange objects are
            required and append this to it's collection time_ranges.
                Params:
                    schedule (str) <required>: A string in a format like this:
                        "MO10:00-12:00,TH12:00-14:00,SU20:00-21:00"
    '''
    time_ranges = []
    
    def __init__(self, schedule):
        self.time_ranges = []
        time_ranges = schedule.split(',')

        for time_range in time_ranges:
            new_time_range = TimeRange(time_range)
            self.time_ranges.append(new_time_range)


class Employee:
    '''
    Employee Class:
        Properties:
            name (str): A string containing the name of the employee
            schedule (Schedule): A Schedule object containing the schedule of the employee
    '''
    def __init__(self, name, schedule) -> None:
        self.name = name
        self.schedule = schedule


class FileParser:
    '''
    FileParser Class:
        Properties:
            rows (list): A list containing a collection of records readed from the data_file
        Methods:
            _load_rows(self): Marked as private, this method is invoqued to fill the rows property.
            get_employees(self): This method parse rows and instantiate on Employee object for each
                                 row, assign it's name property. Also instantiate a Schedule object
                                 and assign it to an Employee object.
                returns:
                    data (list): A list of Employee objects           
    '''
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
    '''
    SalaryCalculator Class:
        Properties:
            There are not useful properties on this class. All are only for internal purposes.
            There are not marked as private because check this properties by code has no secondary effects,
            and in order to preserve readability.
        Methods:
            calculate_salary(self, schedule): This method is used to calculate the salary.
                params:
                    schedule (Schedule): An object of type Schedule containing the schedule to be
                                         analyzed.
                returns:
                    Salary (number): An int or float that represents the salary.
    '''
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