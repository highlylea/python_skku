"""
1차시도_두줄연습
temperature=float(input("This program converts Celsius to Fahrenheit. Celsius:"))
print("It is", temperature*9/5+32, "in fahrenheit.")

2차시도_한줄연습
print('It is {}°F.'.format(float(input('This program converts Celsius to Fahrenheit. Celsius:'))*9/5+32))


#3차시도_함수연습_
def ctof():
    c = float(input("섭씨 온도를 입력하세요.:"))
    return c*9/5+32  
print("화씨", ctof(),"도 입니다.")

""" 
#4차시도_함수 더 짧게
def ctof():
    return float(input("섭씨 온도를 입력하세요:"))*9/5+32
print(ctof(),"도 입니다.")