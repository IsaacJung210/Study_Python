import json,sys

class Coffee:
    coffee=[]
# 함수들 넣어준다.
    def data_load(self):
        with open('./day04/coffeedata.json' , 'r') as f:
            self.coffee = json.load(f)        

    def data_input(self):
        item = input('메뉴명 >>>')
        price = int(input('메뉴가격 >>>'))
        self.coffee[item] = price
        print(self.coffee)

    def data_delete(self):
        print(self.coffee.keys())
        item = input('삭제할 메뉴명 >>>')
        del self.coffee[item]
        print(self.coffee)

    def data_update(self):
        print(self.coffee.keys())
        item = input('수정할 메뉴명 >>>')
        price = int(input('수정할 가격 >>>'))
        self.coffee[item] = price
        print(self.coffee)

    def data_list(self):
        for k,v in self.coffee.items():
            print(f' {k:^10}  {v:,}')

    def data_save(self):
        with open('./day04/coffeedata.json' , 'w') as f:
                json.dump(self.coffee,f,indent=True)
#끝낼 수 있도록 exe를 만들어준다.
    def exe(self,menu):
        if menu == '1':    
            self.data_input()
        elif menu == '2':  
            self.data_delete()
        elif menu == '3': 
            self.data_update()
        elif menu == '4':    
            self.data_list()
        elif menu == '5':
            self.data_save()
            print('프로그램 종료')
            sys.exit()
    
    def display(self):
        menu = input('''
---------------------------------------------------------------------
1. 메뉴입력   2. 메뉴삭제   3. 메뉴 수정   4. 메뉴리스트  5. 종료
---------------------------------------------------------------------
>>> ''')
        return menu #해도 되고 안해도 상관 없다.
#초기시작값을 설정한다.
    def __init__(self):
        self.data_load()
        while True:
            self.exe(self.display())

Coffee()