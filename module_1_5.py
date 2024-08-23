from dataclasses import replace

immutable_var = 1, 2, 'ДЗ'
print(immutable_var)
#immutable_var[0] = 3 # Получаем ошибку 'tuple' object does not support item assignment означающую что нельзя менять данные в "Кортежи"
mutable_var = '1, 2, ДЗ'
print(type(mutable_var))
print(mutable_var.replace('1', '3'))