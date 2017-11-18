from random import randint
# from time import gmtime, strftime

def get_answer(question, answers = \
    {"привет":["И тебе привет!", "Здорово!", "Дратути!","Здоровеньки булы!","Добрый день!"], 
    "как дела?":["лучше всех", "Отлично!", "Супер", "Пока не родила :)", "Как сажа бела"], 
    "пока":["Увидимся!", "До свидания!", "Аста ла виста, бэби", "Гуд бай!"]
    }):
  answers_list = answers.get(question.lower())
  if answers_list:
    answer = answers_list[randint(0,len(answers_list)-1)]
  else:
    answer = 'Я тебя не понимаю'
  return answer

while True:
  question = input('$ ')
  # print (strftime("%Y-%m-%d %H:%M:%S", gmtime()))
  print (get_answer(question))
  if question.lower() == 'пока':
    break