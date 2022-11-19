"""import datetime
zminna_date_time = datetime.datetime(2022, 11, 19, hour=21, minute=54, second=34, microsecond=434)
print(f'object datetime-{zminna_date_time}')
print(f'type-{type(zminna_date_time)}')
zminna_date_now = datetime.datetime.now()
print((zminna_date_now))
print(datetime.datetime.today())
print(datetime.date.today())
a = datetime.date.today()
b = datetime.datetime(int(input('рік: ')), int(input('місяць: ')), int(input('день: ')), hour=22, minute=11, second=49, microsecond=222)
print(b)"""

#Программа підрахунку років користувачу
import datetime
date_of_birthday = datetime.date(int(input('Введіть ваш рік народження: ')), int(input('Введіть ваш місяць народження: ')), int(input('Введіть ваш день народження: ')))
date_now = datetime.date.today()
count_days = date_now - date_of_birthday
count_days = str(count_days).split()
count_years = int(count_days[0]) / 365
print('Повних років =', round(count_years))