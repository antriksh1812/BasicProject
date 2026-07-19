def averageOfThree(num1,num2,num3):
    return (num1+num2+num3)/3;


try :
     num1 = int(input('Enter num1'));
     num2 = int(input('Enter num2'));
     num3 = int(input('Enter num3'));
     avg = averageOfThree(num1,num2,num3)
     print(f"Average is {avg}")
except Exception:
     print('Kindly Enter valid numbers')