import random
import time

print ("проверим твою память?")
print ("есть 3 уровня сложности (1, 2, 3)")
list = []
levl = int(input ("какой уровень сложности выберишь?"))
if levl == 1 :
    levl = 10
elif levl == 2 :
    levl = 20
else :
    levl = 30
for i in range(levl):
    i +=1
    ran1 = random. randint(0, 1)
    list.append(ran1)
print(list)
print ("у тябя 5 секунд чтоб запомнить всё")
for i in range (5):
    print (i)
    time.sleep(1)
print("авсё" * 100000)
number = int(input ("введи это число через пробел"))
# print("я сам хз проверь сам)", list)
if number == list :
    print ("харооооощ")
else :
    print ("бывает")