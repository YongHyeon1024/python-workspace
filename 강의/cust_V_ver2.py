import re

"""
정보 입력 받는 함수
"""


# 정보 입력 함수
def set_name():
    validation = False
    while validation is not True:
        name = input("이름 : ")
        if not re.match(r'[a-zA-Zㄱ-힣]', name):
            print("올바른 이름입력이 아닙니다. 다시 시도해주세요")
        else:
            validation = True
    return name


def set_identnum():
    validation = False
    while validation is not True:
        ident_num = input("주민등록 번호를 입력하세요 (123456-1234567) :")
        if not re.match(
                r'^(?:[0-9]{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[1,2][0-9]|3[0,1]))-[1-4][0-9]{6}$',
                ident_num):
            print('올바른 주민등록 번호가 아닙니다.')
        else:
            validation = True
    return ident_num


def set_gender():
    validation = False
    while validation is not True:
        gender = input('성별 (M 또는 F) : ')
        if gender.upper() == 'M' or gender.upper() == 'F':
            validation = True
        else:
            print("올바른 성별입력이 아닙니다. 다시 시도해주세요")
    return gender


def set_email():
    validation = False
    while validation is not True:
        email = input('이메일 (형식 : a@a.com) : ')
        if len(email) > 6:
            if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                print("올바른 이메일이 아닙니다. 다시 시도해주세요")
            else:
                validation = True
    return email


def set_birth():
    validation = False
    while validation is not True:
        birth = input('생년월일(ex. 940915) :')
        if len(birth) == 6:
            if not re.match(r"[0-9]", birth):
                print('올바른 생년월일이 아닙니다. 다시 시도해주세요.')
            else:
                validation = True
    return birth


# 다음 스텝 입력받는 함수
def what_next_step(list_information, idx):
    valid = False
    while valid is False:
        print('**%s / %s**' % (idx + 1, len(list_information)))
        print('P : 다음 고객 정보')
        print('N : 이전 고객 정보')
        print('U : 정보 수정')
        print('Z : 첫  화  면')
        u_i = input('입력 : ')
        user_input = u_i.upper()
        steps = ['P', 'N', 'U', 'Z']
        if user_input in steps:
            valid = True
            return user_input
        else:
            print('입력이 틀렸습니다. 다시입력해 주세요.')


def what_next_step_last(list_information, idx):
    valid = False
    while valid is False:
        print('**마지막 고객입니다. %s / %s**' % (idx + 1, len(list_information)))
        print('N : 이전 고객 정보')
        print('U : 정보 수정')
        print('Z : 첫  화  면')
        u_i = input('입력 : ')
        user_input = u_i.upper()
        steps = ['N', 'U', 'Z']
        if user_input in steps:
            valid = True
            return user_input
        else:
            print('입력이 틀렸습니다. 다시입력해 주세요.')


def what_next_step_first(list_information, idx):
    valid = False
    while valid is False:
        print('**처음 고객입니다. %s / %s**' % (idx + 1, len(list_information)))
        print('P : 다음 고객 정보')
        print('U : 정보 수정')
        print('Z : 첫  화  면')
        u_i = input('입력 : ')
        user_input = u_i.upper()
        steps = ['P', 'U', 'Z']
        if user_input in steps:
            valid = True
            return user_input
        else:
            print('입력이 틀렸습니다. 다시입력해 주세요.')

"""
출력 함수
"""


# 고객 정보 조회 출력 함수
def get_inform(list_information, index=0):
    print('')
    print('이    름 : ', list_information[index].get('name'))
    print('성    별 : ', list_information[index].get('gender'))
    print('이 메 일 : ', list_information[index].get('email'))
    print('출생년도 : ', list_information[index].get('birth'))
    print('')


# 인트로 출력 함수
def say_hello():
    print('='*50)
    print('{:^40}'.format('고객 관리 프로그램'))
    print('='*50)
    print("고객의 정보는 이름, 성별, 이메일, 출생년도를 저장합니다.")
    print("할 일을 선택하십시오.")
    print("""
    1. 고객정보입력
    2. 고객정보조회
    3. 고객정보수정
    4. 고객정보삭제
    0. 프로그램종료
                """)


# 고객 정보 출력 - 다음 고객 정보
def next_information(list_information, idx):
    idx += 1
    get_inform(list_information, idx)
    return idx


# 고객 정보 출력 - 이전 고객 정보
def previous_information(list_information, idx):
    idx -= 1
    get_inform(list_information, idx)
    return idx