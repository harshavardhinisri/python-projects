from collections import defaultdict

class Contacts:
    def __init__(self):
        self.dict=defaultdict(None)

    def phoneBook(self):
        key=input("Enter the name:\n ")
        value=input("Enter the phone number:\n ")
        self.dict[key]=[value,[]]

    def get_phoneNumber(self):
        name=input("Enter the name to get phone number:\n ")
        print(self.dict[name][0])

    def sendMessage(self):
        print(self.dict.keys())
        name=input("Enter name: ")
        message=input("Enter the text message to send: ")
        self.dict[name][1].append(message)
        print("message sent")

    def getMessage(self):
        name=input("Enter name: ")
        print(self.dict[name][1])

    def getAll(self):
        print(self.dict.items())


contact=Contacts()
contact.phoneBook()
contact.phoneBook()
contact.getAll()
contact.get_phoneNumber()
contact.sendMessage()
contact.sendMessage()
contact.getMessage()
