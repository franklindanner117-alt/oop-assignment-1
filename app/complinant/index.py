from data.complaints import complaints 

class Complaint: 

    def __init__(self, NIN: str) -> None:

        self.NIN = NIN
        self.index = 0

    def add_complaint(self, complaint) -> None: 

        complaints.append({"NIN": self.NIN, "complaint": complaint})

    def update_complaint(self, complaint) -> None: 

        NINs = [complaint["NIN"] for complaint in complaints]
        self.index = NINs.index(self.NIN)

        if not self.index: 
            print("\n\t[!] No complaint found")

        complaints[self.index]["complaint"] = complaint 
        print("\n\tUpdate went successfully!")

    def view_complaint(self) -> None: 

        NINs = [complaint["NIN"] for complaint in complaints]
        self.index = NINs.index(self.NIN)

        if not self.index: 
            print("\n\t[!] No complaint found")

        user_complaint = complaints[self.index]["complaint"]

        print("========================================================================================")
        print(f"Complaint: {user_complaint}")
        print("========================================================================================")
