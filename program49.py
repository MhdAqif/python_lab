class Publisher:
  def __init__(self,pid,pname):
    self.pid = pid
    self.pname = pname
  def display(self):
    print("Publisher ID :",self.pid)
    print("Publisher Name :",self.pname)
class Book(Publisher):
  def __init__(self,pid,pname,title,author):
    super().__init__(pid,pname)
    self.title = title
    self.author = author
  def display(self):
    super().display()
    print("Book title:",self.title)
    print("Author:",self.author)
class Python(Book):
  def __init__(self,pid,pname,title,author,price,pages):
    super().__init__(pid,pname,title,author)
    self.price = price
    self.pages = pages
  def display(self):
    super().display()
    print("Price:",self.price)
    print("Number of Pages:",self.pages)
p = Python(101,"ABC Publications","Python Programming","Guido van Rossum",500,350)
p.display()
