# Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141   
# Ввод: 0.01
#     Вывод: 3.14
#     Ввод: 0.001
#     Вывод: 3.141

import math

d = input('--->')
d1 = '.'


res = (map(lambda x: round(math.pi,len(d)-2), d))
print(res)

exit()
for el in range(2):
   my_tuple = (d.split(d1))
print(round(math.pi,len(my_tuple[1])))