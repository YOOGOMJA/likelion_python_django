# 팀원을 추가할 배열을 만듭니다
# 고정 배열을 만들수도 있겠지만, 매번 할때마다 번거로우니 가변 배열로 정의합니다
members = []

# 팀원수는 따로 입력받도록 했습니다
# 다만 Input은 text 형태로 받는게 기본이기때문에, 숫자로 변환해줍니다
number_of_members = int(input('팀원 수를 입력해주세요 : '))

# 입력받은 팀원 수만큼 반복합니다
for index in range(number_of_members):
    # 코드가 보기 쉽도록 번저 따로 변수를 만들어 학번 , 이름을 입력받습니다
    info = input('학번 , 이름을 입력해주세요 : ')
    # 입력받은 정보는 members에 append합니다.
    # 빈 배열에 입력받은 정보가 삽입될 것입니다
    members.append(info)

# 이미 입력받은 정보는 내림차순 정렬합니다
# 이때 내림차순 정렬은 문자열의 맨앞부터 내림차순 정렬하게 되고,
# 학번을 먼저 입력했으므로, 학번순으로 내림차순 될 것입니다.
members.sort(reverse=True)

# 그리고 하나씩 출력합니다
for member in members:
    print(member)



