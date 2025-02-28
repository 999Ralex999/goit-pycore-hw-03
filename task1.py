from datetime import datetime

def get_days_from_today(date):
    try:
        today = datetime.today().date()
        date_obj = datetime.strptime(date, '%Y-%m-%d').date()

        delta = today - date_obj
        return delta.days
    
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."

print (get_days_from_today('2025-05-05'))
   
    



