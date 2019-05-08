# 파이썬과 HTML 차이?

# 1. HTML 특징 
# : 문서의 구조를 정하기 위해 사용하는 HTML 각 요소간의 포함 
#   관계에 따라서 문서가 보여지는 모습이 결정됨 다시 말해 
#   특별한 논리적인 프로그램을 위해 작성되는 언어가 아닌 구조 
#   자체만을 지정해주기 위해 사용되는 언어. 이를 
#   '마크업 언어'라고 한다.

# 2. PYTHON 특징 
# - 데이터를 가공하거나 연산하기 위해서 사용되는 언어 
# - 반복적인 작업을 하거나, 논리적인 처리를 거쳐야 할 떄 사용됨 

# 3. HTML ? vs PYTHON ?
# - HTML이 할 수 있는 일인 '데이터 구조와 계층 정의'라는 기능은 
#   python의 아주 일부분을 차지함 

# 4. 왜 PYTHON을 쓸까?
# 1) HTML은 이미 내용이 정해진 정적인 문서를 작성하기 위해서 사용됨
# 2) 만약 정적인 정보를 다루는 것이 아니라, 시시각각 변하는 정보를 
#    다뤄야 하는 경우에는 어떻게 할 것인가 
#    ex) 조원의 이름 , 학번을 입력하고 그 입력된 내용을 출력하기
# 3) 이런 경우에는 조원의 이름을 어딘가 추가해주고, 동적으로 내용을
#    표기해야할 것

# 5. PYTHON의 실습환경 
# : 여태까지 HTML을 사용하는 동안에는 

# ###################################################
# 조원 이름 출력하기 
# ###################################################

# 0. 상수 (constant) ?
# : 만약 이름 , 학번을 화면에 출력한다면 HTML에서는 직접 값을 
# 출력했을 것이다. 이 경우 이미 정해져 있던 그 '값'을 변하지 않는다
# 라고 하여 '상수(constant)'라고 한다. 

print('\n############예시 1################')
print(1)
print('Hello World')

# 1. 변수 (Variable) ? 
# : 이미 정해진 값만 출력한다면, 다양한 요구사항을 처리하는 프로그래밍을
# 배울 필요는 없을 것이다. 문서를 작성하는 법을 배우면 되는 것이니까.
# 프로그램을 통해서는 요구사항에 따라 다양한 결과를 출력해줄 수 있어야 
# 한다.
# 예를 들어, 올해 1학년인 학생의 학년을 출력하기 위해서는 상수를 이용해
# 아래와 같은 코드를 쓸 수 있다.

print('\n############예시 2################')
print('학년 : ' , 1)

# 하지만 이 학생이 

