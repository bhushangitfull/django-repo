#Special methods aka constructor

class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return "Title: {}, Author: {}, Pages: {}".format(self.title,self.author,self.pages)


b1 = Book("lore-script", "jj-shon", 150)

print(b1)