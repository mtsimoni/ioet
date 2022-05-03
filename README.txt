Program: ioet Programming Challenge
Author:  Marcelo Toledo Simoni

An Overview of the Solution:

This program solves the ioet Programming Challenge for several employees and considering that
one employee can work in a session that overlaps two or three diferent turns, i. e.

    Elizabeth=MO14:00-21:00,TU06:00-19:00,WE02:00-18:00,FR09:00-19:00,SA13:00-14:00,SU14:00-24:00

Here Elizabeth is working from 14:00 to 21:00, overlapping two turns and then even from 6:00 to 19:00 
overlapping three turns. Poor Elizabeth.

The hours from 14:00 to 18:00 has a different value that from 18:00 to 21:00.

Another script to generate users and schedules is included.


Some Comments about the Architecture:

I decided this could be a good Architecture in the case the solution needs to be scaled up.

The directory organization is:

    ioet <the base directory>
        resources <directory for resources>
            data_files <directory containing the data files in the case it extends functionality to deal
                        with several files>
                days_worked_sheet.txt <a file containing a the records to analyze>
            scripts <directory containing useful scripts>
                generate_file.py <a program to populate the file days_worked_sheet.txt>
        config.py <a configuration file, useful if the program scales up>
        main.py <the main script>
        test_main.py <a test script>
        README.md <the readme file using markdown>
        README.txt <the same in .txt format>
        requirements.txt <requirements to install the pytest library>



About the Approach and Methodology

For the main.py script my approach is Pythonic, totally Object Oriented, and respecting SOLID and clean code.

Let's check some code to support the previous sentence:


        salary_matrix = {'special': {'first_turn':30, 'second_turn':20, 'third_turn':25},
                        'normal': {'first_turn':25, 'second_turn':15, 'third_turn':20}}    

I think this matrix is easy to understand. It's following the 7th zen rule: Readability counts and also clean
code recomendations.

By the way:

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

When I tought this approach I was triying to reduce considerably the <If> evaluations. I tried to do it easy to read and understand even 
without comments by following clean code recomendations, and also the Pythonic rules:
                
                Beautiful is better than ugly.
                Simple is better than complex.
                Sparse is better than dense.
                Readability counts.

The main script have the following classes:

Employee
Schedule
TimeRange

FileParser
SalaryCalculator

Each one has its own responsibilities (SOLID) and some are applying the Factory Pattern Design.

By example, Schedule instantiate as many TimeRange objects it needs to load the data coming in the string.

Then, it's the TimeRange object that realize hour related operations.

An Employee object contains a Name and a Schedule object.

A Schedule object can contain None, One or Several TimeRange objects.

For the script that populate the file days_worked_sheet with names and schedules my Approach was generic and
it's pure structured programming.

How to run

Python Version: 3.10.4 

- To run the main.py script just use :

        $ python main.py

- To run the generate_file.py script in order to populate the file:

        $ python generate_file.py

- To run the test:

        create the environment:

        $ cd ioet
        $ python -m venv venv

        activate it:

        $ source venv/bin/activate

        install pytest by hand or use requirements.txt:

        (venv)..$ pip install --upgrade pip
        (venv)..$ pip install -r requirements.txt

        run pytest:

        (venv)..$ pytest



