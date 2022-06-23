import json

def data_load(path):
    f = open(path,'r')
    coffee = json.load(f)
    f.close()
    return coffee

def data_input(coffee):
    item = input('메뉴명 >>>')
    price = int(input('메뉴가격 >>>'))
    coffee[item] = price
    print(coffee)
    return coffee

def data_delete(coffee):
    print(coffee.keys())
    item = input('삭제할 메뉴명 >>>')
    del coffee[item]
    print(coffee)
    return coffee

def data_update(coffee):
    print(coffee.keys(coffee))
    item = input('수정할 메뉴명 >>>')
    price = int(input('수정할 가격 >>>'))
    coffee[item] = price
    print(coffee)
    return coffee

def data_list(coffee):
    for k,v in coffee.items():
        print(f' {k:^10}  {v:,}')

def data_save(coffee):
    f = open('./day4/coffee.data','w')
    json.dump(coffee,f)
    f.close()