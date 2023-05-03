class Email:
    def __init__(self, title, sender, subject, text):
        self.title = title
        self.sender = sender
        self.subject = subject
        self.text = text
        self.position = 0
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def printQueue(self):
        print('\n' * 20)
        temp = self.first
        while temp:
            print(f"Title: {temp.title} | Sender: {temp.sender} | Subject: {temp.subject} | Text: {temp.text}")
            temp = temp.next

    def enqueue(self, title, sender, subject, text):
        new_email = Email(title, sender, subject, text)
        if self.first is None:
            self.first = new_email
            self.last = new_email
        else:
            self.last.next = new_email
            self.last = new_email
        self.length += 1
        new_email.position = self.length

    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        return temp
    
    def stash(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            return temp
        else:
            self.first = self.first.next
            self.last.next = temp
            self.last = temp
            temp.next = None
        return temp