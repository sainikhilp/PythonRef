
class Book():

    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages
    
    def __str__(self): # special function which returns a string representation of the object
        return f"{self.title} by {self.author}"
    
    def __len__(self):
        return self.pages

book=Book('Python rocks','nikhil',100)

print(book) # can also be written as print(str(book))
print(len(book))

