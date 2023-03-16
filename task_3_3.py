my_string = "ФИО;Возраст;Категория;_Иванов Иван Иванович;23 года;Студент 3 курса;" \
            "_Петров Семен Игоревич;22 года;Студент 2 курса;_Иванов Семен Игоревич;22 года;Студент 2 курса;" \
            "_Акибов Ярослав Наумович;23 года;Студент 3 курса;_Борков Станислав Максимович;21 год;Студент 1 курса;" \
            "_Петров Семен Семенович;21 год;Студент 1 курса;_Романов Станислав Андреевич;23 года;Студент 3 курса;" \
            "_Петров Всеволод Борисович;21 год;Студент 2 курса"
new_str = my_string.split(";")
# print(new_str)
column = 0
spaces = [26, 10, 20]
for i in range(0, 3):
    st2 = new_str[i] + (spaces[column] - len(new_str[i]))*" "
    print(st2, end=" ")
    column = (column + 1) % 3
print()
flag = False
for st in new_str:
    if column == 0:
        flag = False
    st2 = st + (spaces[column] - len(st))*" "
    if flag:
        print(st2, end=" ")
        if column == 2:
            print()
    if(column == 0) and (st2[1:7].lower() == "петров"):
        print(st2, end=" ")
        flag = True
    column = (column+1) % 3
