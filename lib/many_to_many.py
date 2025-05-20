class Book:
    all_books =[]
    def __init__(self,title):
        if not isinstance(title,str):
            raise Exception("Title must be string")
        self.title=title
        Book.all_books.append(self)#add book to the list of books

    
    def contracts(self):
        # This finds all contracts where THIS book is involved
        return [c for c in Contract.all if c.book == self]    
    
    def authors(self):
        return [c.author for c in self.contracts()]



class Author:
    all_authors = []
    def __init__(self,name):
        if not isinstance(name,str):
            raise Exception("Name must be a string")
        self.name = name
        Author.all_authors.append(self)#add to author list

    def contracts(self):
        return [c for c in Contract.all if c.author == self]

    def books(self):
        return [c.book for c in self.contracts()]

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum(c.royalties for c in self.contracts())    


class Contract:
    all = []
    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of Author")
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of Book")
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer")
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls,date):
        return [c for c in cls.all if c.date == date]
        