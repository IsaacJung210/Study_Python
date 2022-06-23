import json

f = open('./day4/coffee.data','r')
coffee = json.load(f)
f.close()

## 커피자판기 메뉴 입력 프로그램
# coffee = {'아메리카노':3000}

while True:
    display = '''
---------------------------------------------------------------------
1. 메뉴입력   2. 메뉴삭제   3. 메뉴 수정   4. 메뉴리스트  5. 종료
---------------------------------------------------------------------
>>> '''
    menu = input(display)
    if menu == '5':
        print('프로그램 종료')
        break
    elif menu == '1':    
        item = input('메뉴명 >>>')
        price = int(input('메뉴가격 >>>'))
        coffee[item] = price
        print(coffee)
    elif menu == '2':  
        print(coffee.keys())
        item = input('삭제할 메뉴명 >>>')
        del coffee[item]
        print(coffee)
    elif menu == '3': 
        print(coffee.keys())
        item = input('수정할 메뉴명 >>>')
        price = int(input('수정할 가격 >>>'))
        coffee[item] = price
        print(coffee)
    elif menu == '4':    
        for k,v in coffee.items():
            print(f' {k:^10}  {v:,}')

f = open('./day4/coffee.data','w')
json.dump(coffee,f)
f.close()