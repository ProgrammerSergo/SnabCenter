
# Начальные данные:
#=============================================
# 95 160 140 140 60 --- 5
# 60 130 130 140 140
# 90 90 140 140 140
# 190 130 --- 320
#=============================================


# OUT: (Ответ: )
arr = [[95, 160, 140, 140, 60], [60, 130, 130, 140, 140], [90, 90, 140, 140, 140], [190, 130]] # Массив
l = int(input("Размер: ")) # Указание размера
for el in arr: 
    total_el = sum(el) 
    if total_el % l == 0: # Условие с делением остатка
        print(f"Элементы массива: {el}, Итог: {total_el}", sep= " | ") # Вывод на экран
        print(f"===============================================================")   
    else:
        ostatok_masiva = total_el % l   
        print(f"Элементы массива: {el}, Итог: {total_el} c остатком: {ostatok_masiva}", sep= " | ")
        print(f"================================================================")

