import telebot
import random

# Устанавливаем токен бота
bot_token = '64376710:AAEZFLV8dplV-wItDCk2z04_9OYa0'

# Создаем экземпляр бота
bot = telebot.TeleBot(bot_token)

# Словарь для хранения данных пользователей
user_data = {}

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    user_id = message.chat.id
    user_data[user_id] = {
        'number': random.randint(1, 100),  # Генерируем случайное число от 1 до 100
        'attempts': 0  # Инициализируем количество попыток
    }
    bot.reply_to(message, "Привет! Я загадал число от 1 до 100. Попробуй угадать!")

# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def handle_guess(message):
    user_id = message.chat.id
    if user_id in user_data:
        
        correct_number = user_data[user_id]['number']
        attempts = user_data[user_id]['attempts']
        try:
            user_guess = int(message.text)
            if user_guess < 1 or user_guess > 100:
                bot.reply_to(message, "Пожалуйста, введите число от 1 до 100")
            else:
                if user_guess == correct_number:
                    bot.reply_to(message, f"Поздравляю! Ты угадал число {correct_number} за {attempts} попыток.")
                    del user_data[user_id]  # Удаляем данные пользователя после окончания игры
                elif user_guess < correct_number:
                    bot.reply_to(message, "Загаданное число больше.")
                    user_data[user_id]['attempts'] += 1
                else:
                    bot.reply_to(message, "Загаданное число меньше.")
                    user_data[user_id]['attempts'] += 1
        except ValueError:
            bot.reply_to(message, "Пожалуйста, введите число")
        
    else:
        bot.reply_to(message, "Начни игру с команды /start")

# Запускаем бота
bot.polling()
