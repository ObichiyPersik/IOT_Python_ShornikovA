s1 = ['Рентген','Лоренц','Зееман','Кюри','Милликен', 'Сигбан', 'Франк', 'Герц']
s2 = ['Фишер','Резерфорд','Кюри','Прегль']
print(len(s1))
for i in range (len(s1)):
    for j in range (len(s2)):
        if(s1[i] == s2[j]):
            print(s1[i])