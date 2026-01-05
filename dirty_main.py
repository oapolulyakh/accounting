from application.db.people import *
from application.salary import *
from datetime import datetime

if __name__ == '__main__':
    print(f"Today is {datetime.date(datetime.now())} from {__name__}")
    calculate_salary()
    get_employees()