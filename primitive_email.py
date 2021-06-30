class Email:
    def __init__(self, sender, receiver, content):
        self.is_sent = False
        self.sender = sender
        self.receiver = receiver
        self.content = content
    
    def send(self):
        self.is_sent = True
    
    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"

emails = []  
email_data = input()
while not email_data == "Stop":
    sender, receiver, content = email_data.split()
    email = Email(sender, receiver, content)
    emails.append(email)
    email_data = input()

indexes = [int(el) for el in input().split(", ")]

for index in indexes:
    emails[index].send()

for email in emails:
    print(email.get_info())
