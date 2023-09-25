import telebot
n=0;
i=4;

TOKEN = '6605531072:AAGpEQjhSaB4pRAQ9NCdXtpGYCwx56snTeg'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send(message):
    
    bot.send_message(message.chat.id, 'Привет! Я бот-калькулятор, готов помочь вам с вычислениями.')
   
    bot.send_message(5636271256, f'{message.chat.id}, {message.from_user.first_name}')

@bot.message_handler(func=lambda message: True)
def cal(message):
    n=message.chat.id
#id=5636271256
  
    try:
               
        result = eval(message.text)
        print(n)
        bot.reply_to(message, f"Результат: {result}                                                                                                              Если понравился калькулятор, вы можете пожертвовать деньги на мой мобильный кошелек  +992985771736.")
    
    except:
        bot.reply_to(message, "Ошибка при вычислении. Проверьте правильность выражения,вместо '÷' используй '/', и вместо '×' используй '*'.")

bot.polling(none_stop=True)

