import json,sys

class Coffee:
    coffee = {'아메리카노':3000}
    
    def data_load(self,path):
        f = open(path,'r')
        self.coffee = json.load(f)
        f.close()

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
        f = open('./day4/coffee.data','w')
        json.dump(self.coffee,f)
        f.close()
    

    def exe(self):
        display = '''
    ---------------------------------------------------------------------
    1. 메뉴입력   2. 메뉴삭제   3. 메뉴 수정   4. 메뉴리스트  5. 종료
    ---------------------------------------------------------------------
    >>> '''
        menu = input(display)
        if menu == '5':
            print('프로그램 종료')
            self.data_save()
            sys.exit()
        elif menu == '1':    
            self.data_input()
        elif menu == '2':  
            self.data_delete()
        elif menu == '3': 
            self.data_update()
        elif menu == '4':    
            self.data_list()
    
    def __init__(self):
        self.data_load('./day4/coffee.data')
        while True:
            self.exe()

Coffee()