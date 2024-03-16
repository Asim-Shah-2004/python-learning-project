def deposit():
    while True:
        amount = input("Please enter your deposit $ ")
        if amount.isdigit():
            amount = int(amount)
            if amount>0 :
                break
            else:
                print("please enter an amount greater then 0")
        else:
            print("please enter a valid amount")

    return amount

deposit()