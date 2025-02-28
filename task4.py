from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()  
    upcoming_birthdays = []
    
    for user in users:
        user_birthday = get_user_birthday(user, today)
        
        if is_birthday_upcoming(user_birthday, today):
            upcoming_birthdays.append(get_user_notification_object(user, user_birthday))
    
    return upcoming_birthdays

def is_birthday_upcoming(user_birthday, today):
    b_delta = (user_birthday - today).days
    return 0 <= b_delta <= 7 

def get_user_birthday(user, today):
    birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date()
    birthday_this_year = birthday.replace(year=today.year)
    
    if birthday_this_year < today:  
        birthday_this_year = birthday.replace(year=today.year + 1)
    
    return birthday_this_year

def get_user_notification_object(user, user_birthday):
    return {
        'name': user['name'],
        'congratulation_date': get_notification_date(user_birthday).strftime('%Y.%m.%d')
    }

def get_notification_date(user_birthday):
    if user_birthday.weekday() == 5:  
        return user_birthday + timedelta(days=2)
    elif user_birthday.weekday() == 6: 
        return user_birthday + timedelta(days=1)
    return user_birthday

users = [
    {"name": "John Doe", "birthday": "1985.02.25"},
    {"name": "Jane Smith", "birthday": "1990.04.22"},
    {"name": "Mary Jane", "birthday": "1985.05.01"},
    {"name": "Bob Brown", "birthday": "1990.02.28"},
    {"name": "Charlie Davis", "birthday": "1990.03.01"},
    {"name": "Daniel Evans", "birthday": "1990.03.22"},
    {"name": "Emma Wilson", "birthday": "1990.02.19"},
    {"name": "Grace Taylor", "birthday": "1990.02.20"},
    {"name": "Helen Anderson", "birthday": "1990.02.21"},
    {"name": "Isabella Thomas", "birthday": "1990.02.22"},
    {"name": "Kevin Jackson", "birthday": "1990.02.23"},
    {"name": "Liam Harris", "birthday": "1990.02.24"},
    {"name": "Megan White", "birthday": "1990.02.25"},
    {"name": "Noah Martin", "birthday": "1990.02.26"},
    {"name": "Olivia Thompson", "birthday": "1990.02.27"},
    {"name": "Peter Martinez", "birthday": "1990.02.28"},
    {"name": "Quinn Robinson", "birthday": "1990.03.01"},
    {"name": "Rose Clark", "birthday": "1990.03.02"},
    {"name": "Samuel Rodriguez", "birthday": "1990.03.03"},
    {"name": "Tina Lewis", "birthday": "1990.03.04"},
    {"name": "Ursula Lee", "birthday": "1990.03.05"},
    {"name": "Victor Walker", "birthday": "1990.03.06"},
    {"name": "Wendy Hall", "birthday": "1990.03.07"},
    {"name": "Xander Young", "birthday": "1990.03.08"},
    {"name": "Yvonne Allen", "birthday": "1990.03.09"},
    {"name": "Zack Scott", "birthday": "1990.03.10"},
    {"name": "Alice King", "birthday": "1990.03.11"},
    {"name": "Benjamin Wright", "birthday": "1990.03.12"},
    {"name": "Catherine Lopez", "birthday": "1990.03.13"},
    {"name": "David Hill", "birthday": "1990.03.14"},
    {"name": "Eva Green", "birthday": "1990.03.15"},
    {"name": "Frank Adams", "birthday": "1990.03.16"},
    {"name": "Gina Baker", "birthday": "1990.03.17"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список приветствий на этой неделе:")
for item in upcoming_birthdays:
    print(f"{item['name']} - {item['congratulation_date']}")


