from list import ran_wor, list_data
from list import num1

bol = False
otvet_list = []
var = []
a = 0
num = 0
a_otvet = 0
word=ran_wor()


abc_list = list_data(word)

for i in word :
    a +=1
print ("количество букв в слове :", a)
i=0
while i<10 and bol==False :
    i += 1
    while a != a_otvet :
        otvet = input("введите предпологаемое слово")
        a_otvet =num1(otvet)
        otvet_list=list_data(otvet)

    if otvet_list == abc_list:
        print("молодец ты угодал")
        bol=True
    else:
        for i1 in otvet_list :
            if abc_list[num] == otvet_list[num] :
                var.append("да")
            else:
                if i1 in abc_list :
                    var.append("^")
                else :
                    var.append("x")
            num +=1

    num=0
    print(var)
    var.clear()
    a_otvet=0