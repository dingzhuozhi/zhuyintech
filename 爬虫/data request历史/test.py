import os

date_list=[]
for i in os.listdir(r"C:\Users\Dell\Desktop\DataBase\DataBase\FOMC\Features\statement"):
    date_list.append(i[8:16])

print(date_list)