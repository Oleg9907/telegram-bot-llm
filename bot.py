import telebot as tb
from google import genai

key = '8301571937:AAFCS3pFFff-vgaKN7bS_VA52nbAMmDV5No'
bot = tb.TeleBot(key)

GEMINI_API_KEY = 'AIzaSyBrTBcB0JH2s06pVqSfPWznUVmIgigXpS8'
client = genai.Client(api_key = GEMINI_API_KEY)



@bot.message_handler(commands = ['start']) #ответ на команду /start
def start_message(message):
  bot.send_message(message.chat.id, 'Введите свой запрос и Gemini-3-flash ответит вам')

def gemini(message): #ответ нашей языковой модели на любое сообщение
  response = client.models.generate_content(
      model="gemini-3-flash-preview", contents=message.text
  )
  bot.send_message(message.chat.id, response.text)
  bot.register_next_step_handler(message, gemini)

@bot.message_handler(content_types = ['text']) #ловим первый запрос пользователя
def zapros(message):
  bot.register_next_step_handler(message, gemini)


bot.infinity_polling()
