# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# open_account()

def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance+money))
    return balance+money

def withdraw(balance, money):
    if (balance > money): # 잔액이 출금액보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance-money))
        return balance-money
    else:
        print("출금이 완료되지않았습니다. 잔액은 {0}원입니다.".format(balance))
        return balance

def withdraw_night(balance, money):
    commission = 100 # 수수료
    return commission, balance-money-commission

balance = 0 # 잔액
balance = deposit(balance, 1000)
# balance = withdraw(balance, 2000)
commission, balance = withdraw_night(balance, 500)
print("수수료 {0}원이며 잔액은 {1}원 입니다.".format(commission, balance))