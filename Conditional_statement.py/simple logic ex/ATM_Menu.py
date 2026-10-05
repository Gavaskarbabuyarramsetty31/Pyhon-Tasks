balance=10000
print('''
        -------ATM Menu-------
        1.Check Balance
        2.Deposit
        3.Withdraw
        4.Exit
        
      ''')
option=int(input("Enter the option :"))


match option:
    case 1:
        print("Current Balence :₹10,000")
    case 2:
        a=int(input("Enter the Deposit Amount"))
        print(f"Updated Balance :₹{balance+a}")
    case 3:
            b=int(input("Enter the Withdraw Amount"))
            print(f"Remaining Balance :₹{balance-b}")
    case 4:
        print("Thank you for using the ATM !")
    case _:
        print("invalid Option")
        