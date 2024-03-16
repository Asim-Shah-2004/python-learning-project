MAX_LINES = 3

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

def get_number_of_lines():
    while True:
        lines = input("Enter number of lines you want to bet on (between 1 and " + str(MAX_LINES) + ") $ ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("enter valid number of lines")
        else:
            print("enter valid input")
    return lines        
    
def main():
    balance = deposit()
    lines = get_number_of_lines()
    print(balance,lines)
    
main()