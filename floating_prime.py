def check_prime(num):
    count = 0
    for j in range(1,int(num)):
        print(f'{num}%{j}={num%j}')
        if num%j == 0:
            count+=1
        if count > 1:
            return False
    else:
        return True

def cal_floating_prime(num):
    for i in range(1,4):
        print(num[:i+2])
        result = check_prime(float(num[:i+2]) * (10 ** i))
        if result == True:
            return True
    return False


num = float(input())
while 0.0 != num:
    if 0.1 < num < 10.0:
        print(cal_floating_prime(f"{num}"))
    num = float(input())
            
            

print(check_prime(num))
        


