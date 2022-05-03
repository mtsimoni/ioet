import random
from sched import scheduler
from webbrowser import get

import os

basedir = os.path.abspath(os.path.dirname(__file__))
basedir = os.path.join(basedir, os.pardir)
data_dir = basedir + '/data_files'
file = data_dir + '/days_worked_sheet.txt'


def get_name():
    names = ('Shannon', 'Kathleen', 'Bryan', 'Sheryl', 'Jenniffer', 'Felicia', 'Brandom', 'Matthew',
                'April', 'Alison', 'Kimberly', 'James', 'Todd', 'Tina', 'Crystal', 'Tracy', 'Caleb',
                'Benjamin', 'Natasha', 'Beverly', 'Jordan', 'Eugene', 'Katherine', 'Joshua', 'Daniel',
                'María', 'Susan', 'Isabel', 'Xinqi', 'Huiting', 'Panthea', 'Ximena', 'Elizabeth')

    return random.choice(names)


def get_time_range():
    start_hour = random.randrange(0,24)
    end_hour = random.randrange(start_hour, 25)
    time_range = str(start_hour).zfill(2) + ':00-' + str(end_hour).zfill(2)+':00'
    return time_range


def get_schedule():
    schedule = ''
    days = ('MO','TU','WE','TH','FR','SA','SU')
    
    for day in days:
        is_worked_day = random.choice((True, False))
        if is_worked_day:
            schedule += day + get_time_range() + ','

    return schedule[:-1]


def get_row():
    row = get_name() + '=' + get_schedule()
    return row


if __name__=='__main__':

    rows = int(input ('How many records do you want to insert into the data file?: '))

    f = open(file,'w')

    for row in range(rows):
        f.write(get_row()+'\n')

    f.close()