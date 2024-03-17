import random

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

ROWS=3
COLS=3

sybmol_count = {
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

sybmol_value = {
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

def check_winnings(columns,lines,bet,values):
    winnings = 0
    winning_lines = []
    
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            sybmol_to_check = column[line]
            if symbol != sybmol_to_check:
                break
        else:
            winnings+=values[sybmol_to_check]*bet
            winning_lines.append(line+1)
    return winnings,winning_lines

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol,sybmol_count in symbols.items():
        for _ in range(sybmol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)            
        columns.append(column)
    
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i!= len(columns) -1:
                print(column[row],end=" | ")
            else:
                print(column[row],end="")
        print()

def deposit():
    while True:
        amount = input("Please enter your deposit $")
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
        lines = input("Enter number of lines you want to bet on (between 1 and " + str(MAX_LINES) + ") :")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("enter valid number of lines")
        else:
            print("enter valid input")
    return lines        

def  get_bet():
    while True:
        bet = input("Enter the amount you want to bet $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"your bet must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("enter valid input")
    return bet
    
def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet*lines
        if total_bet > balance:
            print(f"you dont have enough money to bet your current balance is ${balance}")
        else:
            break
    print(f"you have bet ${bet} on {lines} lines and your total bet is ${total_bet}")
    
    slots = get_slot_machine_spin(ROWS,COLS,sybmol_count)
    print_slot_machine(slots)
    winnings,winning_lines = check_winnings(slots,lines,bet,sybmol_value)
    print(f"you won ${winnings}.")
    print(f"you want on lines:",*winning_lines)
    
    
    
main()