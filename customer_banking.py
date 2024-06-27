# Import the create_cd_account and create_savings_account functions

# ADD YOUR CODE HERE
from Account import Account
from cd_account import create_cd_account
from savings_account import create_savings_account
from replit import clear



# Define the main function

def main():
    space = "\n"
    run = True
    current_balance = float(input("Enter Current Balance: $"))
    while run:
        response = input("1. Display Account Balance\n"
                        "2. Calculate Interest Earned - Savings Account\n"
                        "3. Calculate Interest Earned - CD Account\n"
                        "\n"
                        "Which option would you like to perform?\n"
                        )
        """This function prompts the user to enter the savings and cd account balance, interest rate,
        and the length of months to determine the interest gained.
        It displays the interest earned on the savings and CD accounts and updates the balances.
        """


        if response == '1':
                account = Account(current_balance, 0)
                current_balance = account.get_balance
                print(f"Current Account Balance: ${current_balance} ")
                keep_going = input("(\'c\') to continue\n"
                                    "(e) to exit program")
                if keep_going == 'e':
                    run = False
                elif keep_going == 'c':
                    continue
                else:
                    print("Please enter a valid option.")
        elif response == '2':
            savings_balance = float(input("Enter 'Saving Account' Balance: "))
            savings_interest = float(input("Enter Annual Interest Rate: "))
            savings_maturity = int(input("Enter the estimated number of months: "))
            # Call the create_savings_account function and pass the variables from the user.
            updated_saving_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

            # Print out the interest earned and updated savings account balance with interest earned for the given months.
            # ADD YOUR CODE HERE
            print(space)
            print(f"Updated \'Savings Account\' Balance:  ${updated_saving_balance:.2f}")
            print(f"Interest Earned: ${interest_earned:,.2f}")
            print(space)
            keep_going = input("(c) to continue\n"
                                "(e) to exit program")
            if keep_going == 'e':
                run = False
                break
            elif keep_going == 'c':
                main()
            else:
                print("Please enter a valid option.")
        elif response == '3':
            # Prompt the user to set the CD balance, interest rate, and months for the CD account.
            # ADD YOUR CODE HERE
            cd_balance = float(input("Enter 'CD Account' Balance: "))
            cd_interest = float(input("Enter the Annual Interest Rate - 'CD Account' : "))
            cd_maturity = int(input("Enter the number of months (maturity): "))
            # Call the create_cd_account function and pass the variables from the user.
            updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)
            print(space)
            print(f"Updated \'CD Account\' Balance:  ${updated_cd_balance:.2f}")
            print(f"Interest Earned: ${interest_earned:,.2f}")
            print(space)
            keep_going = input("(\'c\') to continue\n"
                                "(e) to exit program")
            if keep_going == 'e':
                run = False
                break
            elif keep_going == 'c':
                main()
            else:
                print("Please enter a valid entry.")
        else:
            print("Please enter a valid entry")
            
            # Prompt the user to set the savings balance, interest rate, and months for the savings account.
            # ADD YOUR CODE HERE

            

            # Print out the interest earned and updated CD account balance with interest earned for the given months.
            # ADD YOUR CODE HERE
        
if __name__ == "__main__":
    # Call the main function.
    main()