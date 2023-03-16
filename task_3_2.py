my_string = "ФИО;Возраст;Категория;Иванов Иван Иванович;23 года;Студент 3 курса;" \
            "Петров Семен Игоревич;22 года;Студент 2 курса"
new_str = my_string.split(";")
# print(new_str)
column = 0
for st in new_str:
    st2 = st
    if column == 0:
        st2 = st + (25 - len(st))*" "
    print(st2, end=" ")
    if column == 2:
        print()
    column = (column+1) % 3
