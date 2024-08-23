immutable_var = 1, 2, 'ДЗ'
print(immutable_var)
#immutable_var[0] = 3 # Получаем ошибку 'tuple' object does not support item assignment означающую что нельзя менять данные в "Кортежи"
mutable_var = (['1', '2'], 'ДЗ')
print(mutable_var)
mutable_var[0][0] = '3'
print(mutable_var)