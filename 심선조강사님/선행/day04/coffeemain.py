import coffeetestfunc as ctf
## 커피자판기 메뉴 입력 프로그램
coffee = {'아메리카노':3000}
coffee = ctf.data_load('./day4/coffee.data')
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
        coffee = ctf.data_input(coffee)
    elif menu == '2':  
        coffee = ctf.data_delete(coffee)
    elif menu == '3': 
        coffee = ctf.data_update(coffee)
    elif menu == '4':    
        ctf.data_list(coffee)
ctf.data_save(coffee)