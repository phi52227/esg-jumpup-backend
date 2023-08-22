import math


def coffee(money):
    coffee_price = 2500
    if money < coffee_price:
        print("돈이 부족합니다.")
    else:
        print(f"커피 나왔습니다! 거스름돈은 {money - coffee_price}원 입니다.")


coffee(int(input("자판기에 돈을 넣어주세요 : ")))


def bmi(height, weight):
    bmi = weight / math.pow(height / 100, 2)
    print(f"bmi 지수는{bmi: .1f} 입니다.")
    if bmi < 18.5:
        print("저체중입니다.")
    elif bmi < 25.0:
        print("정상입니다.")
    elif bmi < 30.0:
        print("과체중입니다.")
    else:
        print("비만입니다.")


height = float(input("키를 입력해주세요(cm) : "))
weight = float(input("몸무게를 입력해주세요(kg) : "))
bmi(height, weight)
