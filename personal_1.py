## 구구단 출력 

# 1단부터 9단까지
# range(시작 숫자 , 제한) 
# range(1,10) => 1,2,....9
for num1 in range(1,10):
    for num2 in range(1,10):
        result_multiple = num1 * num2
        print(num1 , "*" , num2 , "=",result_multiple)

# 입력한 숫자만 

# 입력받은 값은 문자열이기 때문에, 변환해주어야 함
number_of_multiple = int(input('몇 단을 출력할까요? '))

for num in range(1,10):
    print(number_of_multiple , '*' , num,'=', number_of_multiple * num)

