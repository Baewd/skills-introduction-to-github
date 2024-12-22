# file = open ("data/text.txt", "a")
#
# vod = input ("введите число")
#
# file.write(vod + "\n")
#
# file.close()
file = open ("data/text.txt", "r")

print (file.read())       #вывод сплошым текстом

for line in file :        #вывод по строкам
    print(line, end=" ")

file.close()