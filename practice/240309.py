#test(자주 혼동하고 헷갈리는 기본 문법 필기.)
#나도코딩(1분 속성 강의 정리)

#인덱스와 슬라이싱
#인덱스 : 배열(0부터 시작함.)

#슬라이싱(인덱스의 a번째부터 b번째까지의 
# 인덱스 값을 출력하는 과정.)
# ex) print(lang[1:6]) //인덱스 1부터 6직전(6포함X)까지 출력.
# ex) print(lang[:]) //처음부터 끝까지.

####################
#--파이썬 메소드 등을 쉽게 찾는법--
# Python 내장형 -> 공식홈피 -> ctrl+F 하고 'find' 검색
####################

#문자열 포맷
# 1. {} + format
# ex) print('개발 언어에는 {}, {} 등이 있어요.'.format(python, java))

python = '파이썬'
java = '자바'

print('개발 언어에는 {}, {} 등이 있어요.'.format(python, java))

# 2. {N} + format //N : 0, 1, 2 ···
print('개발 언어에는 {0}, {1}등이 있어요'.format(python, java))

# 3. f-string //파이썬 3.6이상
print(f'개발 언어에는 {python}, {java}등이 있어요.')

# 탈출 문자 :
#큰 따옴표는 \"
#작은 따옴표는 \'
#ex) print('하지만 \'나만 당할 순 없지\'라는 생각에\"엄청쉽지\"라고 했다.')
#역슬래쉬 두번 적으면 역슬래쉬도 제대로 출력이 된다.

# 리스트와 튜플 |
# 리스트는 수정이 가능하지만 튜플은 한번 만들고 나면 수정이 불가능 하다.
# 즉, 튜플은 "읽기전용 리스트" 와 같이 볼 수 있음.

# set |
#set은 순서가 보장되지 않음** 그래서 인덱스를 통해서
# 접근 및 수정 불가능 (ex) print(set[1]) 과 같이..
# 하지만 removw, add, clear 메소드 등을 활용할 수 있음.

#딕셔너리( key와 value가 한쌍으로 이루어짐.)
# dic = {key1:value, key2:value2, ...}



