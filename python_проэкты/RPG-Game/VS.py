def VS(play, lvl):
    my_list = list(play)
    if play == "normal":
        for i in my_list:
            print(" ".join(i))
    elif play == "inventory":
        for i in my_list:
            print(" ".join(i))
    elif play == "bos":
        for i in my_list:
            print(" ".join(i))

def VS_list(play):
    if play == "normal" or play == 1:
        list =[
            [" ", " ", " ", " ", " "],
            [" ", " ", "M", " ", " "],
            [" ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "],
            [" ", " ", "I", " ", " "],
        ]

    elif play == "inventory" or play == 2:
        list =[
            [" ", " ", " ", " ", " "],
            [" ", " ", "B", " ", " "],
            [" ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "],
            [" ", " ", "I", " ", " "],
        ]

    elif play == "bos" or play == 3:
        list =[
            [" ", " ", " ", " ", " "],
            [" ", " ", "D", " ", " "],
            [" ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "],
            [" ", " ", "I", " ", " "],
        ]
    return list

def print_list(list) :
    for i in list :
        print(" ".join(i))

def fight_D(list, play, Plaer, vrag) :
    a=0

    list_def = []
    new_list=[]
    for i in list:
        for ii in i:
            a +=1
            if a == 8:
                ii=" "
            elif a == 13:
                if play ==1:
                    ii = "M"
                elif play ==2:
                    ii = "B"
                elif play ==3:
                    ii = "D"
            elif a == 18:
                ii = "|"
            new_list.append(ii)
        list_def.append(new_list)
        new_list=[]
    print_list(list_def)
    list_def=[]
    a=0
    str_vrag=str(vrag)
    str_Plaer = str(Plaer)
    print(str_Plaer)
    for d in list:
        for dd in d:
            a +=1
            if a == 2:
                for c in str_vrag :
                    dd = c
                    new_list.append(dd)
            if a==17:
                for c in str_Plaer :
                    dd = c
                    new_list.append(dd)
            if a == 8:
                if play ==1:
                    dd = "M"
                elif play ==2:
                    dd = "B"
                elif play ==3:
                    dd = "D"
            elif a == 13:
                dd = " "
            elif a == 18:
                dd = " "
            new_list.append(dd)
        list_def.append(new_list)
        new_list = []
    print_list(list_def)



