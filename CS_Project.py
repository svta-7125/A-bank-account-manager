import os, sys, time
if not os.path.isdir("Accounts"): os.makedirs("Accounts")       

def breaker():
    for i in range(2):
        continue
def scroller(x):
    print(x, end="")
    a = '.....................................'
    for char in a:  
        sys.stdout.write(char)
        sys.stdout.flush()  
        time.sleep(0.06)
    print('Finished')
def scroller_alt(str):
    for char in str:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.06)
def add(name,Acc_No, amt):
    text = name +","+ str(Acc_No) +","+ str(amt)
    with open('Accounts/'+str(Acc_No)+'.txt', 'w') as f:
        f.write(text)        
    scroller('Saving')
def remove():
    print("Enter you account's number:")        
    try:
        accno = int(input())
        os.remove('Accounts/'+str(accno)+'.txt')
        scroller('Removing')
    except:
        print("This account does not exist, so not deleted.")
def edit(name, accno):
    try:
        with open('Accounts/'+str(accno)+'.txt', 'r') as f: data_list = f.readline().split(',')
    except: print("Account does not exist")
    print('''What will you like to edit?
        1) Name
        2) Account Number''')
    pick = int(input())
    if pick == 0:
        print("Shhhh, you found an easter egg. Way to go!")
    elif pick == 1:
        print("Enter new name")
        new_name = input()
        data_list[0] = new_name
        data_str = ""
        for i in data_list:
            data_str+=str(i)
            data_str+=","
        data_str = data_str[:len(data_str)-1]
        with open("Accounts/"+str(accno)+".txt", 'w') as f: f.write(str(data_str))
    elif pick == 2:
        print("Enter correct Account number")
        no = int(input())
        data_list.pop(1)
        data_list.insert(1, no)
        data_str = ""
        for i in data_list:
            data_str+=str(i)
            data_str+=","
        data_str = data_str[:len(data_str)-1]
        with open("Accounts/"+str(accno)+".txt", 'w') as f: f.write(str(data_str))
        old = "Accounts/"+str(accno)+".txt"
        new = "Accounts/"+str(no)+".txt"
        os.rename(old,new)
    else:
        print("Invalid input")
    scroller('Editing')
def withdraw(Acc_No, amount):
    try:
        with open('Accounts/'+str(Acc_No)+'.txt' ,'r') as f:
            data_list = f.readline().split(',')
    except:
        print("Invalid Account")
        sys.exit(1)
    if (int(data_list[2]) - amount) < 0:
        print("Not enough balance")
    else:
        balance = int(data_list[2]) - amount
        data_list[2] = str(balance)
        data_str = ""
        for i in data_list:
            data_str+=str(i)
            data_str+=","
        data_str = data_str[:len(data_str)-1]
        with open('Accounts/'+str(Acc_No)+'.txt' ,'w') as f:
            f.write(data_str)
        scroller('Withdrawing')
        print("Remaining balance: ", balance)
def deposit(Acc_No, amount):
    balance = int(data_list[2]) + amount
    data_list[2] = str(balance)
    data_str = ""
    for i in data_list:
        data_str+=str(i)
        data_str+=","
    data_str = data_str[:len(data_str)-1]
    with open('Accounts/'+str(Acc_No)+'.txt' ,'w') as f:
        f.write(data_str)
    scroller('Depositing')
    print("Total: ", balance)
print('''******************************************************************************************************************************                                             SVTA's Bank Manager Utility                                   ******
************************************************************************************************************************''')
while True:
    print('''
1) Add an account
2) Remove an account
3) Edit an existing account
4) Withdraw
5) Deposit
6) Exit''')
    print("\n What would you like to do?\n")
    try:
        choice = int(input())
    except:
        print("Invalid option")
        time.sleep(0.5)
        os.system('cls')
        continue
    if choice > 6:
        print("Invalid option")
        time.sleep(0.5)
        os.system('cls')
    if choice == 1:
        os.system('cls')
        scroller_alt("You will now add an account.........")
        time.sleep(0.5)
        os.system('cls')
        print("Enter name:")
        name = input()
        print("Enter Account number:")
        try: Acc_No = int(input())
        except:
            print("Invalid input.")
            continue
        print("Enter amount deposited:")
        try:amt = int(input())
        except:
            print("Invalid input.")
            continue
        add(name, Acc_No, amt)
    elif choice == 2:
        os.system('cls')
        print("Are you sure you want to delete your account?(y/n)")
        yn = input()
        if yn == "y" or yn == "Y": 
            os.system('cls')   
            scroller_alt('You will now remove your account.........')
            time.sleep(0.5)
            os.system('cls')
            remove()
        elif yn == "n" or yn == "N":
            scroller("Aborting")
            os.system('cls')
    elif choice == 3:
        os.system('cls')
        scroller_alt("You will now edit an existing account.........")
        time.sleep(0.5)
        os.system('cls')
        print("Enter your name")
        name = input()
        print("Enter Account Number")
        try:accno = int(input())
        except: 
            print("Invalid input")
            continue
        edit(name, accno)
    elif choice == 4:
        os.system('cls')
        scroller_alt("You will now withdraw money from your account.........")
        time.sleep(0.5)
        os.system('cls')
        print("Enter account number")
        try: x = int(input())
        except:
            print("Invalid input.")
            continue
        print("Enter how much would like to withdraw:")
        try: 
            y = int(input())
            if y < 0:
                print("Error: Negative number recieved")
                continue
        except:
            print("Invalid input.")
            continue
        withdraw(x,y)
    elif choice == 5:
        os.system('cls')
        scroller_alt("You will now deposit money to your account.........")
        time.sleep(0.5)
        os.system('cls')
        print("Enter account number")
        try: Acc_No = int(input())
        except:
            print("Invalid input")
            continue
        print("Enter how much would like to deposit:")
        try:amount = int(input())
        except:
            print("Invalid input")
        try:
            with open('Accounts/'+str(Acc_No)+'.txt' ,'r') as f:
                data_list = f.readline().split(',')
        except:
            print("Invalid Account")
            continue
        deposit(Acc_No, amount)
    elif choice == 6:
        scroller_alt("Thank you, exiting...........................")
        break
        
        
        
        
