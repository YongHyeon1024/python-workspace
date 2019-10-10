from cust_V_ver2 import set_birth, set_email, set_gender, set_identnum, set_name

"""
기능함수
"""


# 입력받은 정보 딕셔너리에 넣는 함수
def insert_inform_to_dict(name, gender, email, birth, ident_num):
    dict_information = {}
    dict_information['name'] = name
    dict_information['gender'] = gender
    dict_information['email'] = email
    dict_information['birth'] = birth
    dict_information['ident_num'] = ident_num
    return dict_information


# 고객 수정 - 지금 열람중인 정보 바꾸기
def adjust_inform(list_information, idx):
    print('수정할 정보를 입력하세요 :')
    name = set_name()
    gender = set_gender()
    email = set_email()
    birth = set_birth()
    ident_num = set_identnum()

    list_information[idx] = insert_inform_to_dict(name,
                        gender, email, birth, ident_num)
    return list_information


# 고객 수정 - 입력받은 주민번호와 일치하는 정보 찾아바꾸기
def modify_inform(name, ident_num, list_information):
    iscorrect_ident = False            
    for i in range(0, len(list_information)):
        iscorrect_ident = False
        if ident_num in list_information[i]['ident_num']:
            iscorrect_ident = True

        if iscorrect_ident is True:
            print('%s 고객의 수정입니다.' % name)
            adjust_inform(i)
            print("수정된 고객의 정보입니다.")
            get_inform(i)
            break
    if iscorrect_ident is False:
        print('\n없는 고객정보입니다.\n')
    return list_information

# 고객 정보 삭제 함수
def del_infrom(name, ident_num, list_information):
    iscorrect_ident = False

    for i in range(0, len(list_information)):
        iscorrect_ident = False
        if ident_num in list_information[i].values():
            iscorrect_ident = True

        if iscorrect_ident is True:    
            print('\n%s 님은 삭제 되었습니다.\n' % name)
            del list_information[i]
            break
    if iscorrect_ident is False:
        print('\n없는 고객 정보입니다.\n')
    return list_information