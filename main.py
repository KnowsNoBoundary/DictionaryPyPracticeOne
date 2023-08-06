# August 5, 2023, Let's practice some dictionary methods, and how manipulate the code for our future goals.
from datetime import datetime
import calendar

gaming_titles = {
    'Pokémon UNITE': {
        'Date': '07-05-23',
        'Dailies': True,
        'GraphData': 0
    },
    'NIKKE': {
        'Date': '07-05-23',
        'Dailies': False,
        'GraphData': 0
    }
}

current_date = datetime.today()
last_day = calendar.monthrange(current_date.year, current_date.month)[1]
this_month_days = [(current_date.replace(day=day)).strftime('%y-%m-%d') for day in range(1, last_day + 1)]
print("This month's days:", this_month_days)
