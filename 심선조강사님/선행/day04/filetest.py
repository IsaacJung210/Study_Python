import pickle

# f = open('./day04/pickle01.txt' , 'wb')
# coffee = {'아메리카노':3000}
# pickle.dump(coffee,f)
# f.close()

# f = open('./day04/pickle01.txt' , 'rb')
# coffee = pickle.load(f)
# f.close()
# print(coffee)

import json

# f = open('./day04/json01.txt' , 'w', encoding='cp949')
# coffee = {'아메리카노':3000}
# json.dump(coffee,f)
# f.close()

f = open('./day04/json01.txt' , 'r')
coffee = json.load(f)
f.close()
print(coffee)
