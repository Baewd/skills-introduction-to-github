otvet = input ("что вы хотите добавить  инфуу или получить инфу")
i =0
if otvet == "добавить" :


    file = open ("book/book.txt", "a", encoding="utf8")

    class Book :
        name = None
        paichs = None
        avtor = None
        old = None

    book = Book()
    book.name = input ("введите название книги")
    book.paichs = input ("введите количество страниц в книге")
    book.avtor = input ("введите автора книги")
    book.old = input ("введите год выпуска книги")
    file.write(book.name+ "\n")
    file.write(book.paichs+ "\n")
    file.write(book.avtor+ "\n")
    file.write(book.old+ "\n")
    file.close()
elif otvet == "получить":
    file = open ("book/book.txt", "r", encoding="utf8")
    otvet = input ("введите название текста")
    if otvet in file :
        print (i)
    else :
        print ("текс не найден")




    file.close()