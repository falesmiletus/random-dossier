import random
surname = [' Смирнов ', 'Иванов', 'Кузнецов', 'Попов', 'Соколов', 'Лебедев', 'Козлов', 'Новиков', 'Морозов']
name = ['Григорий','Михаил','Владислав','Иван','Афонасий','Антон','Александр']
patronymic = ['Романович','Николаевич','Владимирович','Сергеевич','Александрович']
print(surname[random.randint(0,len(surname)-1)],name[random.randint(0,len(name)-1)],patronymic[random.randint(0,len(patronymic)-1)],sep= ' ' )
month = random.randint(1,12)
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print(random.randint(1,31),'.',month,'.',random.randint(1956,2000),sep='')
elif month == 2:
    print(random.randint(1, 28), '.', month, '.', random.randint(1956, 2000),sep='')
else:
    print(random.randint(1, 30), '.', month, '.', random.randint(1956, 2000),sep='')
city = ['Москва', 'Екатеренбург', 'Санкт-Петербург', 'Владивосток', 'Волгоград', 'Магадан']
print('Уроженец города -',city[random.randint(0,len(city)-1)])
tel = random.randint(7, 8)
if tel == 7:
    tel = '+7'

print('Телефон - ',tel,'(','9',random.randint(0, 9),random.randint(0, 9),')',random.randint(0, 9),random.randint(0, 9),random.randint(0, 9)
      ,'-',random.randint(0, 9),random.randint(0, 9),'-',random.randint(0, 9),random.randint(0, 9),sep='')