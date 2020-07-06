class CellPhone:
    def __init__(self, tell_number, mail_address):
        self.tell_number = tell_number
        self.mail_address = mail_address

    def call(self):
        print(self.tell_number + "から発信します") 

    def send_mail(self):
        print(self.mail_address + "から送信します")
