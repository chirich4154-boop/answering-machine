def recognize_request(action_number):
    if action_number == 1:
        print_trainer()
    elif action_number == 2:
        print_schedule()
    elif action_number == 3:
        days_count = int(input('Сколько дней было отработано?'))
        print_total(days_count)

def print_total(days_count):
    price_day = 1200
    total = days_count * price_day
    print('Сумма к оплате за', days_count, 'дней:', total, 'рублей.')

def print_trainer():
    print('Вот данные тренера:\nКонтакт тренера: Петров А.В.,\nТелефон +79991112233,\nЭлектронная почта: trainer4154@mail.ru.')

def print_schedule():
    print('Расписание секций:\nБокс - Пн/Ср в 19:00,\nПлавание - Вт')         
