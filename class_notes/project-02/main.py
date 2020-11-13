# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 12:27:52 2020

@author: platf
"""

import os
import csv

class Bank:

    def __init__(self):
        self.__file_name = 'bank.csv'
        self.__customer_record = None
        self.__local_data = {}
        self.__read_data()
        self.__login_screen()
        self.save_data()


    def __read_data(self):
        try:
            current_folder = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(current_folder, self.__file_name)

            file = open(file_path, "r")

            for line in file:
                col = line.rstrip("\n").split(';')
                self.__local_data[col[0]] = [
                    str(col[1]),
                    str(col[2]),
                    str(col[3]),
                    float(col[4]),
                    float(col[5])
                    ]

            file.close()
        except IOError:
            print("Bank services are not available")

    def __login_screen(self):
        print("""
              Bank System Login

                """)

        new = input("New customer?> Y/N")

        if new.upper() == 'Y':
            self.new_customer()

        account_number = input("Enter Acct Number: ")

        if self.__local_data.get(account_number):
            self.__customer_record = self.__local_data.get(account_number)

            self.password_check()

        else:
           print("Account number not found")
           self.__login_screen()



    def password_check(self):
        password = input("Enter password: ")

        if self.__customer_record[2] == password:
            Customer(self.__customer_record)
        else:
            print("Account not found")
            self.__login_screen()

    def set_local_data(self, new_cust_record):
        self.__local_data.update(new_cust_record)


    def get_local_data(self):
        return self.local_data


    def new_customer(self):
        new_cust_record = {}
        print("Your new account number is " + self.find_id_for_new_cutomer())
        fname = input("Enter first name: ")
        lname = input("Enter last name: ")
        password = input("Enter password: ")
        new_cust_record[self.find_id_for_new_cutomer()] = [fname,
                                                          lname,
                                                          password,
                                                          0,
                                                          0,]
        self.set_local_data(new_cust_record)

    def find_id_for_new_cutomer(self):
        return str(int(max(self.__local_data.keys())) + 1)

    def standardize_local_data(self):
        """
        need something to switch dictonary from key/value to ';' seperated list to save back to .csv
        """
        pass

    def save_data(self):
        try:
            test_file = 'bank2.csv'
            current_folder = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(current_folder, test_file)

            with open(file_path, "w") as csv_file:
                writer = csv.writer(csv_file)
                for key, value in self.__local_data.items():
                    writer.writerow([key, value])

            csv_file.close()
        except IOError:
            print("Bank services not responding to session end")


class Customer(Bank):

    def __init__(self, customer_record):
        self.customer_record = customer_record
        self.first_name = self.customer_record[0]
        self.last_name = self.customer_record[1]
        self.check_bal = self.customer_record[3]
        self.save_bal = self.customer_record[4]
        self.welcome_screen()



    def welcome_screen(self):
        print(f"""

              Hello, {self.first_name} welcome to the bank!

              """)
        print("1. Deposit")
        print("2. Withdrawal")
        print("3. Available Balances")
        print("4. Logout")
        option = int(input("""
                           Choose an option
                           """))

        if option == 1:
            self.deposit_menu()
        if option == 2:
            self.withdrawl_menu()
        if option == 3:
            self.display_acounts()
        if option == 4:
            Bank().save_data()

    def display_acounts(self):
        print(f'Checking balance: {self.check_bal}')
        print(f'Savings balance: {self.save_bal}')

    def deposit_menu(self):
        try:
            deposit_amt = float(input("How much would you like to deposit?"))
            acct = int(input("Which account 1 = Savings, 2 = Checking"))
        except:
            print("Invalid entry")

        if acct == 1:
            self.save_bal += deposit_amt
            print(f'Your new savings balance is {self.save_bal}')
        elif acct == 2:
            self.check_bal += deposit_amt
            print(f'Your new checking balance is {self.check_bal}')

    def withdrawl_menu(self):
        try:
            withdraw_amt = float(input("How much would you like to withdraw?"))
            acct = int(input("Which account 1 = Savings, 2 = Checking"))
        except:
            print("Invalid entry")

        if acct == 1:
            self.save_bal -= withdraw_amt
            print(f'Your new savings balance is {self.save_bal}')
        elif acct == 2:
            self.check_bal -= withdraw_amt
            print(f'Your new checking balance is {self.check_bal}')



def main():
    """
    function calls
    """
    bank = Bank()

    # cust = Customer(['suresh', 'sigera', 'juagw362', 1000.0, 10000.0])
    # cust.deposit_menu()
    # cust.withdrawl_menu()




# the driver code
if __name__ == '__main__':
    main()