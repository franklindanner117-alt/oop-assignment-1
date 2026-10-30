from data.users import users

class Account: 

    def __init__(self, email: str, password: str, NIN: str, username: str) -> None:

        self.NIN = NIN
        self.email = email 
        self.username = username 
        self.password = password

        self.index = 0

    def sign_up(self) -> None: 

        users.append({"NIN": self.NIN, "email": self.email, "username": self.username, "password": self.password})
        print("\n\tYou've signed up successfully!")


    def sign_in(self) -> str: 

        emails = [user["email"] for user in users]

        self.index = emails.index(self.email)

        if self.email == users[self.index]["email"] and self.password == users[self.index]["password"]:
            return 'OK' 
        
        else: 

            print('\n[!] Access denied')
            return ''