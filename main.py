#First portfolio project


big_string = """
  _  _       _  _        _   
| || | ___ | || | ___  | |  
| __ |/ -_)| || |/ _ \ |_|  
|_||_|\___||_||_|\___/ (_)  
"""
greeting = 'Welcome to the game!'

print(big_string)

print(greeting)

user_name = input('What is your name?\n')
greeting_user = f'Hello, {user_name}'

print(greeting_user)

user_birthday = input('What is your date of birth (mm/dd):\n')

def zodiac_sign(birthday):
    bday_list = birthday.split('/')
    month = int(bday_list[0])
    day = int(bday_list[1])
    # Define the start and end dates for each zodiac sign
    zodiac_dates = {
        'Aries': [(3, 21), (4, 19)],
        'Taurus': [(4, 20), (5, 20)],
        'Gemini': [(5, 21), (6, 20)],
        'Cancer': [(6, 21), (7, 22)],
        'Leo': [(7, 23), (8, 22)],
        'Virgo': [(8, 23), (9, 22)],
        'Libra': [(9, 23), (10, 22)],
        'Scorpio': [(10, 23), (11, 21)],
        'Sagittarius': [(11, 22), (12, 21)],
        'Capricorn': [(12, 22), (12, 31)],
        'Aquarius': [(1, 20), (2, 18)],
        'Pisces': [(2, 19), (3, 20)]
    }
    for sign, (start_date, end_date) in zodiac_dates.items():
        if (month, day) >= start_date and (month, day) <= end_date:
            return sign

    return "Unknown"

print(f"You're a {zodiac_sign(user_birthday)}")







