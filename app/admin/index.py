from data.complaints import complaints

class Admin: 

    def __init__(self) -> None:

        self.index = 0

    def view_all_complaints(self) -> None: 
        
        print("COMPLAINTS")
    
        for complaint in complaints: 
            
            if len(complaint["NIN"]) != 0: 

                print("\n===================================================================================")
                print(f'NIN: {complaint["NIN"]} \nComplaint: {complaint["complaint"]}')
                print("===================================================================================\n")

    def remove_complaint(self, NIN: str) -> str: 

        NINs = [complaint["NIN"] for complaint in complaints]
        self.index = NINs.index(NIN.upper())
        
        if self.index: 
            complaints.remove(complaints[self.index])
            print("\n\tComplaint removed successfully!")
            return 'OK'

        print("\n\t[!] Complaint not found")
        print(f"{self.index}")
        return 'NOT FOUND'
    

        