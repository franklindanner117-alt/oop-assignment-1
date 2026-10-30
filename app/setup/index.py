from complinant.index import Complaint 
from admin.index import Admin 
from account.index import Account
from data.users import users

class Setup: 

    status: bool = False
    res: str = ''

    @classmethod 
    def exec(cls) -> None: 
        
        print("\n====================================")
        print(f" LAY COMPLAIN SL")
        print("================================================\n")

        choice = int(input('Enter (1) to sign in or (2) to sign up: \n\t '))

        if choice: 

            if choice == 1: 

                email = input('\nEnter your email: \n\t ')
                password = input('\nEnter your password: \n\t ')
                
                account = Account(email, password, NIN= "", username="") 

                res = account.sign_in() 

                if res == 'OK': 
                    status = True 

                else: 
                    status = False 

                emails = [user["email"] for user in users]

                user_index = emails.index(email)

                role = users[user_index]["role"] 

                NIN = users[user_index]["NIN"] 

                if status == True: 

                    if role == 'admin': 

                        admin = Admin()

                        while status == True: 

                            entry = int(input(f'\n1. View all complaints\n2. Remove complaint\n3. Logout\n\t  '))

                            if entry == 1: 

                                admin.view_all_complaints()

                            elif entry == 2: 

                                target_nin = input('\nEnter the NIN of the complinant whose complaint you may want to remove:  ')

                                admin.remove_complaint(target_nin)

                            elif entry == 3: 

                                status = False

                            else: 

                                print('\n\t[!] Invalid entry\n')


                    else: 

                        complinant = Complaint(NIN)

                        while status == True: 

                            entry = int(input(f'\n1. View complaint\n2. Add complaint\n3. Update complaint\n4. Logout\n\t  '))

                            if entry == 1: 

                                complinant.view_complaint() 

                            elif entry == 2: 

                                user_complaint = input('\nEnter your complaint here: \n\t')

                                complinant.add_complaint(user_complaint)

                            elif entry == 3: 

                                user_complaint = input('\nEnter your complaint here: \n\t')

                                complinant.update_complaint(user_complaint)

                            elif entry == 4: 

                                status = False 

                            else: 

                                print('\n\t[!] Invalid entry\n')


                    

            elif choice == 2: 

                NIN = input('\nEnter your NIN: \n\t ')
                email = input('\nEnter your email: \n\t ')
                username = input('\nEnter your username: \n\t ')
                password = input('\nEnter your password: \n\t ')

                account = Account(email, password, NIN, username) 

                account.sign_up() 

                status = True

                emails = [user["email"] for user in users]
                
                user_index = emails.index(email)
                
                NIN = users[user_index]["NIN"] 
                
                if status == True: 
                
                    complinant = Complaint(NIN.upper())
                                    
                    while status == True: 
                                    
                        entry = int(input(f'\n1. View complaint\n2. Add complaint\n3. Update complaint\n4. Logout\n\t  '))
                                    
                        if entry == 1: 
                                    
                            complinant.view_complaint() 
                                    
                        elif entry == 2: 
                                    
                            user_complaint = input('\nEnter your complaint here: \n\t')
                                    
                            complinant.add_complaint(user_complaint)
                                    
                        elif entry == 3: 
                                    
                            user_complaint = input('\nEnter your complaint here: \n\t')
                                    
                            complinant.update_complaint(user_complaint)
                                    
                        elif entry == 4: 
                                    
                            status = False 
                                    
                        else: 
                                    
                            print('\n\t[!] Invalid entry\n')
                
                        


            else: 
                print("\n\t[!] Invalid Entry") 


        else: 

            print('\n\t[!] Expected an input but got none')
        

                




